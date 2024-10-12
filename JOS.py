#IMPORTS

import pyfiglet
import time
import sys
import os
import random



#COLORS

BOLD = "\033[1m"
RESET = "\033[0m"
ITALIC = "\033[3m"
FAINT = "\033[2m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"



#VARIABLES

HEALTH = [f"{RED}HOW CAN YOU RUN THIS?",f"{FAINT}{RED}QUESTIONABLE",f"{YELLOW}OK",f"{FAINT}{GREEN}GOOD",f"{GREEN}VERY GOOD!",]
TEMPS =  [f"{RED}HOLY...2957°C",f"{FAINT}{RED}VERY TOASTY",f"{YELLOW}PRETTY NORMAL",f"{FAINT}{GREEN}ROOM TEMP",f"{CYAN}ARTIC...",]



#START SCRIPT

def scroll(string):
  for char in string:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.03)
def midscroll(string):
  for char in string:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.075)
def slowscroll(string):
  for char in string:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.5)


os.system("cls")
scroll(f"STARTING {CYAN}JoeOS       ")
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [- - - - - ]")
time.sleep(0.5)
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [█- - - - ]")
time.sleep(0.5)
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [█-█- - - ]")
time.sleep(0.5)
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [█-█-█- - ]")
time.sleep(0.5)
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [█-█-█-█- ]")
time.sleep(0.5)
os.system("cls")
print(f"{BOLD}{RESET}STARTING {CYAN}JoeOS{GREEN}       [█-█-█-█-█]")
time.sleep(2)

print("")
print("")




{CYAN}
print("")
print(f"     _             ___  ____")
time.sleep(0.3)
print(f"    | | ___   ___ / _ \/ ___|")
time.sleep(0.3)
print(f" _  | |/ _ \ / _ \ | | \___ \ ")
time.sleep(0.3)
print(f"| |_| | (_) |  __/ |_| |___) |")
time.sleep(0.3)
print(f" \___/ \___/ \___|\___/|____/")
time.sleep(0.3)


print("")
print("")

scroll(f"{BOLD}{GREEN}SCANNING SYSTEM       ")
slowscroll(f". . .{RESET}")
print("")
print("")
time.sleep(1)
scroll(f"{CYAN}COMPUTER HEALTH: ")
midscroll(f"{HEALTH[random.randint(0,4)]}{RESET}\n")
scroll(f"{CYAN}COMPUTER TEMPS: ")
midscroll(f"{TEMPS[random.randint(0,4)]}{RESET}\n")