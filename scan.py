import pyfiglet
import sys
import socket
from scapy.all import ARP, Ether, srp

ascii_banner = pyfiglet.figlet_format("PORT & NETWORK SCANNER")
print(ascii_banner)

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=9, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def port_scan(target):
    try:
        socket.inet_aton(target)
        target_is_ip = True
    except socket.error:

        try:
            target = socket.gethostbyname(target)
            target_is_ip = False
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved!!!!")
            sys.exit()

    print("-" * 50)
    if target_is_ip:
        print("Scanning Target IP Address: " + target)
    else:
        print("Scanning Target: " + target)
    print("-" * 50)

    ports = [22, 80, 443 ,21, 25, 53, 139, 143, 161, 389]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
                try:
                    service = socket.getservbyport(port)
                    print(f"  Service: {service}")
                except OSError:
                    print(f"  Service: Unknown")
            elif result == 111:
                print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered")
        except socket.error as e:
            print(f"Error connecting to port {port}: {e}")
        s.close()

def main():
    target = input("Enter the target hostname or IP address: ")
    port_scan(target)

    local_ip = get_local_ip()
    ip_parts = local_ip.split('.')
    ip_range = '.'.join(ip_parts[:3]) + '.0/24'

    print(f"Scanning the network: {ip_range}")
    devices = scan_network(ip_range)

    if devices:
        print("Discovered devices:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("No devices found.")

main()
