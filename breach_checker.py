from logger import log_event
import hashlib
import requests

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    
    # Debugging: Print API response
    print(f"Checking password: {password}")
    print(f"SHA1 Hash: {sha1_password}")
    print(f"API Response (first 200 chars): {response.text[:200]}")

    if suffix in response.text:
        log_event("BREACH_DETECTED", f"Password {password[:3]}**** is in a data breach.")
        return True  # Password is breached

    log_event("SAFE_PASSWORD", f"Password {password[:3]}**** is safe.")
    return False  # Password is safe