import os
import time
import sys

os.system("clear")

logo = """\033[32m

╔══╦══╦══╦╗╔╗╔══╦═╦═╦╗
║╔═╣╔╗╠╗╔╣╚╝║╚╗╔╣║║║║║
║╚╗║╠╣║║║║╔╗║─║║║║║║║╚╗
╚══╩╝╚╝╚╝╚╝╚╝─╚╝╚═╩═╩═╝                                                  """
print (logo)
time.sleep(1.0)
print ()

logo1 = """\033[32m+--------------------------------------------+
| This Tool Get Help of Main Termux Packages |
+--------------------------------------------+
| Coded By Ranuja  | version : 1.0           |
+--------------------------------------------+"""
print (logo1)


time.sleep(1.0)

def tprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

print ()

tprint('''\033[32m
[01] python - 1
[02] nmap - 2
[03] ruby - 3
[04] php - 4
[05] java - 5
[06] macchanger - 6''')

tprint('''\033[32m
[+] athal ekata gapu tulak bocca!''')

chs = input("[+] Enter Choice : ")

if chs == '1' : os.system("python -h")
if chs == '2' : os.system("nmap -h")
if chs == '3' : os.system("ruby -h")
if chs == '4' : os.system("php -h")
if chs == '5' : os.system("java -h")
if chs == '6' : os.system("macchanger -h")

else:
	print ()
	print ("Thanks for using!")
	print ()
	sys.exit
