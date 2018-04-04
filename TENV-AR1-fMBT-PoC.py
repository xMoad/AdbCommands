import time

import fmbtandroid

import UseCases

# Set Android device serial
serial = "04cdda6a00747559"

# Define Android device object
dut = fmbtandroid.Device(serial)

# Set and enable visual log
log_name = "TENV-AR1-PoC-log"
print("Enable visual log\n")
dut.enableVisualLog("%s.html" % log_name)

def presets():
    """Preset actions are executed before every use case."""

    print("Unlock the device under test")
    dut.swipe((.5, .8), "north")

    print("Press Home key")
    dut.pressHome()
    time.sleep(1)
    dut.refreshScreenshot()
    if not dut.verifyOcrText("YouTube"): # TODO: improve the logics determining if we're in the home screen or not
        raise Exception("Press Home key - preset STEP FAILED")
    return 1

presets()
UseCases.UseCase1(dut)

presets()
UseCases.UseCase2(dut)
