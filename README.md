# 🔒 NIST Password Policy Enforcer

A Python script that enforces modern password best practices based on **NIST SP 800-63B guidelines**, focusing on usability while blocking truly weak credentials.

## 🛡️ Key Features
- **Blocks 1M+ breached passwords** (case-insensitive check)
- **Minimum 8 characters** (configurable)
- **Blocks repeating patterns** (e.g., `aaa`) without arbitrary complexity rules
- **Clear feedback** with emoji-based strength indicators

**Sample Output**
Enter password: password123
❌ Weak: 
- Extremely common password (top 1M breached)

Enter password: Secure@2024
✅ Strong password (NIST-compliant!)

## 🚀 Quick Start
```bash
git clone https://github.com/Rld2303/Password-Strength-Checker.git
cd Password-Strength-Checker
python password_checker.py

