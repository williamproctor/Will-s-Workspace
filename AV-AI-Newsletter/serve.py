#!/usr/bin/env python3
"""Dev server with HTTP range-request support (needed for audio seeking)."""

import os
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8091
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")


class RangeHTTPRequestHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        range_header = self.headers.get("Range")
        if not range_header:
            return super().do_GET()

        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            return super().do_GET()

        file_size = os.path.getsize(path)
        m = re.match(r"bytes=(\d+)-(\d*)", range_header)
        if not m:
            return super().do_GET()

        start = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else file_size - 1
        end = min(end, file_size - 1)
        length = end - start + 1

        self.send_response(206)
        ctype = self.guess_type(path)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
        self.send_header("Content-Length", str(length))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        with open(path, "rb") as f:
            f.seek(start)
            self.wfile.write(f.read(length))

    def end_headers(self):
        if not any(h[0] == "Accept-Ranges" for h in self._headers_buffer if isinstance(h, tuple)):
            self.send_header("Accept-Ranges", "bytes")
        super().end_headers()


if __name__ == "__main__":
    print(f"Serving AV-AI-Newsletter at http://localhost:{PORT}")
    print(f"  Root: {DIRECTORY}")
    print(f"  Site: http://localhost:{PORT}/site/index.html")
    httpd = HTTPServer(("", PORT), RangeHTTPRequestHandler)
    httpd.serve_forever()
