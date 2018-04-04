# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os	

if len(sys.argv) > 1:
	serial = sys.argv[1]
	dut = fmbtandroid.Device(serial) 
	print("Device            = " + serial)
	if (serial) == "BUC4C16727006201":
		print("HUAWEI is connected, related scripts will be executed")
		execfile(r'C:\TestStand AIVI\fMBT\Huawei\CheckUnPairing.py')
		
	if (dut.serialNumber) == "04cdda6a00747559":
		print("Nexus is connected, related scripts will be executed")
		execfile(r'C:\TestStand AIVI\fMBT\Nexus_5\CheckUnPairing.py')

else:
	print("No serial specified, First One will be connected !") 
	dut = fmbtandroid.Device()
	print("Device            = " + dut.serialNumber)
	
	if (dut.serialNumber) == "BUC4C16727006201":
		print("HUAWEI is connected, related scripts will be executed")
		execfile(r'C:\TestStand AIVI\fMBT\Huawei\CheckUnPairing.py')

	if (dut.serialNumber) == "04cdda6a00747559":
		print("Nexus is connected, related scripts will be executed")
		execfile(r'C:\TestStand AIVI\fMBT\Nexus_5\CheckUnPairing.py')


print "sucess"
os.system("adb.exe kill-server")

sys.exit(0)