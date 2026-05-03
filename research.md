# Terminal Environment Research Report
## For Building a Fresh Dotfiles Setup (Neovim + Tmux + Zsh + OpenCode)

**Date:** 2026-04-30
**Scope:** Ubuntu dev box terminal environment
**Goal:** A cohesive, fast, minimal, and fully scriptable terminal configuration.

---

## 1. Executive Summary / Philosophy

Modern terminal dotfiles in 2026 favor **composability over monoliths**:
- **Zsh**: Use Zsh itself with curated plugins rather than heavy frameworks like Oh My Zsh if startup speed and predictability matter. Starship is the de-facto modern prompt.
- **Neovim**: Kickstart.nvim is the single best reference for a "from-scratch" Lua-based config using `lazy.nvim`. Native LSP has fully replaced coc.nvim.
- **Tmux**: TPM + tmux-sensible + a clean prefix/mouse/vi-mode config is the baseline.
- **CLI Core**: Replace legacy POSIX tools with modern Rust-based equivalents (`fd`, `bat`, `eza`, `ripgrep`, `fzf`).
- **Integration**: `fzf` is the universal glue connecting Zsh, Tmux, and Neovim.
- **OpenCode / Agent Context**: Configs must be **non-interactive**, **fast-starting**, and **deterministic**. Avoid anything that prompts the user on first run.

---

## 2. Zsh Configuration

### 2.1 Core Shell Setup
- **Shell**: Zsh 5.9+ (Ubuntu 24.04 default is fine).
- **Framework Choice**: **Avoid Oh My Zsh** for a clean agent/dotfiles setup. It adds bloat, magic aliases, and slow startup. Instead, use **plain Zsh** + manually sourced high-quality plugins.
- **Prompt**: **Starship** (57k stars) is the modern standard. It is cross-shell, written in Rust, and starts instantly. Replaces Powerlevel10k for most users.
- **Plugins (Must-Have)**:
  - `zsh-autosuggestions` (35.4k stars) — Fish-like grayed-out history suggestions.
  - `zsh-syntax-highlighting` (22.6k stars) — Validates commands as you type; must be sourced **last**.
- **Completion**: Use `zsh-completions` + ensure `compinit` is called once with a cache dump to keep startup fast.

### 2.2 Zsh Key Bindings & Options
```zsh
# Essential options
setopt AUTOCD              # cd by typing directory name
setopt AUTO_PUSHD          # push directories to stack
setopt PUSHD_IGNORE_DUPS   # no duplicate dirs in stack
setopt EXTENDED_GLOB       # powerful globbing
setopt NO_BEEP             # silence
setopt HIST_IGNORE_DUPS    # no duplicate history
setopt HIST_IGNORE_SPACE   # don't save if leading space
setopt SHARE_HISTORY       # share history across sessions

# vi mode
bindkey -v                 # use vim keybindings
export KEYTIMEOUT=1        # fast escape
```

### 2.3 Prompt Configuration (Starship)
- Install: `curl -sS https://starship.rs/install.sh | sh`
- Add to `~/.zshrc`: `eval "$(starship init zsh)"`
- Config lives in `~/.config/starship.toml`.
- Recommended minimal config for a dev box:
  - Show directory, git branch/status, error status, and execution time.
  - Disable slow modules (e.g., `nodejs`, `python`) on large directories using `detect_folders` or `scan_timeout`.
- **Font Requirement**: MesloLGS NF or any Nerd Font v3.0+.

### 2.4 Useful Aliases (Using Modern Tools)
```zsh
alias cat='bat --paging=never'
alias ls='eza --icons --group-directories-first'
alias ll='eza -l --icons --git'
alias la='eza -a --icons'
alias lt='eza --tree --icons'
alias find='fd'
alias grep='rg'
```

---

## 3. Neovim Configuration

### 3.1 Installation & Version
- **Target**: Neovim 0.10+ (stable). 0.11+ if available via `ppa:neovim-ppa/unstable` or AppImage.
- **Config Path**: `~/.config/nvim/init.lua`
- **Prerequisites**: `git`, `make`, `gcc`, `ripgrep`, `fd`, `unzip`, Nerd Font.

