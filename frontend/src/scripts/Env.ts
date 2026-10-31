import m from "mithril"

declare const process: {
	env: {
		NODE_ENV?: string
		KB_ALLOWED_HOSTS: string
		KB_FRONTEND_ROLLBAR_TOKEN?: string
		KB_EXT_URL_PREFIX?: string
	}
}

const NODE_ENV = process.env.NODE_ENV || "production"

const KB_BACKEND = "/"

export const GIST_API_PREFIX = KB_BACKEND + "gist/"

export const EXT_URL_PREFIX = (process.env.KB_EXT_URL_PREFIX || "").trim()

export const rollbarToken: null | string = (() => {
	const token = (process.env.KB_FRONTEND_ROLLBAR_TOKEN || "").trim()
	return token != null && token !== "" ? token : null
})()

export const name: string = (() => {
	return NODE_ENV != null && NODE_ENV !== "" ? NODE_ENV : "production"
})()

let recaptchaSiteKey: null | string = null

export async function getRecaptchaSiteKey(): Promise<string> {
	if (recaptchaSiteKey == null) {
		const response = await m.request<{ recaptchaSiteKey: string }>({
			method: "GET",
			url: KB_BACKEND + "env",
		})
		recaptchaSiteKey = response.recaptchaSiteKey
	}
	return recaptchaSiteKey
}

export function isDev(): boolean {
	return name === "development"
}

export function proxyUrl(): string {
	console.log("proxyUrl", KB_BACKEND)
	return KB_BACKEND + "proxy"
}

export function authUrl(): string {
	return KB_BACKEND + "auth/"
}

export function storageUrl(): string {
	// Commented out since support for storage backend is deprioritized/almost-deprecated.
	return ""  // KB_BACKEND + "storage/"
}

export function allowedToStart(): boolean {
	return process.env.KB_ALLOWED_HOSTS == null ||
		process.env.KB_ALLOWED_HOSTS.split(",").includes(window.location.host)
}
