# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __Check__, __Init__, __HomeButton__, __EnableBluetooth__, __killADB__, SendSMS, setIntent

dut = __Init__()
__HomeButton__(dut)
__Check__(dut, "Home") 
setIntent(dut, "UnsetBattery")
__Check__(dut, "UnsetBattery") 
__killADB__(dut)
 

os.system("adb.exe kill-server")
sys.exit(0)