### 3.2 Plugin Manager
- **Choice**: `lazy.nvim` (20.8k stars) — the uncontested standard. Supports lockfiles (`lazy-lock.json`), async, partial clones, and automatic lazy-loading.
- **Migration**: `packer.nvim` is deprecated. `vim-plug` is legacy. Only `lazy.nvim` should be used for new configs.

### 3.3 Starter Template
- **kickstart.nvim** (30.4k stars) is the single best teaching reference. It is a single `init.lua` (~400 lines) that sets up:
  - `lazy.nvim` bootstrap
  - `nvim-treesitter` with auto-install
  - LSP via `nvim-lspconfig` + Mason
  - `telescope.nvim` (fuzzy finder)
  - `cmp` (completion engine)
  - `lualine` (statusline)
  - `which-key` (keybinding hints)
- **Strategy**: Fork kickstart.nvim, then extract into a modular structure (`lua/plugins/*.lua`, `lua/core/*.lua`) as you grow.

### 3.4 Essential Plugins for a Modern IDE-like Setup
| Plugin | Purpose | Notes |
|--------|---------|-------|
| `lazy.nvim` | Plugin management | Bootstrap in `init.lua` |
| `nvim-treesitter` | Syntax highlighting, folding, indentation | Archive notice: use latest nvim 0.12+ compatible version |
| `nvim-lspconfig` | Native LSP client configuration | Pair with `mason.nvim` + `mason-lspconfig.nvim` |
| `nvim-cmp` | Autocompletion | Sources: LSP, buffer, path, cmdline |
| `telescope.nvim` | Fuzzy finder over files, grep, buffers, help | Requires `ripgrep` and `fd` |
| `nvim-tree.lua` | File explorer sidebar | Disable netrw first |
| `bufferline.nvim` | Tab-like buffer line | Requires `termguicolors` |
| `lualine.nvim` | Status line | Themed automatically |
| `gitsigns.nvim` | Git gutter / hunk navigation | Essential |
| `which-key.nvim` | Keybinding discovery | Non-intrusive |
| `catppuccin/nvim` | Colorscheme | Very popular, 4 flavors |

### 3.5 LSP & Language Support
- Use **Mason** (`williamboman/mason.nvim`) as a registry to install language servers (`pyright`, `tsserver`/`vtsls`, `gopls`, `rust_analyzer`, `lua_ls`).
- Map manual LSP setup to `lspconfig`.
- Formatter: `conform.nvim` (uses `black`, `prettierd`, `shfmt` binaries under the hood).
- Linter: `nvim-lint`.

### 3.6 Key Mappings (Leader = Space)
- `<leader>ff` — Find files (Telescope)
- `<leader>fg` — Live grep (Telescope)
- `<leader>fb` — Buffers (Telescope)
- `<leader>e`  — Toggle file explorer (nvim-tree)
- `<leader>rn` — Rename (LSP)
- `gd` / `gr`  — Go to definition / references (LSP)
- `K`          — Hover documentation (LSP)
- `<C-h/j/k/l>` — Navigate Tmux panes (see Integration section)

---

## 4. Tmux Configuration

### 4.1 TPM (Tmux Plugin Manager)
- Install: `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
- Load at bottom of `~/.tmux.conf`: `run '~/.tmux/plugins/tpm/tpm'`
- Install plugins with `prefix + I`.

### 4.2 Baseline Plugins
| Plugin | Purpose |
|--------|---------|
| `tmux-plugins/tmux-sensible` | Sane defaults everyone agrees on (history-limit, escape-time, etc.) |
| `tmux-plugins/tmux-resurrect` | Save/restore sessions across restarts |
| `tmux-plugins/tmux-continuum` | Auto-save + auto-restore (pairs with resurrect) |
| `catppuccin/tmux` | Beautiful pastel theme |

### 4.3 Essential `.tmux.conf` Settings
```tmux
# Prefix
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Vi mode
setw -g mode-keys vi

# Mouse
set -g mouse on

# Sensible defaults (if not using tmux-sensible)
set -s escape-time 0
set -g history-limit 50000
set -g focus-events on
setw -g aggressive-resize on

# Terminal colors
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"

