# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __Init__, __killADB__



dut = __Init__()


dut.pressKey("MEDIA_PLAY")
dut.close()
__killADB__(dut)

	
os.system("adb.exe kill-server")
sys.exit(0)
