#
# fMBT use cases for TENV-AR1 PoC
#

import time

def UseCase1(dut):
    """
    Use case 1   : Bluetooth pairing
    Pre-requisite: a 2nd DUT is in range and ready to accept pairing

	'dut' parameter is the Android device to exercize.
	"""

    # Bluetooth device name
    bt_device = "MYCAR"

    print("Launch Settings - Bluetooth app")
    dut.shell("am start -a android.Telephony.Sms)
	#settings.BLUETOOTH_SETTINGS")
    time.sleep(10)
    dut.refreshScreenshot()
    if not dut.verifyOcrText("Bluetooth"):
        raise Exception("Launch Settings - Bluetooth app - STEP FAILED")
        return 1

    """print("Turn Bluetooth on and proceed with discovery")
    if dut.verifyOcrText("Off"):
        result = dut.tapOcrText("Off")
        time.sleep(20)
    dut.refreshScreenshot()
    if not dut.verifyOcrText("On"):
        raise Exception("Turn Bluetooth on and proceed with discovery - STEP FAILED")
        return 1"""

    print("Pair with %s" % bt_device)
    result = dut.tapOcrText(bt_device)
    time.sleep(5)
    dut.refreshScreenshot()
    if not result:
        raise Exception("Pair with %s - STEP FAILED" % bt_device)
        return 1

    print("Press PAIR")
    result = dut.tapOcrText("PAIR")
    time.sleep(1)
    dut.refreshScreenshot()
    if not result:
        raise Exception("Press PAIR - STEP FAILED")
        return 1

    print("Use case 1 - Bluetooth pairing - DONE\n\n")
    return 0

def UseCase2(dut):
    """
    Use case 2   : Play audio
    Pre-requisite: a sample audio file was pushed to the DUT

	'dut' parameter is the Android device to exercize.
	"""

    # TODO: the output sound should be captured to verify the test
    print("Play an audio media")
    dut.pressKey("MEDIA_PLAY")
    time.sleep(1)
    dut.refreshScreenshot()

    print("Use case 2 - Play audio - DONE\n\n")
    return 0
