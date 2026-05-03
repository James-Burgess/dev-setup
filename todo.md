google cloud needs user entry
post install for each script (path and .zshrc) (or do we do that in configure step?)
iperf3 needs entry
attuin needs input. no account, no ai. daemon on.




─── jaq [cli-tools] ────────────────────
  → sudo apt install -y jaq
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package jaq
  ✗ Failed: sudo apt install -y jaq

─── dust [cli-tools] ────────────────────
  → sudo apt install -y dust
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done

No apt package "dust", but there is a snap with that name.
Try "snap install dust"

E: Unable to locate package dust
  ✗ Failed: sudo apt install -y dust

─── signal-cli [communication] ────────────────────
  → sudo apt install -y default-jre
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
default-jre is already the newest version (2:1.21-75+exp1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
  → sudo curl -fsSL https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-latest-linux-amd64.tar.gz | sudo tar xz -C /usr/local/bin --strip-components=1
curl: (22) The requested URL returned error: 404

gzip: stdin: unexpected end of file
tar: Child returned status 1
tar: Error is not recoverable: exiting now
  ✗ Failed: sudo curl -fsSL https://github.com/AsamK/signal-cli/releases/latest/download/signal-cli-latest-linux-amd64.tar.gz | sudo tar xz -C /usr/local/bin --strip-components=1

─── discord-cli [communication] ────────────────────
  → go install github.com/ayn2op/discordo/cmd/discordo@latest
go: github.com/ayn2op/discordo@v0.0.0-20260430060403-b3fe7e345324 requires go >= 1.26.0; switching to go1.26.2
go: github.com/ayn2op/discordo/cmd/discordo@latest: module github.com/ayn2op/discordo@latest found (v0.0.0-20260430060403-b3fe7e345324), but does not contain package github.com/ayn2op/discordo/cmd/discordo
  ✗ Failed: go install github.com/ayn2op/discordo/cmd/discordo@latest

─── terraform [infrastructure] ────────────────────
  → sudo apt install -y terraform
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done

No apt package "terraform", but there is a snap with that name.
Try "snap install terraform"

E: Unable to locate package terraform
  ✗ Failed: sudo apt install -y terraform

─── zoho-cli [infrastructure] ────────────────────
  → pip3 install --user --break-system-packages zohocli
WARNING: Skipping /usr/lib/python3.12/dist-packages/asciinema-2.4.0.dist-info due to invalid metadata entry 'name'
ERROR: Could not find a version that satisfies the requirement zohocli (from versions: none)
ERROR: No matching distribution found for zohocli
  ✗ Failed: pip3 install --user --break-system-packages zohocli

─── theHarvester [osint-security] ────────────────────
  → sudo apt install -y theharvester
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package theharvester
  ✗ Failed: sudo apt install -y theharvester

─── recon-ng [osint-security] ────────────────────
  → sudo apt install -y recon-ng
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package recon-ng
  ✗ Failed: sudo apt install -y recon-ng

─── amass [osint-security] ────────────────────
  → sudo apt install -y amass
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done

No apt package "amass", but there is a snap with that name.
Try "snap install amass"

E: Unable to locate package amass
  ✗ Failed: sudo apt install -y amass

─── bashorg-motd [system] ────────────────────
  → sudo curl -fsSL https://raw.githubusercontent.com/bound-journal/bashorg-motd/main/bashorg-motd -o /usr/local/bin/bashorg-motd
curl: (22) The requested URL returned error: 404
  ✗ Failed: sudo curl -fsSL https://raw.githubusercontent.com/bound-journal/bashorg-motd/main/bashorg-motd -o /usr/local/bin/bashorg-motd


-------------
not detecting installed: 

─── pyenv [languages] ────────────────────
  → curl https://pyenv.run | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   270  100   270    0     0    884      0 --:--:-- --:--:-- --:--:--   885

WARNING: Can not proceed with installation. Kindly remove the '/home/jimmy/.pyenv' directory first.

  ✗ Failed: curl https://pyenv.run | bash


