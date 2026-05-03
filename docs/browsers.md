# Browsers

Package file: `packages/browsers.yaml`

---

## `firefox`

Firefox.

### Description
`firefox` is the free and open-source web browser from Mozilla. It features strong privacy protections, extensions, and developer tools.

### Usage
```bash
# Launch Firefox
firefox

# Open a URL
firefox https://example.com

# Private browsing
firefox --private-window

# Headless screenshot
firefox --headless --screenshot https://example.com
```

---

## `brave`

Brave browser.

### Description
`brave` is a privacy-focused browser based on Chromium. It blocks trackers and ads by default and supports a built-in crypto wallet and Tor private windows.

### Usage
```bash
# Launch Brave
brave

# Open a URL
brave https://example.com

# Incognito mode
brave --incognito
```

---

## `browsh`

Text browser (TTY).

### Description
`browsh` renders modern websites as text inside a terminal. It runs a headless Firefox in the background and streams a text representation to your TTY over SSH.

### Usage
```bash
# Launch in terminal
browsh

# Open a specific URL
browsh https://example.com

# Ideal for low-bandwidth or SSH-only environments
```

---

## `puppeteer`

Headless Chrome.

### Description
`puppeteer` is a Node.js library providing a high-level API to control headless Chrome or Chromium. It is used for automated testing, scraping, and PDF/screenshot generation.

### Usage
```bash
# Requires Node.js installed via nvm first
# Generate a screenshot via a small script:
npx puppeteer script.js

# Script example (script.js):
# const puppeteer = require('puppeteer');
# (async () => {
#   const browser = await puppeteer.launch();
#   const page = await browser.newPage();
#   await page.goto('https://example.com');
#   await page.screenshot({path: 'example.png'});
#   await browser.close();
# })();
```

---

## `playwright`

Cross-browser automation.

### Description
`playwright` is a browser automation library supporting Chromium, Firefox, and WebKit. It enables reliable end-to-end testing and web scraping with auto-waiting and tracing.

### Usage
```bash
# Install browsers
npx playwright install

# Install dependencies
npx playwright install-deps

# Run a test
npx playwright test

# Record a test
npx playwright codegen https://example.com

# Run in UI mode
npx playwright test --ui
```
