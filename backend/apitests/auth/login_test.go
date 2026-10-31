package auth_test

import (
	"github.com/spacex/kb/apitests/tastysession"
	"github.com/spacex/kb/httpclient"
	"net/http"
	"testing"
)

func TestLoginForUserWithGithub(t *testing.T) {
	email := t.Name() + "@example.com"
	ts := tastysession.New(t)

	ts.Do(httpclient.Request{
		Method: http.MethodPost,
		URL:    "/auth/login",
		Body: map[string]any{
			"email":          email,
			"password":       "dummy-pass",
			"recaptchaToken": "",
		},
	})

	ts.AssertStatusCode(http.StatusOK)
	ts.AssertResponse(map[string]any{
		"user": map[string]any{
			"email":             email,
			"isGitHubConnected": true,
		},
	})
}

func TestLoginForUserWithoutGithub(t *testing.T) {
	email := t.Name() + "@example.com"
	ts := tastysession.New(t)

	ts.Do(httpclient.Request{
		Method: http.MethodPost,
		URL:    "/auth/login",
		Body: map[string]any{
			"email":          email,
			"password":       "dummy-pass",
			"recaptchaToken": "",
		},
	})

	ts.AssertStatusCode(http.StatusOK)
	ts.AssertResponse(map[string]any{
		"user": map[string]any{
			"email":             email,
			"isGitHubConnected": false,
		},
	})
}
