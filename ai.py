import datetime

print("=" * 60)
print("🤖               M U S A   A I")
print("=" * 60)
print("Version : 0.3")
print("Status  : Online")
print("Developer : Musa")
print("=" * 60)

name = input("👤 Enter your name: ")

print(f"\n🤖 Welcome {name}!")
print("I am MUSA AI.")
print("Type 'help' to see commands.")
print("Type 'exit' to close MUSA AI.\n")

while True:

    user = input(f"\n{name} ➜ ").strip().lower()

    if user == "exit":
        print("\n🤖 Thank you for using MUSA AI.")
        print("Have a wonderful day! 👋")
        break

    elif user == "hello":
        print("\n🤖 Hello!")
        print("It is great to meet you.")
        print("How can I assist you today?")

    elif user == "how are you":
        print("\n🤖 I am doing great!")
        print("I am always ready to help you with programming,")
        print("technology, cybersecurity, and much more.")

    elif user == "your name":
        print("\n🤖 My name is MUSA AI.")
        print("I am your personal AI assistant.")

    elif user == "time":
        now = datetime.datetime.now()
        print("\n🕒 Current Time:", now.strftime("%I:%M:%S %p"))

    elif user == "date":
        now = datetime.datetime.now()
        print("\n📅 Today's Date:", now.strftime("%d-%m-%Y"))

    elif user == "python":
        print("""
🐍 Python is one of the most popular programming languages.
It is used in:
• Artificial Intelligence
• Machine Learning
• Cybersecurity
• Automation
• Web Development
• Data Science
        """)

    elif user == "cybersecurity":
        print("""
🛡️ Cybersecurity protects computers, networks,
websites and digital information from hackers
and cyber attacks.

Major Fields:
✔ Ethical Hacking
✔ Penetration Testing
✔ Digital Forensics
✔ Malware Analysis
✔ SOC Analyst
✔ Cloud Security
        """)

    elif user == "ai":
        print("""
🤖 Artificial Intelligence (AI)

AI enables computers to learn, analyze,
solve problems and interact like humans.

Examples:
✔ ChatGPT
✔ Gemini
✔ Claude
✔ DeepSeek
✔ MUSA AI (Future)
        """)

    elif user == "help":

        print("""
================ AVAILABLE COMMANDS ================

hello
how are you
your name
python
cybersecurity
ai
time
date
help
exit

====================================================
""")

    else:
        print("\n🤖 I don't know the answer yet.")
        print("I am still learning.")
        print("Soon I will become much smarter!")