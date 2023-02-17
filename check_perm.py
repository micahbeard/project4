import os
import sys


def check(): 
    print("/passwd Dir\nShould have -rw-r--r--")
    os.system('ls -l /etc/passwd')
    print("/shadow Dir\nShould have -rw-r-----")
    os.system('ls -l /etc/shadow')
    print("/services Dir\nShould have -rw-r--r--")
    os.system('ls -l /etc/services')
    print("/home Directory\nShould have drwxr-x---")
    os.system('ls -l /home')

    perms = input("Reset Perms to Default?\n1:Yes Any key to Exit")
    if perms == "1":
        os.system('sudo chmod 644 /etc/passwd')
        os.system('sudo chmod 640 /etc/shadow')
        os.system('sudo chmod 644 /etc/services')
        os.system('sudo chmod 710 /home')
    else:
        return