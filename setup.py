#setup script for debian 10 buster (works on pretty much every distro if it debian/ubuntu you get the point base)
#made for my school, they want me to setup debian on the pcs and shit
#coded by KrisIsHere
#DO NOT STEAL WITHOUT CREDIT
import sys
import os

if os.getuid():
    print("Script By KrisIsHere")
    exit('\nroot access required\n')
else:
    os.system("clear")
    print("        Script By KrisIsHere")
    xd = input("Script starting press 'y' to continue: ")
    if xd == "y":
        os.system("rm -rf /etc/apt/sources.list")
        os.system("cp -r sources.list /etc/apt/")
        os.system("apt update")
        os.system("apt upgrade")
        os.system("apt install htop neofetch")
        print("\nSetup finished!")
        sys.exit()
    else:
        print("\nStoping script\n")
        sys.exit()
