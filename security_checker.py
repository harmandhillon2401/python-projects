import requests

def check_website_security(url):
    print(f"\nChecking: {url}")
    print("=" * 40)
    
    response = requests.get(url)
    
    if url.startswith("https"):
        print("HTTPS - SECURE!")
    else:
        print("HTTP - NOT Secure!")
    
    print(f"Status: {response.status_code}")
    
    server = response.headers.get('Server', 'Unknown')
    print(f"Server: {server}")
    
    hsts = response.headers.get('Strict-Transport-Security', 'Not Set')
    if hsts != "Not Set":
        print("HSTS - SECURED")
    else:
        print("HSTS - NOT SET")

check_website_security("https://www.google.com")
check_website_security("http://www.example.com")