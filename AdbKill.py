# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __killADB__, __Init__

dut = __Init__()
__killADB__(dut)

os.system("adb.exe kill-server")
sys.exit(0)