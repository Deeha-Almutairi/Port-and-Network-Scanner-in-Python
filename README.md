Port & Network Scanner

Port & Network Scanner is a Python-based tool for scanning open ports on a target host and discovering devices on the local network using ARP.
It is designed for learning, lab use, and testing purposes only.

Project Overview

Port scan of common ports: 22 (SSH), 80 (HTTP), 443 (HTTPS), 21 (FTP), 25 (SMTP), 53 (DNS), 139 (NetBIOS), 143 (IMAP), 161 (SNMP), 389 (LDAP)

Local network ARP discovery to find connected devices (IP + MAC)

ASCII banner using pyfiglet

Service detection when possible

Goals

Simplify testing and learning network scanning techniques

Understand basic network mapping and port scanning

Provide a foundation for building more advanced network tools

Technologies Used
Layer	Technologies
Programming	Python 3.8+
Networking	socket, scapy
UI / Display	pyfiglet (ASCII banner)
Features

Simple TCP port scan for a list of predefined ports

Local network ARP scan to discover connected devices

Automatic detection of local subnet (/24)

Displays service names where available

Security & Legal Notice

Do not scan networks or devices without explicit permission.

Intended only for personal labs, learning environments, or networks you are authorized to test.

Future Improvements

Add CLI arguments for non-interactive use

Implement multithreading to speed up port scans

Allow reading port lists from configuration file

Export results to CSV or JSON

Integrate with python-nmap for advanced scanning

How to Run

Set up a Python virtual environment:

python -m venv venv
# Activate environment
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\activate

pip install --upgrade pip
pip install pyfiglet scapy


Run the script:

sudo python scanner.py   # Linux / macOS
python scanner.py        # Windows (Run PowerShell as Administrator)


Enter a hostname or IP when prompted.

The script scans ports and then scans your local /24 subnet for devices.
