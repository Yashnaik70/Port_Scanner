import socket  # network functions
from datetime import datetime  # get time

# common ports with services
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

# scan ports on host
def scan_host(host):
    print(f"\n[+] Scanning {host} on {len(common_ports)} ports...")
    print("Started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
        socket.setdefaulttimeout(1)  # set timeout
        result = sock.connect_ex((host, port))  # try connect

        if result == 0:
            service = common_ports[port]
            print(f"  [OPEN] Port {port} ({service})")
            open_ports.append((port, service))
        sock.close()

    if not open_ports:
        print("  No common ports open.")

    return open_ports

# run if main file
if __name__ == "__main__":
    target = input("Enter IP address or hostname to scan: ")
    try:
        scan_host(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\nScan canceled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
