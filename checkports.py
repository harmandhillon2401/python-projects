import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((host, port))
    sock.close()
    
    if result == 0:
        print(f"Port {port} - OPEN")
    else:
        print(f"Port {port} - CLOSED")

check_port("google.com", 80)
check_port("google.com", 443)
check_port("google.com", 22)
check_port("google.com", 3306)