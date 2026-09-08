#!/usr/bin/env python3
"""One-time Resend setup for Monday Signal's email list.

Needs RESEND_API_KEY in the environment (a Full-access key). No third-party
dependencies; talks to https://api.resend.com with urllib.

Usage:
    python3 scripts/resend_setup.py domain add            # register the domain from config.json, print DNS records
    python3 scripts/resend_setup.py domain status         # show verification status + records again
    python3 scripts/resend_setup.py domain verify         # ask Resend to re-check DNS
    python3 scripts/resend_setup.py audience create       # create the "Monday Signal" audience, print its id
    python3 scripts/resend_setup.py audience list
    python3 scripts/resend_setup.py contacts count        # how many contacts are in RESEND_AUDIENCE_ID

The domain and audience ids are printed, not stored: put RESEND_AUDIENCE_ID in
Vercel's environment variables (next to RESEND_API_KEY) and flip
config.subscribe.enabled to true once the domain shows "verified".
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.resend.com"
CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"


def api(method: str, path: str, payload: dict | None = None) -> dict:
    key = os.environ.get("RESEND_API_KEY")
    if not key:
        sys.exit("RESEND_API_KEY is not set. Add it as a Cloud Agent secret (or export it) and rerun.")
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        f"{API}{path}",
        data=data,
        method=method,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", errors="replace")
        sys.exit(f"Resend API {method} {path} failed: HTTP {err.code}\n{detail}")


def site_domain() -> str:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return str(config.get("domain", "")).replace("https://", "").replace("http://", "").strip("/")


def print_records(domain: dict) -> None:
    print(f"\nDomain: {domain.get('name')}   id: {domain.get('id')}   status: {domain.get('status')}")
    records = domain.get("records") or []
    if not records:
        print("  (no records returned)")
        return
    print("\nAdd these DNS records where mondaysignal.com's DNS lives:\n")
    print(f"  {'TYPE':<6} {'NAME (host)':<34} {'VALUE':<70} {'PRIORITY':<9} {'STATUS'}")
    for rec in records:
        print(
            f"  {str(rec.get('type', '')):<6} {str(rec.get('name', '')):<34} "
            f"{str(rec.get('value', '')):<70} {str(rec.get('priority', '') or ''):<9} {rec.get('status', '')}"
        )
    print(
        "\nNotes: TTL can stay at your host's default. The MX + TXT pair on the 'send' subdomain "
        "handles bounces (SPF); the TXT under resend._domainkey is DKIM. Also add a DMARC record if none exists:\n"
        "  TXT  _dmarc   v=DMARC1; p=none; rua=mailto:dmarc@" + site_domain()
    )


def find_domain(name: str) -> dict | None:
    for item in api("GET", "/domains").get("data", []):
        if item.get("name") == name:
            return item
    return None


def cmd_domain(action: str) -> None:
    name = site_domain()
    if action == "add":
        existing = find_domain(name)
        if existing:
            print(f"{name} is already registered in Resend; showing its records.")
            print_records(api("GET", f"/domains/{existing['id']}"))
            return
        created = api("POST", "/domains", {"name": name})
        print_records(created)
    elif action in ("status", "verify"):
        found = find_domain(name)
        if not found:
            sys.exit(f"{name} is not registered yet. Run: domain add")
        if action == "verify":
            api("POST", f"/domains/{found['id']}/verify")
            print("Verification requested; Resend re-checks DNS asynchronously.")
        print_records(api("GET", f"/domains/{found['id']}"))
    else:
        sys.exit("domain actions: add | status | verify")


def cmd_audience(action: str, name: str = "Monday Signal") -> None:
    if action == "create":
        for item in api("GET", "/audiences").get("data", []):
            if item.get("name") == name:
                print(f"Audience '{name}' already exists: RESEND_AUDIENCE_ID={item['id']}")
                return
        created = api("POST", "/audiences", {"name": name})
        print(f"Created audience '{name}': RESEND_AUDIENCE_ID={created.get('id')}")
        print("Add that id to Vercel's environment variables, then set config.subscribe.enabled to true and rebuild.")
    elif action == "list":
        for item in api("GET", "/audiences").get("data", []):
            print(f"  {item.get('id')}  {item.get('name')}  created {item.get('created_at')}")
    else:
        sys.exit("audience actions: create | list")


def cmd_contacts(action: str) -> None:
    audience_id = os.environ.get("RESEND_AUDIENCE_ID")
    if not audience_id:
        sys.exit("RESEND_AUDIENCE_ID is not set.")
    contacts = api("GET", f"/audiences/{audience_id}/contacts").get("data", [])
    active = [c for c in contacts if not c.get("unsubscribed")]
    if action == "count":
        print(f"{len(active)} active contact(s), {len(contacts) - len(active)} unsubscribed.")
    else:
        sys.exit("contacts actions: count")


def main() -> None:
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    group, action = args[0], args[1]
    if group == "domain":
        cmd_domain(action)
    elif group == "audience":
        cmd_audience(action, *args[2:3])
    elif group == "contacts":
        cmd_contacts(action)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
