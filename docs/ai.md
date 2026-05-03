# AI

Package file: `packages/ai.yaml`

---

## `ollama`

Local LLM runner.

### Description
`ollama` makes it easy to run large language models locally. It handles downloading models, GPU acceleration, and provides a simple CLI and API server.

### Usage
```bash
# Pull a model
ollama pull llama3

# Run a model interactively
ollama run llama3

# Serve the API
ollama serve

# List downloaded models
ollama list

# Remove a model
ollama rm llama3
```

---

## `opencode`

AI CLI code assistant.

### Description
`opencode` is an AI-powered CLI assistant for writing, explaining, and refactoring code. It connects to LLM APIs for terminal-based coding help.

### Usage
```bash
# Ask a coding question
opencode "explain recursion in Python"

# Refactor a file
opencode --file script.py "refactor this into a class"

# Generate tests
opencode --file utils.py "write unit tests for these functions"
```

---

## `browser-use`

AI browser agent.

### Description
`browser-use` is a Python library that lets AI agents control a web browser to perform tasks like form filling, navigation, and data extraction.

### Usage
```bash
# Requires Python and pip
# Quickstart in Python:
# from browser_use import Agent
# agent = Agent()
# agent.run("Go to example.com and find the contact email")
```
