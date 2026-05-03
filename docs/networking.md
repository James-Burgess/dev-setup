# Networking

Package file: `packages/networking.yaml`

---

## `netmon`

nethogs, iftop, nload, iperf3, tcpdump.

### Description
`netmon` installs a bundle of network monitoring utilities:
- `nethogs` — per-process bandwidth usage
- `iftop` — bandwidth usage by host
- `nload` — real-time network throughput graphs
- `iperf3` — bandwidth testing between two hosts
- `tcpdump` — packet capture and analysis

### Usage
```bash
# Per-process bandwidth
sudo nethogs

# Bandwidth by remote host
sudo iftop

# Simple throughput monitor
nload

# Test bandwidth to a server
iperf3 -c 192.168.1.1

# Start iperf3 server
iperf3 -s

# Capture packets on interface
sudo tcpdump -i eth0

# Capture and save to file
sudo tcpdump -i eth0 -w capture.pcap
```

---

## `tailscale`

Mesh VPN.

### Description
`tailscale` builds a private WireGuard-based mesh network between your devices. It provides secure access to servers, remote debugging, and file sharing without opening firewall ports.

### Usage
```bash
# Authenticate with Tailscale
sudo tailscale up

# Check your tailnet IPs
tailscale status

# SSH into a machine over Tailscale
tailscale ssh user@machine-name

# Serve a local service over Tailscale
sudo tailscale serve --https=443 --set-path=/ localhost:3000

# Funnel to the public internet
sudo tailscale funnel --https=443 localhost:3000

# Logout
tailscale logout
```
