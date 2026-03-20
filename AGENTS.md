# AGENTS.md

## Cursor Cloud specific instructions

This is a static-content monorepo with three projects — no build tools, no package managers, no databases. The only runtime dependency is Python 3 (standard library only).

### Projects

| Project | Directory | Dev Server | Port |
|---|---|---|---|
| AV AI Newsletter | `AV-AI-Newsletter/` | `python3 AV-AI-Newsletter/serve.py` | 8091 |
| Positioning Quiz | `positioning-quiz/` | `python3 -m http.server 8092` (from `positioning-quiz/`) | 8092 |
| GitHub Pages (docs) | `docs/` | `python3 -m http.server 8093` (from `docs/`) | 8093 |

### Running locally

- **Newsletter**: `python3 AV-AI-Newsletter/serve.py` — serves at `http://localhost:8091`. Uses a custom `RangeHTTPRequestHandler` that supports HTTP range requests (required for audio/video seeking in embedded media).
- **Quiz**: `cd positioning-quiz && python3 -m http.server 8092` — serves at `http://localhost:8092`. The quiz runs in dev mode (`EMAIL_ENDPOINT` is `null`) so email capture stores to `localStorage` instead of calling an external API.
- **Docs**: `cd docs && python3 -m http.server 8093` — optional; serves GitHub Pages content.

### Non-obvious notes

- There are no lint, test, or build commands — all content is plain HTML/CSS/JS with no transpilation or bundling.
- The newsletter `serve.py` serves from the `AV-AI-Newsletter/site/` subdirectory, not the `AV-AI-Newsletter/` root. Edition markdown files in `editions/` and `research/` are source content, not served directly.
- Deployment targets: Vercel (`avaidispatch.com`) for the newsletter, GitHub Pages for `docs/`.
