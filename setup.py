#setup script for debian 10 buster (works on pretty much every distro if its a debian/ubuntu you get the point base)
#made for my school, they want me to setup debian on the pcs and shit but im too lazy to do it manually
#coded by KrisIsHere
#DO NOT STEAL WITHOUT CREDIT

import sys
import os
import time

build = "1.2"

if os.getuid():
    print("Script By KrisIsHere | Built " + build)
    exit('\nroot access required\n')
else:
    os.system("clear")
    print("Script By KrisIsHere | Built " + build + "\n")
    xd = input("Script Starting Press 'y' To Continue: ")
    if xd == "y":
        os.system("rm -rf /etc/apt/sources.list")
        os.system("cp -r sources.list /etc/apt/")
        os.system("apt update")
        os.system("apt upgrade")
        os.system("apt install htop neofetch")
        print("\nSetup finished!")
        sys.exit()
    else:
        print("\nScript Stopped\n")
        sys.exit()
