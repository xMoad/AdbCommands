# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __Init__, __killADB__

dut = __Init__()
 
dut.pressKey("Call")

__killADB(dut)

os.system("adb.exe kill-server")
sys.exit(0)s