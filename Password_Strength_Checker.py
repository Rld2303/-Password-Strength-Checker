import re
from pathlib import Path

# Load common passwords with case-insensitive matching
try:
    COMMON_PASSWORDS = {pwd.lower().strip() for pwd in 
                       Path("common_passwords.txt").read_text(encoding='utf-8').splitlines()}
except FileNotFoundError:
    print("⚠️ common_passwords.txt not found. Using minimal default list.")
    COMMON_PASSWORDS = {"123456", "password", "admin", "qwerty"}

def check_password_strength(pwd):
    """Check password against NIST SP 800-63B guidelines."""
    errors = []
    
    # NIST Rule: Ban common passwords (exact lowercase match)
    if pwd.lower() in COMMON_PASSWORDS:
        errors.append("❌ Extremely common password (top 1M breached)")
    
    # NIST Rule: Minimum 8 chars
    if len(pwd) < 8:
        errors.append("❌ Too short (min 8 characters)")
    
    # Custom Rule: No 3+ repeating chars (e.g., 'aaa') but allow '123'
    if re.search(r"(.)\1{2,}", pwd.lower()):
        errors.append("❌ Repeating characters (e.g., 'aaa')")
    
    # Output results
    if errors:
        print("\nPassword is ❌ Weak:")
        for e in errors:
            print("-", e)
    else:
        print("\n✅ Strong password (NIST-compliant!)")

if __name__ == "__main__":
    password = input("Enter password: ")
    check_password_strength(password)