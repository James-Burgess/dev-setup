# Productivity

Package file: `packages/productivity.yaml`

---

## `obsidian`

Knowledge base.

### Description
`obsidian` is a powerful knowledge management app built on a local folder of Markdown files. It supports backlinks, graph views, plugins, and sync options.

### Usage
```bash
# Launch Obsidian
obsidian

# Open a specific vault
obsidian --vault-dir ~/Notes
```

---

## `aerc`

Modern terminal email client.

### Description
`aerc` is an efficient, extensible email client for the terminal. It supports multiple accounts, Maildir/Notmuch/IMAP, Vim-style keybindings, and filtering with pipes.

### Usage
```bash
# Start aerc
aerc

# Read the tutorial
# Press '?' inside aerc for help

# Compose a new message
# Press 'C' in the message list
```

---

## `borg`

Borg deduplicating backup.

### Description
`borg` is a deduplicating archiver with compression and encryption. It creates space-efficient backups of files and supports pruning policies and remote repositories.

### Usage
```bash
# Initialize a backup repository
borg init --encryption=repokey /path/to/backup

# Create a backup archive
borg create /path/to/backup::mypc-$(date +%Y-%m-%d) ~/Documents ~/Pictures

# List archives
borg list /path/to/backup

# Extract an archive
borg extract /path/to/backup::mypc-2024-01-01

# Prune old backups
borg prune --keep-daily=7 --keep-weekly=4 /path/to/backup
```

---

## `fnt`

Font manager.

### Description
`font-manager` is a GUI and CLI tool for browsing, installing, and managing fonts on Linux systems. It supports collections, Google Fonts, and system/user-level installation.

### Usage
```bash
# Launch the GUI
font-manager

# Install a font file
font-manager --install FontFile.ttf

# View installed fonts
font-manager --list
```