# Easy reload
bind r source-file ~/.tmux.conf \; display "Config reloaded!"

# Pane navigation (vim-style)
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Window splitting
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"
```

### 4.4 Tmux + Neovim Integration (Seamless Navigation)
- Use **christoomey/vim-tmux-navigator** plugin for Neovim.
- Map the same `<C-h/j/k/l>` keys in Tmux to send the appropriate commands when Neovim is active, otherwise switch Tmux panes.

---

## 5. Modern CLI Tooling (The "Core Utils" Rewrite)

All of these should be installed via the dev box setup script (`apt`, `cargo install`, or `mise`).

| Tool | Replaces | Why |
|------|----------|-----|
| `fzf` | nothing — it's new fuzzy-finding | Universal fuzzy filter; integrates with Zsh, Tmux, Vim/Neovim, git |
| `fd` (`fdfind` on Debian) | `find` | Intuitive regex-by-default; respects `.gitignore`; fast |
| `bat` (`batcat` on Debian) | `cat` | Syntax highlighting, git diff markers, paging |
| `eza` | `ls` / `exa` | Better colors, icons, git integration, tree view |
| `ripgrep` (`rg`) | `grep` | Fast, respects `.gitignore`, recursively searches by default |
| `lazygit` | raw `git` CLI | Amazing TUI for git operations |

### 5.1 fzf Integration Points
- **Zsh**: `eval "$(fzf --zsh)"` in `.zshrc` (fzf 0.48+). Provides `Ctrl-T` (file), `Ctrl-R` (history), `Alt-C` (cd).
- **Neovim**: `telescope-fzf-native.nvim` for Telescope; or `fzf-lua` as a native Lua alternative.
- **Tmux**: `fzf-tmux` script for popup windows (tmux 3.3+).
- **Environment Variables**:
  ```zsh
  export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'
  export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
  export FZF_ALT_C_COMMAND='fd --type d --hidden --follow --exclude .git'
  export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'
  ```

---

## 6. OpenCode / Agent-Specific Considerations

When building dots that may be bootstrapped by an AI agent or CI/CD pipeline:

1. **No Interactive Prompts**
   - Starship: run `starship init` non-interactively.
   - Powerlevel10k: avoid entirely because the wizard requires interaction. Use Starship instead.
   - Neovim: Ensure `:MasonInstall`, `:TSInstall`, and `lazy.nvim` run headless (use `nvim --headless` with appropriate ex-commands or Lua scripts).

2. **Deterministic Lockfiles**
   - Commit `lazy-lock.json` for Neovim plugins.
   - Commit `starship.toml` (explicit config, not generated).
   - Pin TPM plugin versions with `#v2.3.0` syntax.

3. **Fast Startup is Critical**
   - Profile Zsh startup with `time zsh -i -c exit`.
   - Keep `~/.zshrc` under 100ms load time.
   - Use `zsh-defer` or lazy-loading for heavy plugins if needed.
   - Neovim startup should be < 200ms cold. `lazy.nvim` handles most of this.

4. **XDG Compliance**
   - Store configs under `~/.config/` (nvim, tmux via `XDG_CONFIG_HOME/tmux/tmux.conf`, starship).
   - Avoid cluttering `$HOME` with dotfiles.

5. **Font Installation (Non-Interactive)**
   - Download MesloLGS NF Regular/Bold/Italic/Bold-Italic TTFs from the Nerd Fonts release page and install to `~/.local/share/fonts/`.
   - Run `fc-cache -fv`.

---

## 7. Recommended File Layout for New Dotfiles

```
.dotfiles/
├── zsh/
│   ├── .zshrc                 # main entry: exports, aliases, compinit, plugin sourcing
│   ├── .zprofile              # login shell only (PATH, env vars)
│   └── plugins/               # cloned repos (autosuggestions, syntax-highlighting)
├── nvim/
│   └── .config/nvim/
│       ├── init.lua           # bootstrap lazy.nvim + require core
│       ├── lazy-lock.json     # pinned plugin commits
│       └── lua/
│           ├── core/
│           │   ├── options.lua
│           │   ├── keymaps.lua
│           │   └── autocmds.lua
│           └── plugins/
│               ├── lsp.lua
│               ├── telescope.lua
│               ├── treesitter.lua
│               ├── ui.lua       # bufferline, lualine, nvim-tree, theme
│               └── git.lua
├── tmux/
│   └── .tmux.conf             # TPM init + plugins + keybindings
├── starship/
│   └── .config/starship.toml
├── bin/
│   └── install-fonts.sh       # MesloLGS NF installer
└── setup.sh                   # idempotent installer
```

