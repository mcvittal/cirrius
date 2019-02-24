#!/usr/bin/env python3

import urllib.request, os
from sys import platform
import subprocess as commands

urllib.request.urlretrieve("http://alexmcvittie.me/htv3/desktop.png", "/tmp/htv.png")
os.system("gsettings set org.gnome.desktop.background picture-uri file:///tmp/htv.png")

'''
if (platform == "linux" or platform == "linux2"):
else if (platform == "windows" or platform == "nt"):
    import ctypes
    urllib.request.urlretrieve("http://alexmcvittie.me/htv3/desktop.png", "htv.png")
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "htv.jpg" , 0)

else:
    print("Not supported on your platform")
'''