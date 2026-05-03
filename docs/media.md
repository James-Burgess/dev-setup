# Media

Package file: `packages/media.yaml`

---

## `vlc`

VLC media player.

### Description
`vlc` is the popular cross-platform multimedia player and framework. It supports virtually all audio/video formats, streaming protocols, and network sources.

### Usage
```bash
# Open a file
vlc movie.mp4

# Stream to HTTP
vlc movie.mp4 --sout '#standard{access=http,mux=ts,dst=:8080}'

# Convert media
vlc input.mp4 --sout '#transcode{vcodec=h264,acodec=mp3}:file{dst=output.mkv}'
```

---

## `aria2`

CLI torrent + HTTP downloader.

### Description
`aria2` is a lightweight multi-protocol and multi-source command-line download utility. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent, and Metalink.

### Usage
```bash
# Download a file over HTTP
aria2c https://example.com/file.iso

# Multi-connection download (faster)
aria2c -x 16 -s 16 https://example.com/file.iso

# Download a torrent
aria2c file.torrent

# Download with a metalink
aria2c file.metalink

# Resume a broken download
aria2c -c https://example.com/file.iso
```

---

## `webtorrent-cli`

WebTorrent CLI.

### Description
`webtorrent-cli` streams and downloads torrents from the command line using WebTorrent, supporting both traditional torrents and magnet links.

### Usage
```bash
# Download a torrent
webtorrent magnet:?xt=urn:btih:...

# Stream a torrent to VLC
webtorrent magnet:?xt=urn:btih:... --vlc

# Stream to stdout (pipe to player)
webtorrent magnet:?xt=urn:btih:... --stdout | vlc -

# Download to a specific folder
webtorrent magnet:?xt=urn:btih:... -o ./downloads
```
