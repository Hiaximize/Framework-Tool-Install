#!/usr/bin/env python3

import subprocess
import os
#import fileinput

print("This script will help you update the necessary configuration files"
      " to get tor started, but also install the frameworks")

print("")
print("[+] Performing basic update and upgrade plus full upgrade functions")
print("")

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newpath):
        self.newpath = os.path.expanduser(newpath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newpath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def install_beelogger():
    with cd("~/"):
        print("[-] Installing BeeLogger in your root directory")
        subprocess.call("git clone https://github.com/4w4k3/BeeLogger.git", shell=True)
        with cd("BeeLogger/"):
            subprocess.call("./install.sh", shell=True)
            print("[+] BeeLogger is now installed in root directory")


def install_thefatrat():
    with cd("~/"):
        print("")
        print("[-] Installing TheFatRat to root directory")
        print("")
        subprocess.call("git clone https://github.com/Screetsec/TheFatRat.git", shell=True)
        with cd("TheFatRat/"):
            subprocess.call("chmod +x setup.sh", shell=True)
            subprocess.call("./setup.sh", shell=True)
            print("")
            print("[+] TheFatRat is now installed in the root directory")

def install_empire():
    with cd("~/"):
        print("")
        print("[-] Installing Empire to root directory")
        print("")
        subprocess.call("git clone https://github.com/EmpireProject/Empire.git", shell=True)
        with cd("Empire/setup"):
            subprocess.call("chmod +x install.sh", shell=True)
            subprocess.call("./install.sh", shell=True)
            print("")
            print("[+] Empire is now installed in the root directory")


def install_lazagne():
    with cd("~/"):
        print("")
        print("[-] Installing LaZagne to root directory")
        print("")
        subprocess.call("git clone https://github.com/AlessandroZ/LaZagne.git", shell=True)
        with cd("LaZagne/setup"):
            print("")
            print("[+] LaZagne is now installed in the root directory")


def install_veil_framework():
    with cd("~/"):
        print("")
        print("[-] Installing Veil-Framework to root directory")
        print("")
        subprocess.call("git clone https://github.com/gold1029/Veil-Framework-Veil3.0-.git", shell=True)
        with cd("Veil-Framework-Veil3.0-/setup"):
            subprocess.call("chmod +x setup.sh", shell=True)
            subprocess.call("./setup.sh", shell=True)
            print("")
            print("[+] Veil-Framework is now installed in the root directory")


def install_zlogger():
    with cd("~/"):
        print("")
        print("[-] Installing Zlogger to root directory")
        print("")
        subprocess.call("git clone https://github.com/jlemon/zlogger.git", shell=True)
        with cd("ZLogger/"):
            subprocess.call("chmod +x install.sh", shell=True)
            subprocess.call("./install.sh", shell=True)
            print("")
            print("[+] ZLogger is now installed in the root directory")


def installing_and_setup_tor():
    with cd("~/"):
        subprocess.call("clear")
        print('')
        print("[-] Installing tor...")
        subprocess.call("apt-get install tor -y", shell=True)
        subprocess.call("clear", shell=True)
        print("You will need to edit the config file for proxychains in order to be able to tunnel your connection")
        print("through the tor network to further anonymize yourself. Use responsibly!!")
        print("")
        print("")
        print("You will need to erase the '#' from dynamic_chain, and add a '#' to strict_chain. ")
        print("Once you do that, scroll down to the bottom and where it says add proxy here...")
        print("you will need to add the following to the list ensuring you maintain the formatting")
        print("")
        print("socks5   127.0.0.1 9050")
        print("socks5   127.0.0.1 9050")
        print("")
        print("When you are finished save the file and hit the exit button in the top right corner to "
              "move to the next phase of the installation.")
        print("")
        subprocess.call("leafpad /etc/proxychains.conf", shell=True)
        subprocess.call("clear", shell=True)


def install_repository_tools():
    subprocess.call("apt-get install snort -y", shell=True)
    subprocess.call("apt-get install pdas -y", shell=True)
    subprocess.call("apt-get install mitmf -y", shell=True)

def setup_networkmanager():
    print("You will need to change the value from false to true, click the exit button when done")
    subprocess.call("leafpad /etc/NetworkManager/NetworkManager.conf", shell=True)
    subprocess.call("service network-manager restart", shell=True)
    subprocess.call("clear", shell=True)
    print("There is one more thing to do which is quite complicated but hopefully this gets everything up and running "
          "for your network")
    subprocess.call("clear", shell=True)
# def setup_NetworkManager():
#     with cd("/"):
#         with cd("etc/NetworkManager/"):
#             tempfile = open("etc/NetworkManager/NetworkManager.conf", 'r+')
#             for line in fileinput.input("NetworkManager.conf"):
#                 if "true" in line:
#                     print("Current value set to true")
#                     continue
#                 else:
#                     print("Changing value to true")
#                     tempfile.write(line.replace("false", "true"))
#                     tempfile.close()

setup_networkmanager()
#setup_NetworkManager()
installing_and_setup_tor()
install_beelogger()
install_thefatrat()
install_empire()
install_lazagne()
install_veil_framework()
install_zlogger()
install_repository_tools()
subprocess.call("apt-get update && apt-get upgrade -y && apt-get full-upgrade -y && apt-get dist-upgrade -y", shell=True)
