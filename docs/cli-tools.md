# CLI Tools

Package file: `packages/cli-tools.yaml`

---

## `bat`

`cat` with syntax highlighting and git integration.

### Description
`bat` is a drop-in replacement for `cat` that adds syntax highlighting, line numbers, git decorations, and automatic paging. It supports a wide range of formats and themes.

### Usage
```bash
# View a file with syntax highlighting
bat main.py

# Show line numbers, git changes, and no paging
bat -p --plain file.txt

# Use a specific theme
bat --theme=TwoDark config.yaml

# List available themes
bat --list-themes
```

---

## `jq`

JSON processor.

### Description
`jq` is a lightweight command-line JSON processor. It allows slicing, filtering, mapping, and transforming structured data with a powerful query language.

### Usage
```bash
# Pretty-print JSON
cat data.json | jq .

# Extract a field
jq '.name' data.json

# Filter an array
jq '.users[] | select(.age > 18)' data.json

# Transform and output as CSV
jq -r '.users[] | [.name, .email] | @csv' data.json

# Inline edit a JSON file
jq '.version = "2.0.0"' package.json > tmp.json && mv tmp.json package.json
```

---

## `jaq`

Fast near drop-in jq clone.

### Description
`jaq` is a Rust-based reimplementation of `jq` designed for dramatically faster performance on large JSON payloads while maintaining syntax compatibility.

### Usage
```bash
# Same syntax as jq — run queries faster on big files
jaq '.items[] | select(.price < 10)' large.json

# Benchmark against jq
jaq '.[] | .id' 100mb-array.json
```

---

## `fzf`

Fuzzy finder.

### Description
`fzf` is a general-purpose command-line fuzzy finder. It reads a list from stdin and presents an interactive interface for filtering files, history, git branches, processes, and more.

### Usage
```bash
# Search files interactively
fzf

# Search files under current directory
find . -type f | fzf

# Search shell history
history | fzf

# Open selected file in editor
vim $(fzf)

# Git branch switcher
git branch | fzf | xargs git checkout

# Interactive process kill
ps aux | fzf | awk '{print $2}' | xargs kill -9
```

---

## `ripgrep`

Fast recursive grep.

### Description
`ripgrep` (`rg`) recursively searches directories for regex patterns while respecting `.gitignore` and hidden file conventions by default. It is significantly faster than `grep -r`.

### Usage
```bash
# Search a regex in current directory
rg 'TODO'

# Search in a specific file type
rg 'class App' --type js

# Show line numbers with context
rg -C 3 'def main'

# List files with matches
rg -l 'import React'

# Search hidden files too
rg -uu 'API_KEY'

# Replace grep in pipelines
rg 'error' /var/log | head -20
```

---

## `fd-find`

Fast find.

### Description
`fd` (`fdfind` on Debian) is a simple, fast, and user-friendly alternative to `find`. It uses sensible defaults: respects `.gitignore`, excludes hidden files, and uses regex by default.

### Usage
```bash
# Find files matching pattern
fd 'config'

# Find by extension
fd -e py

# Find and execute a command
fd -e log -x rm

# Find hidden files
fd -H 'secret'

# Find directories only
fd -t d 'venv'
```

---

## `exa`

Modern maintained ls replacement.

### Description
`eza` (formerly `exa`) is a modern replacement for `ls` with support for colors, git integration, tree views, and better defaults.

### Usage
```bash
# Default colorful listing
eza

# Long format with git info
eza -la --git

# Tree view
eza --tree --level=2

# Sort by modified time
eza -la --sort=modified

# Show file sizes in human-readable format
eza -lh
```

---

## `dust`

Visual intuitive disk usage tree.

### Description
`dust` is a more intuitive version of `du`. It shows disk usage as an interactive tree, skipping empty directories and sorting by size.

### Usage
```bash
# Show disk usage tree for current directory
dust

# Limit depth
dust -d 2

# Show only directories (no files)
dust -D

# Show specific path
dust /var/log

# Show bar charts
dust -b
```

---

## `gdu`

Go disk usage (fast ncdu).

### Description
`gdu` is a fast disk usage analyzer written in Go, similar to `ncdu`. It provides an interactive TUI for navigating disk usage.

### Usage
```bash
# Start interactive disk analyzer
gdu

# Analyze a specific path
gdu /home

# Non-interactive output
gdu -n /var

# Show largest files first
gdu -l
```

---

## `yt-dlp`

Video downloader.

### Description
`yt-dlp` is a feature-rich command-line tool for downloading videos and audio from YouTube and thousands of other sites. It is an actively maintained fork of `youtube-dl`.

### Usage
```bash
# Download a video
yt-dlp 'https://www.youtube.com/watch?v=...'

# Download audio only
yt-dlp -x --audio-format mp3 'URL'

# Download playlist
yt-dlp -o '%(playlist_index)s - %(title)s.%(ext)s' 'PLAYLIST_URL'

# Show available formats
yt-dlp -F 'URL'

# Download best quality + subtitles
yt-dlp --embed-subs --all-subs 'URL'
```
