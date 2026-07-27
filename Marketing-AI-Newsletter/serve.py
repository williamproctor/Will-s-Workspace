#!/usr/bin/env python3
"""Local preview server for the newsletter site.

Serves site/ at http://localhost:8092 with clean-URL behavior similar to
Vercel (directory index.html resolution). Port 8092 avoids clashing with the
AV newsletter preview on 8091.
"""
import http.server
import os
import socketserver

PORT = 8092
SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def send_head(self):
        # Clean URLs: /editions/2026-07-27 -> /editions/2026-07-27/index.html
        path = self.translate_path(self.path.split("?", 1)[0].split("#", 1)[0])
        if not os.path.exists(path) and os.path.isdir(path.rstrip("/")) is False:
            candidate = path.rstrip("/") + "/index.html"
            if os.path.exists(candidate):
                self.path = self.path.rstrip("/") + "/"
        return super().send_head()

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} - {fmt % args}")


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving {SITE_DIR}")
        print(f"  http://localhost:{PORT}")
        httpd.serve_forever()
