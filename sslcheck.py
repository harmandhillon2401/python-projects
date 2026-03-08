import ssl
import socket

def check_ssl(hostname):
    print(f"\nChecking SSL for: {hostname}")
    print("=" * 40)
    
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            
            print(f"TLS Version: {ssock.version()}")
            print(f"Issued To: {cert['subject'][0][0][1]}")
            print(f"Issued By: {cert['issuer'][1][0][1]}")
            print(f"Valid Until: {cert['notAfter']}")
            print("Certificate: VALID!")

check_ssl("www.google.com")
check_ssl("www.github.com")