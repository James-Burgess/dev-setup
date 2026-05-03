# Communication

Package file: `packages/communication.yaml`

---

## `signal-cli`

Signal CLI (needs Java).

### Description
`signal-cli` is a command-line interface for Signal Messenger. It allows sending and receiving Signal messages, managing contacts, and linking devices without a GUI.

### Usage
```bash
# Register a phone number
signal-cli -a +12345678901 register

# Verify registration code
signal-cli -a +12345678901 verify 123456

# Send a message
signal-cli -a +12345678901 send -m "Hello" +10987654321

# Receive messages
signal-cli -a +12345678901 receive
```

---

## `whatsapp-cli`

WhatsApp CLI.

### Description
`whatsapp-cli` provides terminal-based access to WhatsApp messaging via the WhatsApp Web protocol.

### Usage
```bash
# Start the CLI
whatsapp-cli

# Scan QR code with your phone to authenticate
# Send messages: /message <number> <text>
```

---

## `teams-cli`

Teams CLI.

### Description
`teams-for-linux` is an unofficial Teams client for Linux. The CLI wrapper enables launching and basic interaction from the terminal.

### Usage
```bash
# Launch Teams
teams-for-linux

# Launch minimized
teams-for-linux --minimized
```

---

## `discord-cli`

Discord TUI (discordo).

### Description
`discordo` is a terminal UI for Discord. It allows browsing servers, channels, and sending messages entirely from the terminal.

### Usage
```bash
# Start the TUI
discordo

# Authenticate with your Discord token
# Navigate with arrow keys, type to send messages
```
