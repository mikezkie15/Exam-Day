import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?|ftp):\/\/'  # Protocol (http, https, ftp)
        r'([a-zA-Z0-9.-]+)\.'  # Subdomain or domain
        r'([a-zA-Z]{2,20})'  # TLD (like .com, .org, .technology)
        r'(:\d+)?'  # Optional port (e.g., :8080)
        r'(\/[^\s]*)?'  # Optional path
        r'(\?[^\s]*)?'  # Optional query parameters
        r'(#\S*)?$'  # Optional fragment identifier
    )
    return re.match(pattern, url) is not None

url = input("Enter a URL to check: ")

if is_valid_url(url):
    print("✅ URL is valid")
else:
    print("❌ URL is not valid")
