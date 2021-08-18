#setup script for debian 11 bullseye (works on pretty much every distro if its a debian/ubuntu you get the point base)
#made for my school, they want me to setup debian on the pcs and shit but im too lazy to do it manually
#coded by KrisIsHere

import sys
import os

build = "2.1"

if os.getuid():
    exit("Script By KrisIsHere | Built " + build + "\n\nroot access required\n")
else:
    os.system("clear")
    xd = input("Script By KrisIsHere | Built " + build + "\n\nScript Starting Press 'y' To Continue: ")
    if xd == "y":
        os.system("rm -rf /etc/apt/sources.list ; cp -r sources.list /etc/apt/ ; apt update ; apt upgrade ; apt install htop neofetch ; gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'")
        print("\nSetup finished!")
        sys.exit()
    else:
        print("\nScript Stopped\n")
        sys.exit()
