# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions  import __Check__, __Init__, PressButton, __killADB__, TapOnBitMap, __EnableBluetooth__, Pairing, LoadVCF, DeleteMusic, DeleteImage, LoadImage, LoadMusic, setIntent



dut = __Init__()

PressButton(dut, "Home")
__Check__(dut, "Home")

setIntent(dut, "SettingsMenu")
__Check__(dut, "Check_SettingsMenu")

while(not __Check__(dut,"ComptesGoogle")):
    PressButton(dut,"Swipe")

TapOnBitMap(dut, "ComptesGoogle")
__Check__(dut, "Check_GoogleIcon")

#Deactivate Contact Sync
TapOnBitMap(dut, "GoogleIcon")


#Delete Contacts
setIntent(dut, "DeleteAllContacts")
setIntent(dut, "DisplayPhonebook")
__Check__(dut, "DeleteAllContacts")

#Load Media Files
LoadImage(dut)
LoadMusic(dut)
LoadVCF(dut)

PressButton(dut, "Home")
__Check__(dut, "Home")

__killADB__(dut)