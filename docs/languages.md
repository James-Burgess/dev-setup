# Languages

Package file: `packages/languages.yaml`

---

## `python3-pip`

Python3 + pip + venv.

### Description
`python3-pip` installs Python 3, the pip package manager, and the `venv` module for creating isolated Python environments. It is essential for Python development.

### Usage
```bash
# Install a package globally
pip3 install requests

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install inside a venv
pip install flask

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Run a Python script
python3 script.py
```

---

## `go`

Go toolchain.

### Description
`go` is the official Go language toolchain including the compiler, formatter (`gofmt`), package manager, and testing tools.

### Usage
```bash
# Run a program
go run main.go

# Build an executable
go build -o myapp

# Initialize a module
go mod init example.com/myapp

# Get dependencies
go get github.com/gin-gonic/gin

# Run tests
go test ./...

# Format code
go fmt ./...
```

---

## `pyenv`

Python version manager.

### Description
`pyenv` lets you install and switch between multiple Python versions globally or per-project. It works by shim PATH manipulation and compiles Pythons from source.

### Usage
```bash
# List installable versions
pyenv install --list

# Install a Python version
pyenv install 3.12.0

# Set global version
pyenv global 3.12.0

# Set local version (creates .python-version)
pyenv local 3.12.0

# Run a specific version
pyenv shell 3.11.0

# List installed versions
pyenv versions
```

---

## `rust`

Rust via rustup.

### Description
`rustup` installs the Rust toolchain (`rustc`, `cargo`, `rustfmt`, `clippy`). Cargo is the build system and package manager for Rust.

### Usage
```bash
# Verify installation
rustc --version && cargo --version

# Create a new project
cargo new myapp

# Build and run
cargo run

# Run tests
cargo test

# Build for release
cargo build --release

# Add a dependency
cargo add serde --features derive
```

---

## `nvm`

Node version manager.

### Description
`nvm` installs and manages multiple Node.js versions. It allows per-project `.nvmrc` files and quick switching between LTS and latest releases.

### Usage
```bash
# Install a Node version
nvm install 20

# Use a specific version
nvm use 20

# Set default
nvm alias default 20

# List installed versions
nvm ls

# Run a command with a specific version
nvm run 18 -- app.js
```
