// Monday Signal — email signup endpoint (Vercel serverless function).
//
// Adds a contact to the Resend audience configured by RESEND_AUDIENCE_ID.
// Keeps the API key server-side; the static site only ever POSTs here.
//
// Accepts JSON ({ email, website }) or a classic form POST. The `website`
// field is a honeypot: humans never see it, bots fill it, and we answer
// with a fake success so they learn nothing.

const RESEND_API = "https://api.resend.com";
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const MAX_EMAIL_LENGTH = 254;

const MESSAGES = {
  ok: "You're on the list. See you Monday.",
  exists: "You're already on the list. See you Monday.",
  invalid: "Enter a valid email address.",
  unavailable: "Signups aren't switched on yet. Check back soon.",
  failed: "Couldn't subscribe right now. Try again in a minute.",
};

function parseBody(req) {
  const body = req.body;
  if (!body) return {};
  if (typeof body === "object") return body;
  const type = String(req.headers["content-type"] || "");
  if (type.includes("application/json")) {
    try {
      return JSON.parse(body);
    } catch (err) {
      return {};
    }
  }
  return Object.fromEntries(new URLSearchParams(String(body)));
}

function wantsHtml(req) {
  const type = String(req.headers["content-type"] || "");
  const accept = String(req.headers.accept || "");
  return !type.includes("application/json") && accept.includes("text/html");
}

function respond(req, res, status, payload) {
  if (wantsHtml(req)) {
    const state = payload.ok ? "ok" : "error";
    const params = new URLSearchParams({ subscribed: state, msg: payload.message || payload.error || "" });
    res.statusCode = 303;
    res.setHeader("Location", `/?${params.toString()}#subscribe`);
    return res.end();
  }
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  return res.end(JSON.stringify(payload));
}

async function addContact(apiKey, audienceId, email) {
  const response = await fetch(`${RESEND_API}/audiences/${audienceId}/contacts`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, unsubscribed: false }),
  });
  let data = {};
  try {
    data = await response.json();
  } catch (err) {
    data = {};
  }
  return { status: response.status, data };
}

module.exports = async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Content-Type-Options", "nosniff");

  if (req.method === "OPTIONS") {
    res.setHeader("Allow", "POST, OPTIONS");
    res.statusCode = 204;
    return res.end();
  }
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST, OPTIONS");
    return respond(req, res, 405, { ok: false, error: "Method not allowed." });
  }

  const body = parseBody(req);
  const email = String(body.email || "").trim().toLowerCase();
  const honeypot = String(body.website || "").trim();

  if (honeypot) {
    return respond(req, res, 200, { ok: true, message: MESSAGES.ok });
  }
  if (!EMAIL_RE.test(email) || email.length > MAX_EMAIL_LENGTH) {
    return respond(req, res, 400, { ok: false, error: MESSAGES.invalid });
  }

  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;
  if (!apiKey || !audienceId) {
    return respond(req, res, 503, { ok: false, error: MESSAGES.unavailable });
  }

  try {
    const { status, data } = await addContact(apiKey, audienceId, email);
    if (status >= 200 && status < 300) {
      return respond(req, res, 200, { ok: true, message: MESSAGES.ok });
    }
    const detail = String((data && (data.message || data.name)) || "").toLowerCase();
    if (status === 409 || detail.includes("already")) {
      return respond(req, res, 200, { ok: true, message: MESSAGES.exists });
    }
    console.error("resend contact create failed", status, data);
    return respond(req, res, 502, { ok: false, error: MESSAGES.failed });
  } catch (err) {
    console.error("resend request error", err);
    return respond(req, res, 502, { ok: false, error: MESSAGES.failed });
  }
};

module.exports.MESSAGES = MESSAGES;
