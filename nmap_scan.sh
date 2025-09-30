#!/usr/bin/env bash
# nmap_scan.sh - simple Nmap runner for lab scans
# Usage: ./nmap_scan.sh <target-ip> <label>

set -e

TARGET="$1"
LABEL="$2"

if [[ -z "$TARGET" || -z "$LABEL" ]]; then
  echo "Usage: $0 <target-ip> <label>"
  exit 1
fi

OUTDIR="scans"
mkdir -p "$OUTDIR"

# Full TCP SYN scan for open ports (fast-ish)
echo "[+] Running SYN full-port scan on $TARGET (label=$LABEL)"
nmap -sS -p- --open -T4 -oA "$OUTDIR/${LABEL}" "$TARGET"

# Service + version + OS detection on discovered ports (if any)
echo "[+] Running service/version and OS detection"
# use previously discovered ports list if desired; here we run a full sweep for completeness
nmap -sS -sV -O -p1-65535 -T4 -oA "$OUTDIR/${LABEL}-service" "$TARGET"

# Note: UDP scans are slow; uncomment when needed
# echo "[+] Running quick UDP scan (top 100)"
# sudo nmap -sU -sV --top-ports 100 -oA "$OUTDIR/${LABEL}-udp" "$TARGET"

echo "[+] Scans saved to $OUTDIR/"
