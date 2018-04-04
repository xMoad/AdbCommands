# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __Check__, __Init__, PressButton, __EnableBluetooth__, __killADB__, setIntent

NbToCall = str(sys.argv[2])

dut = __Init__() 
dut.callNumber(NbToCall)
__killADB__(dut)

os.system("adb.exe kill-server")
sys.exit(0)