# Dev Tools

Package file: `packages/dev-tools.yaml`

---

## `git`

Git version control.

### Description
`git` is the distributed version control system used by most software projects. It tracks changes, manages branches, enables collaboration, and supports advanced workflows like rebase, cherry-pick, and bisect.

### Usage
```bash
# Clone a repository
git clone https://github.com/user/repo.git

# Stage, commit, and push
git add .
git commit -m "feat: add new widget"
git push origin main

# Create and switch to a branch
git checkout -b feature-branch

# View history
git log --oneline --graph --decorate

# Interactive rebase last 3 commits
git rebase -i HEAD~3
```

---

## `gh`

GitHub CLI.

### Description
`gh` is the official GitHub command-line tool. It lets you create PRs, review code, manage issues, clone repos, and interact with GitHub Actions directly from the terminal.

### Usage
```bash
# Authenticate with GitHub
gh auth login

# Create a pull request
gh pr create --title "Fix crash" --body "Closes #42"

# List open PRs in current repo
gh pr list

# View workflow runs
gh run list

# Clone repo interactively
gh repo clone user/repo

# Create an issue
gh issue create --title "Bug report" --body "..."
```

---

## `neovim`

Text editor.

### Description
`neovim` (`nvim`) is a hyperextensible Vim-based text editor with built-in Lua scripting, LSP support, treesitter, and a modern async architecture. It is the preferred terminal editor for many developers.

### Usage
```bash
# Open a file
nvim file.txt

# Open in diff mode
nvim -d file1.txt file2.txt

# Edit multiple files
nvim file1.py file2.py

# Start with a clean config
nvim --clean

# Run a command and quit
nvim +"lua print('hello')" -c "q"
```

---

## `tmux`

Terminal multiplexer.

### Description
`tmux` allows multiple terminal sessions inside a single window. It supports splitting windows into panes, creating persistent sessions that survive SSH disconnects, and scripting workflows.

### Usage
```bash
# Start a new session
tmux new -s mysession

# Attach to an existing session
tmux attach -t mysession

# Split window vertically
tmux split-window -h

# Split window horizontally
tmux split-window -v

# List sessions
tmux ls

# Detach (keep running in background)
Ctrl+b d
```

---

## `chezmoi`

Dotfile manager.

### Description
`chezmoi` is a declarative dotfile manager that tracks, applies, and syncs configuration files across machines using git. It handles secrets via password managers and supports templates.

### Usage
```bash
# Initialize chezmoi with your dotfiles repo
chezmoi init https://github.com/user/dotfiles.git

# Apply dotfiles to the system
chezmoi apply

# Edit a managed file
chezmoi edit ~/.bashrc

# Add a new file to tracking
chezmoi add ~/.config/alacritty/alacritty.yml

# Diff current system against dotfiles
chezmoi diff

# Update from upstream
chezmoi update
```

---

## `delta`

Syntax-aware diff viewer for git.

### Description
`delta` is a syntax-highlighting pager for git and diff output. It replaces `git diff` and `git show` with beautifully formatted, side-by-side or unified views.

### Usage
```bash
# Configure git to use delta automatically
git config --global core.pager delta
git config --global interactive.diffFilter 'delta --color-only'

# View diff with syntax highlighting
git diff | delta

# Side-by-side mode
delta --side-by-side file1 file2
```

---

## `diff-so-fancy`

Pretty git diffs.

### Description
`diff-so-fancy` is a CLI tool that makes diffs human-readable by enhancing chunk headers, highlighting changes, and stripping unnecessary metadata.

### Usage
```bash
# Pipe any diff through it
git diff | diff-so-fancy

# Set as git pager
git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"

# Enable in interactive mode
git config --global interactive.diffFilter "diff-so-fancy --patch"
```

---

## `ducker-tui`

Docker TUI (lazydocker).

### Description
`lazydocker` (installed as `ducker-tui`) is a terminal UI for managing Docker containers, images, volumes, and logs interactively. It provides keyboard-driven workflows for common Docker operations.

### Usage
```bash
# Launch the TUI
lazydocker

# View containers, images, volumes, and logs in one screen
# Use arrow keys to navigate, Enter to inspect, 'd' to remove, 'r' to restart
```

---

## `zed-server`

Zed editor remote server.

### Description
The Zed editor remote server (`zed`) enables collaboration and remote development with the Zed code editor. It pairs with the Zed desktop app to provide low-latency editing over SSH.

### Usage
```bash
# Install and start the remote server
zed

# From your local Zed client, open a remote folder via SSH
# The server handles LSP, file watching, and terminal integration remotely
```

---

## `gopass`

Team password manager.

### Description
`gopass` is a password manager for teams built on top of `gpg` and `git`. It stores encrypted secrets in a shared git repository and supports templates, mounts, and multiple stores.

### Usage
```bash
# Initialize a password store
gopass init

# Insert a new password
gopass insert mysite.com/admin

# Retrieve a password
gopass show mysite.com/admin

# List all secrets
gopass ls

# Clone a team store
gopass clone https://github.com/org/pass-store.git
```

---

## `pcopy`

Encrypted clipboard sync.

### Description
`pcopy` is a tool for securely copying and pasting text across machines using end-to-end encryption. It replaces Slack/email for sharing snippets in a terminal-first workflow.

### Usage
```bash
# Start the pcopy server (on one machine)
pcopy serve

# Copy text to clipboard remotely
echo 'secret-token' | pcopy copy

# Paste from remote clipboard
pcopy paste
```

---

## `browsr`

CLI file browser.

### Description
`browsr` is a terminal-based file browser and viewer with support for images, data tables, and code preview. It integrates with rich TUI libraries for a polished file navigation experience.

### Usage
```bash
# Open directory browser
browsr .

# Browse with image previews
browsr ~/Pictures

# Open specific file with viewer
browsr data.csv
```

---

## `crawley`

Fast web crawler.

### Description
`crawley` is a high-performance CLI web crawler written in Go for extracting links, assets, and metadata from websites.

### Usage
```bash
# Crawl a site and list all URLs found
crawley https://example.com

# Limit crawl depth
crawley -d 2 https://example.com

# Output to file
crawley https://example.com > sitemap.txt

# Follow redirects and print all discovered links
crawley -r https://example.com
```
