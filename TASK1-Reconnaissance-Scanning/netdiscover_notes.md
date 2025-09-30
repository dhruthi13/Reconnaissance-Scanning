# Netdiscover Notes

- `sudo netdiscover -r <subnet> -P` — passive ARP discovery on given subnet.
- `-i <iface>` — specify interface.
- Example: `sudo netdiscover -i eth0 -r 192.168.56.0/24 -P`.

Interpretation:
- The tool reports MAC, IP, and vendor. Useful for quickly mapping hosts in lab environment.

Safety:
- ARP scans are local-only (layer 2) but still run only on authorized networks.
