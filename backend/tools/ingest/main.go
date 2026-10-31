// Command ingest validates the knowledge corpus and builds the Grokbot feed.
package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

type note struct {
	ID         string   `json:"id"`
	Domain     string   `json:"domain"`
	System     string   `json:"system"`
	Author     string   `json:"author"`
	ReviewedBy string   `json:"reviewed_by"`
	Status     string   `json:"status"`
	Severity   string   `json:"severity"`
	Created    string   `json:"created"`
	Tags       []string `json:"tags"`
	Title      string   `json:"title"`
	Body       string   `json:"body"`
	Path       string   `json:"path"`
	SHA256     string   `json:"sha256"`
}

var required = []string{"id", "domain", "system", "author", "reviewed_by", "status", "severity", "created", "tags"}

func main() {
	root := flag.String("root", "knowledge", "corpus root")
	out := flag.String("out", "dist", "output directory")
	flag.Parse()

	var notes []note
	var problems []string

	err := filepath.Walk(*root, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() || !strings.HasSuffix(path, ".md") || strings.HasSuffix(path, "SCHEMA.md") {
			return err
		}
		raw, err := os.ReadFile(path)
		if err != nil {
			return err
		}
		n, errs := parse(path, string(raw))
		if len(errs) > 0 {
			problems = append(problems, errs...)
			return nil
		}
		notes = append(notes, n)
		return nil
	})
	if err != nil {
		fmt.Fprintln(os.Stderr, "walk:", err)
		os.Exit(1)
	}

	seen := map[string]string{}
	for _, n := range notes {
		if prev, ok := seen[n.ID]; ok {
			problems = append(problems, fmt.Sprintf("%s: duplicate id %q also in %s", n.Path, n.ID, prev))
		}
		seen[n.ID] = n.Path
		if n.Status == "reviewed" && n.ReviewedBy == n.Author {
			problems = append(problems, n.Path+": reviewed_by equals author")
		}
		if want := filepath.Base(filepath.Dir(n.Path)); n.Domain != want {
			problems = append(problems, fmt.Sprintf("%s: domain %q does not match directory %q", n.Path, n.Domain, want))
		}
	}

	sort.Slice(notes, func(i, j int) bool { return notes[i].ID < notes[j].ID })

	if len(problems) > 0 {
		for _, p := range problems {
			fmt.Fprintln(os.Stderr, "FAIL", p)
		}
		fmt.Fprintf(os.Stderr, "%d problem(s)\n", len(problems))
		os.Exit(1)
	}

	if err := os.MkdirAll(*out, 0o755); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	f, err := os.Create(filepath.Join(*out, "corpus.jsonl"))
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	defer f.Close()
	enc := json.NewEncoder(f)
	for _, n := range notes {
		if err := enc.Encode(n); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
	}
	idx, _ := json.MarshalIndent(map[string]any{"count": len(notes), "notes": notes}, "", "  ")
	if err := os.WriteFile(filepath.Join(*root, "index.json"), append(idx, 10), 0o644); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Printf("%d notes ingested\n", len(notes))
}

func parse(path, raw string) (note, []string) {
	var n note
	var errs []string
	n.Path = filepath.ToSlash(path)
	if !strings.HasPrefix(raw, "---\n") {
		return n, []string{path + ": missing front-matter"}
	}
	end := strings.Index(raw[4:], "\n---\n")
	if end < 0 {
		return n, []string{path + ": unterminated front-matter"}
	}
	fm, rest := raw[4:4+end], raw[4+end+5:]
	fields := map[string]string{}
	for _, line := range strings.Split(fm, "\n") {
		k, v, ok := strings.Cut(line, ":")
		if !ok {
			continue
		}
		fields[strings.TrimSpace(k)] = strings.TrimSpace(v)
	}
	for _, k := range required {
		if fields[k] == "" {
			errs = append(errs, fmt.Sprintf("%s: missing field %q", path, k))
		}
	}
	n.ID, n.Domain, n.System = fields["id"], fields["domain"], fields["system"]
	n.Author, n.ReviewedBy, n.Status = fields["author"], fields["reviewed_by"], fields["status"]
	n.Severity, n.Created = fields["severity"], fields["created"]
	tags := strings.Trim(fields["tags"], "[]")
	for _, t := range strings.Split(tags, ",") {
		if t = strings.TrimSpace(t); t != "" {
			n.Tags = append(n.Tags, t)
		}
	}
	if len(n.Tags) < 2 {
		errs = append(errs, path+": needs at least two tags")
	}
	switch n.Status {
	case "draft", "reviewed", "superseded":
	default:
		errs = append(errs, path+": bad status "+n.Status)
	}
	for _, h := range []string{"## Context", "## What happened", "## Root cause", "## What we changed", "## What we would do differently", "## Evidence"} {
		if !strings.Contains(rest, h) {
			errs = append(errs, path+": missing section "+h)
		}
	}
	if i := strings.Index(rest, "\n# "); i >= 0 {
		if j := strings.Index(rest[i+1:], "\n"); j >= 0 {
			n.Title = strings.TrimSpace(rest[i+3 : i+1+j])
		}
	}
	n.Body = strings.TrimSpace(rest)
	sum := sha256.Sum256([]byte(raw))
	n.SHA256 = hex.EncodeToString(sum[:])
	return n, errs
}
