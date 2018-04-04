# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from Functions import __Check__, __Init__, __HomeButton__, __EnableBluetooth__, __killADB__, SendSMS

num = str(sys.argv[2])
texte = str(sys.argv[3])

dut = __Init__()
__HomeButton__(dut)
__Check__(dut, "Home")
SendSMS(dut, num, texte)
__killADB__(dut)









#dut.shell("input keyevent 22") #Key event for right
#dut.shell("input keyevent 66") #Key event for	 enter


#dut.shell("am start -a android.intent.action.SENDTO -d sms:... --es sms_body SMS BODY GOES HERE --ez exit_on_sent true")
#dut.shell("am start -a android.intent.action.SENDTO -d sms:"+Nb+" --es sms_body "+Message+" --ez exit_on_sent true")
#am start -a android.intent.action.SENDTO -d sms:... --es sms_body \"HelloW\" --ez exit_on_sent true")
#dut.shell("am start -a android.intent.action.SENDTO -d sms:0650561783 --es sms_body "Hello" --ez exit_on_sent true")
	
#dut.shell("am start -a android.intent.action.SENDTO -d sms:0650561783 --es sms_body \"Test\" --ez exit_on_sent true")

#dut.smsNumber(Nb, Message)
 

# dut.shell("am start -a android.intent.action.SENDTO -d sms:... --es sms_body \"Test\" --ez exit_on_sent true")
# dut.shell("service call isms 6 s16 \"...\" i32 0 i32 0 s16 \"SMS TEXT HERE\"")
# time.sleep(2)
# dut.shell("input keyevent 22") #Key event for right
# time.sleep(1)
# dut.shell("input keyevent 22") #Key event for right
# time.sleep(1)
# dut.shell("input keyevent 66") #Key event for	 enter
# time.sleep(2)
