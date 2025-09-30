#!/usr/bin/env python3
"""nmap_to_markdown.py
Simple converter: Nmap XML (-oX) -> Markdown summary (services table + OS guess)
Usage: python3 nmap_to_markdown.py scans/target.xml > target_summary.md
"""
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python3 nmap_to_markdown.py <nmap-xml-file>")
    sys.exit(1)

xmlfile = sys.argv[1]

try:
    tree = ET.parse(xmlfile)
except Exception as e:
    print(f"Error parsing XML: {e}")
    sys.exit(1)

root = tree.getroot()

host = root.find('host')
if host is None:
    print('# Nmap Summary

No host found in XML.')
    sys.exit(0)

# hostname / addr
addr = host.find('address')
ip = addr.get('addr') if addr is not None else 'unknown'

hostname = 'N/A'
for hn in host.findall('hostnames/hostname'):
    hostname = hn.get('name')

# OS
os_elem = host.find('os/osmatch')
os_guess = os_elem.get('name') if os_elem is not None else 'Unknown'

# uptime
uptime_elem = host.find('uptime')
uptime = uptime_elem.get('lastboot') if uptime_elem is not None else 'N/A'

print(f"# Nmap Scan Summary for {ip} ({hostname})
")
print(f"**Generated:** {datetime.utcnow().isoformat()}Z
")
print(f"**OS Guess:** {os_guess}
")
print('## Open Services
')
print('| Port | Protocol | Service | Version | State |')
print('|------|----------|---------|---------|-------|')

ports = host.findall('ports/port')
for p in ports:
    portid = p.get('portid')
    protocol = p.get('protocol')
    state = p.find('state').get('state') if p.find('state') is not None else 'unknown'
    svc = p.find('service')
    svcname = svc.get('name') if svc is not None and svc.get('name') is not None else ''
    svcver = ''
    if svc is not None:
        prod = svc.get('product') or ''
        ver = svc.get('version') or ''
        extr = svc.get('extrainfo') or ''
        svcver = ' '.join([x for x in [prod, ver, extr] if x])
    print(f"| {portid} | {protocol} | {svcname} | {svcver} | {state} |")

print('
## Notes
')
print('- Convert this summary and add screenshots / sanitized outputs to your lab report.')
