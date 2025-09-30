# cyber-hands-on-recon — Task 1: Reconnaissance & Scanning

**Objective**
This repository contains lab instructions, scripts, and report templates for Task 1: Reconnaissance & Scanning — focusing on passive and active discovery using tools like Netdiscover and Nmap.

**Contents**
- `TASK1-Reconnaissance-Scanning/` — task folder with all files.
  - `lab_instructions.md` — step-by-step commands and safe flags.
  - `lab_report_template.md` — markdown template for submitting the lab report.
  - `nmap_scan.sh` — automated Nmap scan script (bash).
  - `nmap_to_markdown.py` — convert Nmap XML to Markdown.
  - `netdiscover_notes.md` — short netdiscover guide.
  - `sample_outputs/` — placeholder for sanitized scan outputs.
- `.gitignore` — recommended ignores.
- `LICENSE` — MIT license template.
- `CONTRIBUTING.md` — how to contribute.

**Usage (quick)**
1. Clone or create repo locally.
2. Copy files from `TASK1-Reconnaissance-Scanning/` into the same folder structure locally.
3. Make the script executable: `chmod +x TASK1-Reconnaissance-Scanning/nmap_scan.sh`.
4. Run sample scan: `./TASK1-Reconnaissance-Scanning/nmap_scan.sh 192.168.56.101 target-name`
5. Convert XML to Markdown: `python3 TASK1-Reconnaissance-Scanning/nmap_to_markdown.py scans/target-name.xml > scans/target-name_summary.md`

**Ethics & safety**
- Only run scans against systems you own or have explicit permission to test.
- Use host-only or isolated internal networks for vulnerable VMs.
- Do not commit raw PCAPs or PII to the repository.
