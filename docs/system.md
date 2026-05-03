# System

Package file: `packages/system.yaml`

---

## `system-update`

Apt update + upgrade.

### Description
`system-update` runs `apt update` and `apt upgrade` to refresh package lists and install available updates. It is a foundational dependency for many other packages.

### Usage
```bash
# Run via setup.py (not a standalone binary)
python3 setup.py --select system-update

# Or manually:
sudo apt update && sudo apt upgrade -y
```

---

## `build-essential`

Build tools (gcc, make, libc-dev).

### Description
`build-essential` is a metapackage that installs compilers and libraries required to build software from source, including `gcc`, `g++`, `make`, and standard C library headers.

### Usage
```bash
# Verify compiler installation
which gcc && gcc --version

# Compile a C program
gcc -o hello hello.c

# Run make
make -j$(nproc)
```

---

## `curl-wget`

curl & wget.

### Description
`curl` and `wget` are command-line tools for transferring data with URLs. `curl` supports a vast range of protocols and APIs, while `wget` excels at recursive downloads and resuming interrupted transfers.

### Usage
```bash
# Download a file
curl -O https://example.com/file.zip
wget https://example.com/file.zip

# Download with headers and follow redirects
curl -L -H "Authorization: Bearer TOKEN" https://api.example.com/data

# Resume broken download
wget -c https://example.com/large.iso

# POST JSON data
curl -X POST -H "Content-Type: application/json" -d '{"key":"val"}' https://api.example.com/webhook

# Mirror a website
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com
```

---

## `zsh`

Z shell.

### Description
`zsh` is an interactive shell with powerful scripting features, advanced globbing, programmable completion, and plugin support. It serves as the foundation for frameworks like Oh My Zsh.

### Usage
```bash
# Start zsh
zsh

# Set as default shell
chsh -s $(which zsh)

# Run a zsh script
zsh script.zsh

# Use advanced globbing
ls **/*.py

# Edit config
vim ~/.zshrc
```

---

## `oh-my-zsh`

Zsh framework.

### Description
`oh-my-zsh` is an open-source framework for managing Zsh configuration. It comes bundled with hundreds of plugins, helpers, themes, and aliases.

### Usage
```bash
# Start a new zsh session to load oh-my-zsh
zsh

# Edit config
vim ~/.zshrc

# Enable a plugin
# In ~/.zshrc: plugins=(git docker kubectl)

# Change theme
# In ~/.zshrc: ZSH_THEME="robbyrussell"

# Reload
source ~/.zshrc
```

---

## `starship`

Minimal blazing-fast customizable prompt.

### Description
`starship` is a cross-shell prompt written in Rust. It shows context-aware info (git branch, runtime versions, error codes) with minimal latency and high customizability.

### Usage
```bash
# Enable in zsh (~/.zshrc)
eval "$(starship init zsh)"

# Enable in bash (~/.bashrc)
eval "$(starship init bash)"

# Edit config
vim ~/.config/starship.toml

# Preview prompt config
starship explain
```

---

## `zoxide`

Smarter cd that learns your habits.

### Description
`zoxide` is a replacement for `cd` that remembers the directories you visit most often. It uses fuzzy matching and a scoring algorithm to jump to directories with partial names.

### Usage
```bash
# Replace cd (add to ~/.zshrc or ~/.bashrc)
eval "$(zoxide init zsh)"

# Jump to a frequently visited directory
z proj

# Interactive selection with fzf
zi

# Add a directory to the database explicitly
zoxide add /path/to/dir
```

---

## `atuin`

Magical shell history with encrypted sync.

### Description
`atuin` replaces your shell history with an SQLite database, enabling fuzzy search, stats, and end-to-end encrypted sync across devices.

### Usage
```bash
# Enable in zsh
eval "$(atuin init zsh)"

# Search history interactively (Ctrl+R replacement)
# Press Ctrl+R in your shell after enabling

# Search via CLI
atuin search --filter-mode directory -- "docker"

# View stats
atuin stats

# Sync history
atuin sync
```

