#!/usr/bin/python

import os
import sys
from subprocess import call
from Functions  import __Check__, __Init__, PressButton, __killADB__, TapOnBitMap, __EnableBluetooth__, Pairing, LoadVCF, DeleteMusic, DeleteImage, LoadImage, LoadMusic, setIntent



dut = __Init__()

#dut.shell("push C:/TestStand AIVI/fMBT/InitFiles/Device1.vcf /storage/emulated/0/Contact")
#dut.shell("push C:\'TestStand AIVI'\fMBT\InitFiles\Image\IMAGE2.jpg /storage/emulated/0/Pictures/")
#dut.shell("push C:\\TestStand AIVI\\fMBT\\InitFiles\\Music\\USA_T01_240Hz.mp3 /storage/emulated/0/Music")

os.system('adb shell rm -r /storage/emulated/0/Pictures/')
os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE1.jpg /storage/emulated/0/Pictures')
# print 'Number of arguments', len(sys.argv), 'arguments.'
# print 'Argument List', str(sys.argv)

# print 'totot=' , str(sys.argv[0])
# print 'totot=' , str(sys.argv[1])
# print 'totot=' , str(sys.argv[2])