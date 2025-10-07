PORT & NETWORK SCANNER

A simple Python tool for scanning open ports on a target host and discovering active devices on your local network using ARP. This project is meant for learning and lab use only — not for unauthorized scanning.

📘 Description

PORT & NETWORK SCANNER is a beginner-friendly script that:

Scans a list of common ports (22, 80, 443, 21, 25, 53, 139, 143, 161, 389).

Performs a local network ARP scan to find connected devices.

Displays service names when possible.

Includes a cool ASCII banner using pyfiglet.

⚠️ Disclaimer: This tool is for authorized use only. Scanning networks without permission is illegal in most jurisdictions.

🧩 Requirements

Python 3.8 or newer

The following Python libraries:

pyfiglet

scapy

Install dependencies:

python -m venv venv
# Activate virtual environment
# Linux / macOS:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\activate

pip install --upgrade pip
pip install pyfiglet scapy


Note: Some systems may require administrative privileges or extra dependencies for scapy.

⚙️ How to Run

Run the script directly from your terminal:

On Linux / macOS:
sudo python scanner.py

On Windows (Run as Administrator):
python scanner.py


When prompted, enter the target IP or hostname.
The script will perform a port scan, then automatically detect your local IP and scan the /24 subnet (e.g. 192.168.1.0/24).

🖥️ Example Output
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

🧠 Technical Notes

get_local_ip() uses socket.gethostbyname(socket.gethostname()).
If it returns 127.0.0.1, modify it to connect temporarily to a public IP (like 8.8.8.8) to detect your real local IP.

The port scan uses socket.connect_ex() with a short timeout — fast but simple.
For more advanced scans, use nmap or integrate python-nmap.

The ARP discovery via scapy.srp() requires root/administrator privileges.

🔐 Legal & Security Notice

Do not scan any network or host without explicit permission.

Use it only for your personal lab, test environments, or with written consent.

🚀 Future Improvements

Add CLI arguments (argparse) for non-interactive use.

Add multithreading to speed up port scans.

Allow configuration of port lists via a file.

Export scan results to CSV/JSON.

Integrate with python-nmap for extended features.

🧾 GitHub Setup Tips

Add a .gitignore file to clean your repo:

venv/
__pycache__/
*.pyc
.env


Also consider adding:

LICENSE (e.g., MIT)

examples/ folder for screenshots or test runs

🤝 Contributing

Pull requests are welcome!
If you find a bug or want to suggest a feature, open an issue or submit a PR.

📄 License

Add a LICENSE file (e.g., MIT) or specify that this project is for personal/educational use only.