---

## `gnupg`

GPG encryption & signing.

### Description
`gpg` is the GNU Privacy Guard for encrypting and signing data and communications. It implements the OpenPGP standard and is commonly used for signing git commits, encrypting files, and managing keypairs.

### Usage
```bash
# Generate a new key pair
gpg --full-generate-key

# List keys
gpg --list-keys

# Encrypt a file
gpg --encrypt --recipient alice@example.com secret.txt

# Decrypt a file
gpg --decrypt secret.txt.gpg > secret.txt

# Sign a file
gpg --detach-sign document.pdf

# Configure git to sign commits
git config --global user.signingkey KEYID
git commit -S -m "Signed commit"
```

---

## `mosh`

Mobile (roaming) SSH.

### Description
`mosh` is a remote terminal application that supports intermittent connectivity and roaming. Unlike SSH, it survives IP changes, laptop sleep, and poor networks.

### Usage
```bash
# Connect to a remote server
mosh user@server.example.com

# With a specific SSH port
mosh --ssh="ssh -p 2222" user@server

# Run a command instead of a shell
mosh user@server -- tmux attach
```

---

## `htop`

Process viewer.

### Description
`htop` is an interactive process viewer for Unix systems. It provides a colorized, scrollable list of processes, tree view, and the ability to kill or renice processes directly.

### Usage
```bash
# Start htop
htop

# Show processes for a specific user
htop -u username

# Filter by process name
htop -p $(pgrep -d',' python3)
```

---

## `btop`

Fancy resource monitor.

### Description
`btop` is a beautiful system resource monitor with CPU, memory, disk, and network stats. It features customizable themes, responsive layouts, and detailed per-core graphs.

### Usage
```bash
# Start btop
btop

# Start with a specific theme
btop --theme dracula

# Show help inside the app
# Press 'h' while running
```

---

## `ttyplot`

Terminal plotting.

### Description
`ttyplot` is a real-time plotting tool for the terminal. It reads numerical data from stdin and draws ASCII/Unicode graphs, useful for monitoring log data, metrics, or pipes.

### Usage
```bash
# Plot ping latency in real time
ping 1.1.1.1 | sed -u 's/^.*time=//; s/ ms//' | ttyplot -t "ping"

# Plot CPU usage
vmstat 1 | awk 'NR>2 {print 100-$15}' | ttyplot -t "CPU %"

# Plot with custom unit
seq 1 100 | ttyplot -u "requests"
```

---

## `asciinema`

Terminal recording.

### Description
`asciinema` records terminal sessions as lightweight, text-based cast files. Unlike video recordings, the output is searchable, copyable, and embeddable on the web.

### Usage
```bash
# Start recording
asciinema rec demo.cast

# Play a recording
asciinema play demo.cast

# Upload to asciinema.org
asciinema upload demo.cast

# Convert to GIF (requires agg or svg-term)
agg demo.cast demo.gif
```

---

## `glances`

System monitor.

### Description
`glances` is an advanced cross-platform system monitoring tool. It displays CPU, memory, disk, network, process, and sensor data in a lightweight dashboard.

### Usage
```bash
# Start interactive TUI
glances

# Web UI mode
glances -w

# Run as a client connecting to a glances server
glances -c 192.168.1.10

# Export stats to CSV
glances --export csv --export-csv-file stats.csv
```

---

## `imgcat`

Terminal image display.

### Description
`imgcat` displays images directly inside supported terminal emulators (iTerm2, kitty, WezTerm, etc.) using inline image protocols.

### Usage
```bash
# Display an image in the terminal
imgcat photo.png

# Pipe from curl
curl -s https://example.com/img.jpg | imgcat

# Multiple images
imgcat *.png
```

---

## `bashorg-motd`

bash.org quote MOTD.

### Description
`bashorg-motd` prints a random funny quote from bash.org as your Message of the Day when you open a new shell.

### Usage
```bash
# Run manually
bashorg-motd

# Add to ~/.bashrc or ~/.zshrc to show on login
bashorg-motd
```
