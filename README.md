PORT & NETWORK SCANNER

A simple Python script for port scanning a specific target and ARP-based local network discovery. This README explains how to set up and run the tool. Intended for learning or testing environments only.

Description

A simple tool for scanning ports (Port Scan) on a specific host and scanning the local network to discover connected devices using ARP. Useful for learning or lab use.
The script includes:

Scanning common ports (22, 80, 443, 21, 25, 53, 139, 143, 161, 389).

Local network scanning using ARP to find connected devices.

Displaying service names when possible.

An ASCII banner using pyfiglet.

Note: This tool is for legal and authorized use only (your own network or networks you have explicit permission to scan). Unauthorized scanning may be illegal.

Requirements

Python 3.8+ (recommended)

The following packages:

pyfiglet

scapy

Install dependencies:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows (PowerShell)

pip install --upgrade pip
pip install pyfiglet scapy


Note: scapy may require elevated privileges for ARP operations or extra system libraries on some distributions.

How to Run

Run the script:

sudo python scanner.py


On Windows (run PowerShell as Administrator):

python scanner.py


You will be prompted to enter a hostname or IP to scan.
After the port scan, it will automatically scan the local network (e.g., 192.168.1.0/24).

Example Output
PORT & NETWORK SCANNER
--------------------------------------------------
Scanning Target IP Address: 192.168.1.10
--------------------------------------------------
Port 22 is open
  Service: ssh
Port 80 is open
  Service: http
Port 443 is filtered
Port 21 is closed
...
Scanning the network: 192.168.1.0/24
Discovered devices:
IP: 192.168.1.1, MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.15, MAC: 11:22:33:44:55:66

Technical Notes

get_local_ip() uses socket.gethostbyname(socket.gethostname()); on some systems it may return 127.0.0.1. You can modify it to connect to 8.8.8.8 and read the socket’s local address instead.

Port scanning uses socket.connect_ex() with a short timeout for quick scanning. Advanced scans may use nmap or python-nmap.

srp() from scapy requires root/admin privileges for ARP scanning.

Legal & Security Notice

Do not scan any network or device without explicit permission.

Use only in your lab environment, personal devices, or with written authorization.

Suggested Improvements

Add CLI arguments instead of interactive input.

Add multithreading to speed up scanning.

Use a config file for custom port lists.

Export results to CSV or JSON.

Integrate with python-nmap for advanced scanning.

GitHub Tips

Create a .gitignore file:

venv/
__pycache__/
*.pyc
.env


Also include:

LICENSE (e.g., MIT)

examples/ folder with sample runs or screenshots

Contributing

Contributions are welcome!
Open issues or submit pull requests for new features or bug fixes.