---

## 8. Installation / Bootstrap Strategy

For the Ubuntu dev box setup project:
1. **Stage 1 (Install)**: Add `starship`, `fzf`, `fd`, `bat`, `eza`, `ripgrep`, `neovim`, `tmux`, `zsh`, `git`, `lazygit` to the appropriate `packages/apt.yaml` or `packages/script.yaml`.
2. **Stage 3 (Pull)**: Clone TPM, zsh plugins, and optionally kickstart.nvim.
3. **Stage 4 (Config)**: Symlink (or copy) the dotfiles from this repo into `$HOME/.config/` and `$HOME`.
4. **Post-Config**:
   - Run `nvim --headless -c 'Lazy! sync' -c 'qa'` to install all Neovim plugins.
   - Run `tmux start-server; tmux run-shell ~/.tmux/plugins/tpm/bindings/install_plugins` or simply open tmux and press `prefix + I`.
   - Run `source ~/.zshrc` or `exec zsh`.

---

## 9. Suggested Theme & Aesthetic

- **Colorscheme**: Catppuccin Mocha (dark) or Macchiato. It has official ports for Neovim, Tmux, Zsh (via Starship), Bat, and fzf.
- **Font**: MesloLGS NF (patched for Powerline/Nerd Fonts). Provides all required glyphs.
- **Terminal Emulator** (if applicable): WezTerm, Kitty, Alacritty, or modern Windows Terminal. All support true color and undercurl.

---

## 10. References

| Resource | Link | Purpose |
|----------|------|---------|
| kickstart.nvim | https://github.com/nvim-lua/kickstart.nvim | Neovim starter config |
| lazy.nvim | https://github.com/folke/lazy.nvim | Neovim plugin manager |
| LazyVim | https://www.lazyvim.org/ | Full Neovim distribution (for reference) |
| Starship | https://starship.rs | Shell prompt |
| zsh-autosuggestions | https://github.com/zsh-users/zsh-autosuggestions | Zsh history suggestions |
| zsh-syntax-highlighting | https://github.com/zsh-users/zsh-syntax-highlighting | Zsh syntax highlighting |
| TPM | https://github.com/tmux-plugins/tpm | Tmux plugin manager |
| tmux-sensible | https://github.com/tmux-plugins/tmux-sensible | Sane tmux defaults |
| Catppuccin Tmux | https://github.com/catppuccin/tmux | Tmux theme |
| fzf | https://github.com/junegunn/fzf | Fuzzy finder |
| bat | https://github.com/sharkdp/bat | cat replacement |
| eza | https://github.com/eza-community/eza | ls replacement |
| fd | https://github.com/sharkdp/fd | find replacement |
| nvim-tree.lua | https://github.com/nvim-tree/nvim-tree.lua | Neovim file explorer |
| bufferline.nvim | https://github.com/akinsho/bufferline.nvim | Neovim bufferline |

---

## 11. Conclusion / Next Steps

To build the dotfiles from scratch:
1. Start with a **minimal `init.lua`** bootstrapping `lazy.nvim` and a few essential plugins (treesitter, telescope, lspconfig, nvim-tree, lualine, bufferline, gitsigns, catppuccin).
2. Write a **`.tmux.conf`** with TPM, tmux-sensible, catppuccin theme, and vi-mode.
3. Write a **`.zshrc`** with plain Zsh, Starship prompt, autosuggestions, syntax-highlighting, and aliases for the modern CLI tools.
4. Ensure everything is **non-interactive** and can be bootstrapped by `setup.py` Stage 4.
5. Use **Catppuccin Mocha** + **MesloLGS NF** for a unified visual experience across Neovim, Tmux, Zsh, and Bat.
