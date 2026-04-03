# New Mac Setup — Will Proctor's Complete Migration Guide

> **Generated:** 2026-04-03 from auditing the current MacBook.
> **Purpose:** Give a fresh Cursor instance on a new Mac everything it needs to clone this exact environment.

---

## Table of Contents

1. [Phase 1 — macOS System Preferences](#phase-1--macos-system-preferences)
2. [Phase 2 — Homebrew + CLI Tools](#phase-2--homebrew--cli-tools)
3. [Phase 3 — Runtimes (Node, Python, Bun, Deno, uv)](#phase-3--runtimes)
4. [Phase 4 — Global Packages](#phase-4--global-packages)
5. [Phase 5 — Shell Configuration](#phase-5--shell-configuration)
6. [Phase 6 — Git + GitHub + SSH](#phase-6--git--github--ssh)
7. [Phase 7 — Clone All Repos](#phase-7--clone-all-repos)
8. [Phase 8 — Cursor Configuration](#phase-8--cursor-configuration)
9. [Phase 9 — MCP Server Setup](#phase-9--mcp-server-setup)
10. [Phase 10 — Claude Code + Peon-Ping](#phase-10--claude-code--peon-ping)
11. [Phase 11 — Fonts](#phase-11--fonts)
12. [Phase 12 — macOS Applications](#phase-12--macos-applications)
13. [Phase 13 — Verification Checklist](#phase-13--verification-checklist)

---

## Phase 1 — macOS System Preferences

```bash
# Dock: auto-hide
defaults write com.apple.dock autohide -bool true

# Finder: show path bar
defaults write com.apple.finder ShowPathbar -bool true

# Restart affected services
killall Dock
killall Finder
```

---

## Phase 2 — Homebrew + CLI Tools

### Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### Install all packages from Brewfile

Save this as `~/Brewfile` and run `brew bundle`:

```ruby
tap "runpod/runpodctl"
brew "ffmpeg"
brew "gh"
brew "git"
brew "git-lfs"
brew "rclone"
brew "tmux"
brew "yt-dlp"
brew "deno"
brew "runpod/runpodctl/runpodctl"
```

```bash
brew bundle --file=~/Brewfile
git lfs install
```

---

## Phase 3 — Runtimes

### Node.js v22 (local install, no version manager)

Node is installed to `~/.local/node/` (not via nvm/fnm/volta).

```bash
# Download and install Node 22 LTS
mkdir -p ~/.local
curl -fsSL https://nodejs.org/dist/v22.13.1/node-v22.13.1-darwin-arm64.tar.xz | tar -xJ -C ~/.local
mv ~/.local/node-v22.13.1-darwin-arm64 ~/.local/node
```

### Python 3.14 (via Homebrew)

```bash
brew install python@3.14
```

> Note: Python 3.11 is also on the current PATH (from `/Library/Frameworks/Python.framework/Versions/3.11`). Install from python.org if needed for legacy compatibility.

### uv (Python package manager)

```bash
curl -fsSL https://astral.sh/uv/install.sh | sh
# Installs to ~/.local/bin/uv and ~/.local/bin/uvx
```

### Bun

```bash
curl -fsSL https://bun.sh/install | bash
# Installs to ~/.bun/bin/bun (v1.3.9)
```

### Deno

Already covered by `brew install deno` above.

---

## Phase 4 — Global Packages

### npm globals

```bash
npm install -g @anthropic-ai/claude-code
npm install -g @augmentcode/auggie
npm install -g @ainyc/canonry
npm install -g obsidian-local-rest-api-mcp
npm install -g wrangler
```

### pip globals

```bash
pip3 install google-genai google-generativeai google-api-python-client pillow httpx websockets pydantic requests tqdm
```

---

## Phase 5 — Shell Configuration

### ~/.zprofile

```bash
cat > ~/.zprofile << 'ZPROFILE'
# Node.js (local install)
export PATH="$HOME/.local/node/bin:$PATH"

eval "$(/opt/homebrew/bin/brew shellenv)"
ZPROFILE
```

### ~/.zshrc

```bash
cat > ~/.zshrc << 'ZSHRC'
alias peon="bash ~/.claude/hooks/peon-ping/peon.sh"
[ -f /Users/wil/.claude/hooks/peon-ping/completions.bash ] && source /Users/wil/.claude/hooks/peon-ping/completions.bash

# bun completions
[ -s "$HOME/.bun/_bun" ] && source "$HOME/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

. "$HOME/.local/bin/env"
ZSHRC
```

### ~/.local/bin/env

This file is auto-created by the uv installer. It adds `~/.local/bin` to PATH. If missing after installing uv, create it:

```bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/env << 'ENV'
#!/bin/sh
case ":${PATH}:" in
    *:"$HOME/.local/bin":*) ;;
    *) export PATH="$HOME/.local/bin:$PATH" ;;
esac
ENV
```

---

## Phase 6 — Git + GitHub + SSH

### Git global config

```bash
git config --global user.name "Will Proctor"
git config --global user.email "c-will.proctor@growthx.ai"
git config --global filter.lfs.clean "git-lfs clean -- %f"
git config --global filter.lfs.smudge "git-lfs smudge -- %f"
git config --global filter.lfs.process "git-lfs filter-process"
git config --global filter.lfs.required true
git config --global credential.https://github.com.helper ""
git config --global credential.https://github.com.helper "!/opt/homebrew/bin/gh auth git-credential"
git config --global credential.https://gist.github.com.helper ""
git config --global credential.https://gist.github.com.helper "!/opt/homebrew/bin/gh auth git-credential"
```

### SSH key

Generate a new ED25519 key on the new Mac (do NOT copy the old private key):

```bash
ssh-keygen -t ed25519 -C "c-will.proctor@growthx.ai"
cat ~/.ssh/id_ed25519.pub
# Copy the output and add it to: https://github.com/settings/keys
```

### GitHub CLI auth

```bash
gh auth login
# Choose: GitHub.com → HTTPS → Authenticate via browser
# Scopes needed: gist, read:org, repo
```

Verify:

```bash
gh auth status
```

---

## Phase 7 — Clone All Repos

### Personal repos (williamproctor)

```bash
mkdir -p ~/Documents/GitHub && cd ~/Documents/GitHub

gh repo clone williamproctor/Will-s-Workspace
gh repo clone williamproctor/growthx-system
gh repo clone williamproctor/content-vault
gh repo clone williamproctor/gemini-trial-survey
gh repo clone williamproctor/the-open-door
gh repo clone williamproctor/growthx-landing-prototype
gh repo clone williamproctor/raffle-wheel
```

### Organization repos (GrowthX-Productivity)

```bash
gh repo clone GrowthX-Productivity/gtm-brain
gh repo clone GrowthX-Productivity/strategy-os
gh repo clone GrowthX-Productivity/products
```

### Organization repos (growthxai)

```bash
gh repo clone growthxai/clients-workflows
gh repo clone growthxai/capacity_manager
gh repo clone growthxai/output
gh repo clone growthxai/tcli
gh repo clone growthxai/os-workflows
gh repo clone growthxai/gx-workflows
gh repo clone growthxai/output-web
gh repo clone growthxai/website-q2
gh repo clone growthxai/output-examples
gh repo clone growthxai/fleet
gh repo clone growthxai/training-modules
gh repo clone growthxai/assets-redirect
gh repo clone growthxai/output-launch
gh repo clone growthxai/checkthat-workflows
gh repo clone growthxai/gemini-trial-survey
gh repo clone growthxai/starter
gh repo clone growthxai/growthx.ai-learn
gh repo clone growthxai/shipstack
gh repo clone growthxai/handbook
gh repo clone growthxai/industry-playbooks
```

### External collaboration repos

```bash
gh repo clone nikopueringer/CorridorKey
```

### Set non-default branches where needed

```bash
cd ~/Documents/GitHub/gtm-brain && git checkout playbook/video-packaging
cd ~/Documents/GitHub
```

### gemini-trial-survey dual remote

```bash
cd ~/Documents/GitHub/gemini-trial-survey
git remote add growthx https://github.com/growthxai/gemini-trial-survey.git
cd ~/Documents/GitHub
```

---

## Phase 8 — Cursor Configuration

### Cursor user settings

File: `~/Library/Application Support/Cursor/User/settings.json`

```json
{
    "window.commandCenter": true,
    "editor.accessibilitySupport": "on"
}
```

### Cursor workspace rules (auto-cloned with Will-s-Workspace)

These live in the repo at `.cursor/rules/` and `.cursor/skills/`:

- `.cursor/rules/auto-memory-extraction.mdc`
- `.cursor/rules/background-ideation.mdc`
- `.cursor/rules/exec-safety.mdc`
- `.cursor/rules/stuck-protocol.mdc`
- `.cursor/rules/plan-mode-review.mdc`
- `.cursor/rules/obsidian-knowledge-base.mdc`
- `.cursor/rules/git-worktree-isolation.mdc`
- `.cursor/skills/video-pre-production/SKILL.md`
- `.cursor/skills/blog-to-video/SKILL.md`
- `.cursor/skills/workshop-deck-builder/SKILL.md`

These come with the repo clone — no manual action needed.

### User-level Cursor skills (~/.cursor/skills/)

These need to be manually migrated. Copy from old Mac or re-create:

```
~/.cursor/skills/
├── peon-ping-config/SKILL.md
├── peon-ping-toggle/SKILL.md
├── remotion-best-practices -> ~/.agents/skills/remotion-best-practices (symlink)
├── growthx-landing-page/SKILL.md
├── youtube-packaging-optimizer/SKILL.md
└── av-ai-newsletter/SKILL.md

~/.cursor/skills-cursor/
├── babysit/SKILL.md
├── create-rule/SKILL.md
├── create-skill/SKILL.md
└── update-cursor-settings/SKILL.md
```

**Transfer method:** AirDrop the `~/.cursor/skills/` and `~/.cursor/skills-cursor/` folders, or push them to a private gist/repo.

### Codex skills (~/.codex/skills/)

```
~/.codex/skills/
└── suno-ui-composer/SKILL.md
```

---

## Phase 9 — MCP Server Setup

### Global MCP config (~/.cursor/mcp.json)

```json
{
  "mcpServers": {
    "ahrefs": {
      "command": "/Users/NEW_USERNAME/.local/node/bin/npx",
      "args": ["-y", "mcp-remote", "https://api.ahrefs.com/mcp/mcp"],
      "env": {
        "PATH": "/Users/NEW_USERNAME/.local/node/bin:/usr/local/bin:/usr/bin:/bin"
      }
    },
    "ordinal": {
      "command": "/Users/NEW_USERNAME/.local/node/bin/npx",
      "args": ["-y", "mcp-remote", "https://app.tryordinal.com/api/mcp", "--header", "Authorization: Bearer YOUR_ORDINAL_TOKEN"],
      "env": {
        "PATH": "/Users/NEW_USERNAME/.local/node/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

> Replace `NEW_USERNAME` with the macOS username and `YOUR_ORDINAL_TOKEN` with the Ordinal API token.

### Workspace MCP config (Will-s-Workspace/.cursor/mcp.json)

This file is in the repo but contains secrets. After cloning, update:

- **Obsidian API key** — regenerate from Obsidian's Local REST API plugin settings
- **XAgent Twitter API key** — get from getxagent.com dashboard
- **TalkToFigma** — uses bunx, works automatically
- **Figma** — OAuth, works automatically

### XAgent binary

```bash
# Re-download x-mcp binary
# Check getxagent.com for latest install instructions
# Binary goes to ~/.local/bin/x-mcp
```

---

## Phase 10 — Claude Code + Peon-Ping

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude auth login
```

### Claude settings (~/.claude/settings.json)

```json
{
  "hooks": {
    "SessionStart": [{"matcher": "", "hooks": [{"type": "command", "command": "/Users/NEW_USERNAME/.claude/hooks/peon-ping/peon.sh", "timeout": 10}]}],
    "UserPromptSubmit": [{"matcher": "", "hooks": [{"type": "command", "command": "/Users/NEW_USERNAME/.claude/hooks/peon-ping/peon.sh", "timeout": 10}]}],
    "Stop": [{"matcher": "", "hooks": [{"type": "command", "command": "/Users/NEW_USERNAME/.claude/hooks/peon-ping/peon.sh", "timeout": 10}]}],
    "Notification": [{"matcher": "", "hooks": [{"type": "command", "command": "/Users/NEW_USERNAME/.claude/hooks/peon-ping/peon.sh", "timeout": 10}]}],
    "PermissionRequest": [{"matcher": "", "hooks": [{"type": "command", "command": "/Users/NEW_USERNAME/.claude/hooks/peon-ping/peon.sh", "timeout": 10}]}]
  }
}
```

> Replace `NEW_USERNAME` with the macOS username.

### Peon-Ping (StarCraft notification sounds)

The peon-ping system lives at `~/.claude/hooks/peon-ping/`. It includes:
- `peon.sh` — main script
- `relay.sh` — relay adapter
- `config.json` — settings
- `packs/` — sound packs (sc_scv, sc_battlecruiser, sc_kerrigan)
- `adapters/` — IDE adapters (cursor, codex, etc.)

**Transfer method:** AirDrop `~/.claude/hooks/` from old Mac or reinstall from source (check the peon-ping skill docs for install URL).

---

## Phase 11 — Fonts

The current Mac has **~180 custom font files** in `~/Library/Fonts/`. Key font families:

| Font Family | Type | Usage |
|---|---|---|
| **AktivGrotesk** | Sans (full weight range) | Corporate/brand |
| **ABCWhyte / WhyteInktrap** | Sans | Design |
| **Barlow / BarlowCondensed / BarlowSemiCondensed** | Sans (full) | UI / presentations |
| **BerkeleyMono** | Mono | Code editor |
| **ClashDisplay** | Display | Headlines |
| **ElzaTrial** (Cond/Narrow/Regular) | Sans | Design system |
| **GeneralSans** | Sans | Modern UI |
| **Gotham / GothamNarrow** | Sans | Brand |
| **Haffer / HafferSQ** | Sans | Modern |
| **Inter** (18/24/28pt + Variable) | Sans | UI standard |
| **Lato** | Sans | Web |
| **Manrope** | Sans Variable | Modern UI |
| **MessinaSans** | Sans | Premium brand |
| **Montserrat / MontserratAlternates** | Sans | Presentations |
| **Poppins** | Sans | Web / marketing |
| **Prompt** | Sans | Thai-compatible |
| **Raleway** | Sans | Elegant headers |
| **Roboto** (all variants) | Sans | Google standard |
| **Saans / SaansMono / SaansSemiMono** | Sans/Mono | Code + UI |
| **SuisseIntl** | Sans | Premium brand |
| **UniversalSans** | Display + Text | Brand |
| **Vollkorn / VollkornSC** | Serif | Long-form reading |
| **Comfortaa** | Display | Friendly UI |
| **CrimsonText** | Serif | Elegant |

**Also installed (display/novelty):** Dendritic Voltage, Dream Orphans, Fava, Hello Paris (Sans/Script/Serif), Madrigal, PolySans, Stellar, TrashHand, Asgalt, 5364ANSI, Highway Gothic variants.

**Transfer method:** AirDrop `~/Library/Fonts/` folder from old Mac. Or if you have the `Fonts/` folder in the workspace repo, copy from there:

```bash
cp -r ~/Documents/GitHub/Will-s-Workspace/Fonts/* ~/Library/Fonts/
```

---

## Phase 12 — macOS Applications

Install in priority order. Items marked **(App Store)** come from the Mac App Store. Items marked **(Web)** need manual download.

### Tier 1 — Essential (install first day)

| App | Source |
|---|---|
| 1Password | App Store |
| Cursor | cursor.com |
| Google Chrome | Web |
| Slack | App Store |
| Figma | figma.com |
| Obsidian | obsidian.md |
| Claude | claude.ai/download |
| ChatGPT | App Store |
| GitHub Desktop | desktop.github.com |
| Dropbox | dropbox.com |
| Microsoft Teams | Web |
| Linear | linear.app |
| Zoom | zoom.us |

### Tier 2 — Creative Production

| App | Source |
|---|---|
| Adobe Creative Cloud (After Effects, Premiere Pro, Photoshop, Bridge, Lightroom, Media Encoder) | creativecloud.adobe.com |
| DaVinci Resolve | blackmagicdesign.com |
| Final Cut Pro | App Store |
| Motion | App Store |
| Descript | descript.com |
| Screen Studio | screen.studio |
| HandBrake | handbrake.fr |
| Topaz Photo AI | topazlabs.com |
| Topaz Video AI | topazlabs.com |
| Audacity | audacityteam.org |

### Tier 3 — Utilities & Other

| App | Source |
|---|---|
| VLC | videolan.org |
| Ollama | ollama.com |
| WhatsApp | App Store |
| Discord | discord.com |
| Spotify | spotify.com |
| Loom | loom.com |
| Notion | notion.so |
| Wispr Flow | wispr.ai |
| Frame.io | frame.io |
| Elgato Camera Hub + Studio | elgato.com |
| DisplayLink Manager | displaylink.com |
| Pixelmator Pro | App Store |
| iZotope RX Pro Audio Editor | izotope.com |
| Keynote / Pages / Numbers | App Store (free) |

### Tier 4 — Situational (install when needed)

Codex, Comet, Intent by Augment, Basecamp, Beeper, Evernote, Insta360, JW Library, MacWhisper, Riverside.fm, SmugMug, Sublime, 4K Video Downloader, Battle.net, Epic Games, Steam, Shot Designer, Final Draft.

---

## Phase 13 — Verification Checklist

Run these on the new Mac to verify everything works:

```bash
# Homebrew
brew --version

# Runtimes
node --version    # expect v22.13.1
npm --version     # expect 11.x
python3 --version # expect 3.14.x
bun --version     # expect 1.3.x
deno --version
uv --version

# Git
git config --global user.name   # expect "Will Proctor"
git config --global user.email  # expect "c-will.proctor@growthx.ai"

# GitHub CLI
gh auth status    # expect logged in as williamproctor

# SSH
ssh -T git@github.com  # expect "Hi williamproctor!"

# Claude Code
claude --version

# Global tools
ffmpeg -version | head -1
yt-dlp --version
wrangler --version
tmux -V
rclone version | head -1
runpodctl version

# Repos
ls ~/Documents/GitHub/
# Expect: Will-s-Workspace, growthx-system, content-vault, CorridorKey,
#         growthx-landing-prototype, gemini-trial-survey, gtm-brain,
#         strategy-os, products, + all growthxai repos

# Fonts
ls ~/Library/Fonts/ | wc -l  # expect ~180+ files

# Cursor MCP
cat ~/.cursor/mcp.json  # verify ahrefs + ordinal configured
```

---

## Secrets to Transfer Securely

These cannot be scripted — transfer via 1Password, AirDrop, or manual entry:

| Secret | Where It Goes |
|---|---|
| Ordinal API token | `~/.cursor/mcp.json` |
| XAgent (Twitter) API key | `Will-s-Workspace/.cursor/mcp.json` |
| Obsidian REST API key | `Will-s-Workspace/.cursor/mcp.json` |
| Ahrefs OAuth (handled by mcp-remote) | Browser auth flow |
| Figma OAuth | Browser auth flow |
| Canonry LLM API keys | `canonry init` interactive setup |
| ElevenLabs API key | environment variable or project config |
| Google Gemini API key | pip package / project config |
| Cloudflare (Wrangler) auth | `wrangler login` |
| RunPod API key | `runpodctl config` |

---

## Quick-Start Script

For convenience, here's a single script that handles Phases 2-6 (everything that can be automated):

```bash
#!/bin/bash
set -e

echo "=== Phase 2: Homebrew ==="
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

cat > /tmp/Brewfile << 'EOF'
tap "runpod/runpodctl"
brew "ffmpeg"
brew "gh"
brew "git"
brew "git-lfs"
brew "rclone"
brew "tmux"
brew "yt-dlp"
brew "deno"
brew "runpod/runpodctl/runpodctl"
EOF
brew bundle --file=/tmp/Brewfile
git lfs install

echo "=== Phase 3: Node.js ==="
mkdir -p ~/.local
curl -fsSL https://nodejs.org/dist/v22.13.1/node-v22.13.1-darwin-arm64.tar.xz | tar -xJ -C ~/.local
mv ~/.local/node-v22.13.1-darwin-arm64 ~/.local/node
export PATH="$HOME/.local/node/bin:$PATH"

echo "=== Phase 3: uv ==="
curl -fsSL https://astral.sh/uv/install.sh | sh

echo "=== Phase 3: Bun ==="
curl -fsSL https://bun.sh/install | bash
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

echo "=== Phase 4: npm globals ==="
npm install -g @anthropic-ai/claude-code @augmentcode/auggie @ainyc/canonry obsidian-local-rest-api-mcp wrangler

echo "=== Phase 4: pip globals ==="
pip3 install google-genai google-generativeai google-api-python-client pillow httpx websockets pydantic requests tqdm

echo "=== Phase 5: Shell config ==="
cat > ~/.zprofile << 'ZPROFILE'
export PATH="$HOME/.local/node/bin:$PATH"
eval "$(/opt/homebrew/bin/brew shellenv)"
ZPROFILE

cat > ~/.zshrc << 'ZSHRC'
alias peon="bash ~/.claude/hooks/peon-ping/peon.sh"
[ -f ~/.claude/hooks/peon-ping/completions.bash ] && source ~/.claude/hooks/peon-ping/completions.bash
[ -s "$HOME/.bun/_bun" ] && source "$HOME/.bun/_bun"
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
. "$HOME/.local/bin/env"
ZSHRC

echo "=== Phase 6: Git config ==="
git config --global user.name "Will Proctor"
git config --global user.email "c-will.proctor@growthx.ai"
git config --global filter.lfs.clean "git-lfs clean -- %f"
git config --global filter.lfs.smudge "git-lfs smudge -- %f"
git config --global filter.lfs.process "git-lfs filter-process"
git config --global filter.lfs.required true
git config --global credential.https://github.com.helper ""
git config --global credential.https://github.com.helper "!/opt/homebrew/bin/gh auth git-credential"
git config --global credential.https://gist.github.com.helper ""
git config --global credential.https://gist.github.com.helper "!/opt/homebrew/bin/gh auth git-credential"

echo "=== Phase 6: SSH Key ==="
ssh-keygen -t ed25519 -C "c-will.proctor@growthx.ai" -f ~/.ssh/id_ed25519 -N ""
echo ""
echo ">>> ADD THIS PUBLIC KEY TO https://github.com/settings/keys <<<"
cat ~/.ssh/id_ed25519.pub
echo ""

echo "=== Phase 6: GitHub CLI ==="
echo "Run: gh auth login"
echo ""

echo "=== Phase 1: macOS defaults ==="
defaults write com.apple.dock autohide -bool true
defaults write com.apple.finder ShowPathbar -bool true
killall Dock
killall Finder

echo ""
echo "✓ Automated setup complete!"
echo ""
echo "MANUAL STEPS REMAINING:"
echo "  1. Add SSH public key to GitHub (printed above)"
echo "  2. Run: gh auth login"
echo "  3. Clone repos (see Phase 7 in NEW-MAC-SETUP.md)"
echo "  4. Transfer fonts from old Mac (AirDrop ~/Library/Fonts/)"
echo "  5. Transfer Cursor skills (AirDrop ~/.cursor/skills/)"
echo "  6. Transfer peon-ping (AirDrop ~/.claude/hooks/)"
echo "  7. Configure MCP secrets (see Phase 9)"
echo "  8. Install macOS apps (see Phase 12)"
```

---

## Notes

- **Username assumption:** This guide assumes the new Mac username is the same (`wil`). If different, update paths in MCP configs, Claude settings, and shell configs.
- **Apple Silicon:** All download URLs assume ARM64/Apple Silicon (M-series). If the new Mac is Intel, substitute `darwin-x64` for Node and check Homebrew path (`/usr/local` instead of `/opt/homebrew`).
- **Content Vault:** The `content-vault` repo is private and contains ~100+ markdown notes. MP4 clips (2.4 GB) are gitignored — transfer separately via AirDrop or external drive if needed.
- **Workspace nested repos:** `docs/growthx/` inside Will-s-Workspace is a separate git repo (`williamproctor/growthx-system`). The parent repo gitignores it. Clone it separately into position after cloning the workspace.
