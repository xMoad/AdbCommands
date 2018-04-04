# -*- coding: utf-8 -*-
import time
import fmbtandroid
import sys
import os
from subprocess import call

#####################################################################################################################################
#####################################################################################################################################

#Function to initialize connection to device with or without SerialNumer, including reading the ini files that contains paths
def __Init__():
    if len(sys.argv) > 1:
        serial = sys.argv[1]
        if serial == "04cdda6a00747559":
            dut = fmbtandroid.Device(iniFile=file("C:/TestStand AIVI/fMBT/mydevice_Nexus5.ini"))

        elif serial == "014f76028b4825f3":
            dut = fmbtandroid.Device(iniFile=file("C:/TestStand AIVI/fMBT/mydevice_Nexus5X.ini"))
        print("Device            = " + serial)
    else:
        print("No serial specified, First One will be connected !") 
        dut = fmbtandroid.Device()
        if dut.serialNumber == "04cdda6a00747559":
            dut = fmbtandroid.Device(iniFile=file("C:/TestStand AIVI/fMBT/mydevice_Nexus5.ini"))

        elif dut.serialNumber == "014f76028b4825f3":
            dut = fmbtandroid.Device(iniFile=file("C:/TestStand AIVI/fMBT/mydevice_Nexus5X.ini"))
        print("Device            = " + dut.serialNumber)
    return dut

#####################################################################################################################################
#####################################################################################################################################

#Function to check the expected behavior
def __Check__(sut, bitMapToVerify):
    sut.refreshScreenshot()
	
    if bitMapToVerify == "BluetoothActivated":
        result = sut.verifyBitmap("Nexus_5_BluetoothIconActivated.png")	
        result1 = sut.verifyBitmap("Nexus_5_BluetoothIconActivatedAppaired.png")
        if result | result1 :
            print("Bluetooth activated successfully")
            return True
        if not result | result1:
            print("Error, bluetooth is not activated or not appaired")
            return False
	
	elif bitMapToVerify == "BluetoothDeactivated":
	    result = sut.verifyBitmap("Nexus_5_BluetoothDeactivated.png")
        if result:
            print("Bluetooth is Deactivated")
            return True
        if not result:
            print("Bluetooth is not Deactivated")
            return False
	
    elif bitMapToVerify == "Home":
        result = sut.verifyBitmap("Nexus_5_Home.png")	
        if result:
            print("Home View is displayed")
            return True
        if not result:
            print("Home View not displayed")
            return False	

    elif bitMapToVerify == "BluetoothAppaired":
        result = sut.verifyBitmap("Nexus_5_BluetoothIconActivatedAppaired.png")
        if result:
            print("Bluetooth is Appaired")
            return True
        if not result:
            print("bluetooth is not appaired")
            return False

    elif bitMapToVerify == "BluetoothNotAppaired":
        result = sut.verifyBitmap("Nexus_5_BluetoothIconActivated.png")
        result1 = sut.verifyBitmap("Nexus_5_BluetoothIconNotDisplayed.png")
        if result | result1:
            print("Nexus_5 is not appaired")
            return True
        if not (result | result1):
            print("Nexus_5 is still appaired")
            return False
	
    elif bitMapToVerify == "DeleteAllContacts":
        result = sut.verifyBitmap("Nexus_5_EmptyPhonebook.png")
        if result:
            print("All contacts have been deleted")
            return True
        if not result: 
            print("Contacts have not been deleted")
            return False

    elif bitMapToVerify == "SetBattery":
        result = sut.verifyBitmap("Nexus_5_SetBatteryTo5.png")
        if result:
            print("Battery is set to level 5")
            return True
        if not result:
            print("Battery level wasn't set correctly")
            return False
			
    elif bitMapToVerify == "UnsetBattery":
        result = sut.verifyBitmap("Nexus_5_UnsetBattery.png")
        if result:
            print("Battery level was unset to original value")
            return True
        if not result:
            print("Battery level wasn't Unset correctly")
            return False
			
    elif bitMapToVerify == "PI16TCRWH004982":
        result = sut.verifyBitmap("Nexus_5_PI16TCRWH004982.png")
        if result:
            print("Head Unit PI16TCRWH004982 is founded in bluetooth Menu")
            return True
        if not result:
            PressButton(sut, "Swipe")
            print("Head Unit PI16TCRWH004982 is not founded in bluetooth Menu")
            return False
			
    elif bitMapToVerify == "PI15TCRMH501946":
        result = sut.verifyBitmap("Nexus_5_PI15TCRMH501946.png")
        if result:
            print("Head Unit PI15TCRMH501946 is founded in bluetooth Menu")
            return True
        if not result: 
            print("Head Unit PI15TCRMH501946 is not founded in bluetooth Menu")
            return False
			
    elif bitMapToVerify == "Associate":
        result = sut.verifyBitmap("Nexus_5_AssociatePhonePopUp_CallLog.png")
        if result:
            print("PopUp to associate Phone to Head Unit is displayed")
            return True
        if not result: 
            print("No PopUp to associate Phone is displayed")
            return False

    elif bitMapToVerify == "LaunchSPVR":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_SPVRLaunched.png")
        if result:
            print("SPVR launched succesufully!")
            return True
        if not result: 
            print("SPVR cannot be launched")
            return False

    elif bitMapToVerify == "MusicPlayer":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_MusicPlayer.png")
        if result:
            print("Music Player is Launched succesufully!")
            return True
        if not result: 
            print("Music Player cannot be launched")
            return False

    elif bitMapToVerify == "ContactOptions":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_ContactOptions.png")
        if result:
            print("Contact Options is Displayed succesufully!")
            return True
        if not result: 
            print("Contact Options cannot be displayed")
            return False
			
    elif bitMapToVerify == "ContactParameters":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_ContactParameters.png")
        if result:
            print("Contact Parameters is Displayed succesufully!")
            return True
        if not result: 
            print("Contact Parameters cannot be displayed")
            return False
			
    elif bitMapToVerify == "Check_ImportPopUp":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_ImportPopUp.png")
        if result:
            print("Import PopUp is Displayed succesufully!")
            return True
        if not result: 
            print("Import PopUp cannot be displayed")
            return False
			
    elif bitMapToVerify == "Check_ImportMenu":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_ImportMenu.png")
        if result:
            print("Import Menu is Displayed succesufully!")
            return True
        if not result: 
            print("Import Menu cannot be displayed")
            return False
			
    elif bitMapToVerify == "Check_SettingsMenu":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_SettingsMenu.png")
        if result:
            print("Settings Menu is Displayed succesufully! ==> Check ")
            return True
        if not result: 
            print("Import Menu cannot be displayed")
            return False
			
    elif bitMapToVerify == "ComptesGoogle":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_ComptesGoogle.png")
        if result:
            print("Compte Menu is Displayed succesufully! ==> Check ")
            return True
        if not result: 
            print("Import Menu cannot be displayed")
            return False
			
    elif bitMapToVerify == "Check_ComptesGoogle":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_GoogleIcon.png")
        if result:
            print("Compte Menu is Displayed succesufully! ==> Check ")
            return True
        if not result: 
            print("Import Menu cannot be displayed")
            return False

    elif bitMapToVerify == "Check_GoogleSync":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_Check_GoogleSync.png")
        if result:
            print("Compte Menu is Displayed succesufully! ==> Check ")
            return True
        if not result: 
            print("Import Menu cannot be displayed")
            return False
			
    elif bitMapToVerify == "importSource":
        time.sleep(3)
        result = sut.verifyBitmap("Nexus_5_InternalStorage.png")
        if result:
            print("Import Source Menu is Displayed succesufully! ==> Check ")
            return True
        if not result: 
            print("Import Source Menu cannot be displayed")
            return False
#####################################################################################################################################
#####################################################################################################################################
			
#Function to Press Button 
def PressButton(sut, ButtonToPress):
    sut.refreshScreenshot()
    if ButtonToPress == "Home":
        print("Access Home Page")
        sut.pressHome()
        time.sleep(5)
        sut.refreshScreenshot()
        return True
		
    elif ButtonToPress == "EndCall":
        print("Call ended")
        sut.pressKey("ENDCALL")
        time.sleep(5)
        sut.refreshScreenshot()
        return True
		
    elif ButtonToPress == "BluetoothMenu":
        print("Access to bluetooth Menu")
        sut.shell("am start -a android.settings.BLUETOOTH_SETTINGS")
        time.sleep(5)
        sut.refreshScreenshot()
        return True
		
    elif ButtonToPress == "Swipe":
        print("Execute a swipe")
        sut.shell("input touchscreen swipe 800 800 50 50")
        time.sleep(5)
        sut.refreshScreenshot()
        return True
		
    elif ButtonToPress == "Associer":
        print("Tap On Associer Button")
        whatISee = sut.waitAnyBitmap(["Nexus_5_AssociateButton.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_AssociateButton.png")	
            if result:
                print("Tap on Associer Button")
                return True
            if not result | result1:
                print("Error, Associer button is not displayed any more")
                return False
        
#####################################################################################################################################
#####################################################################################################################################    

#Function to enable Bluetooth
def __EnableBluetooth__(sut):
    dut = sut
    print("PopUp to activate Bluetooth ==> Request Enable")
    dut.shell ("am start -a android.bluetooth.adapter.action.REQUEST_ENABLE") #Activate BT
    time.sleep(5)
    dut.refreshScreenshot()
#Selection/Activation by Key Event 
    print("Enable Bluetooth by Key Event")
    dut.shell("input keyevent 23") #Key event for center => DPAD_CENTER
    time.sleep(1)
    dut.shell("input keyevent 22") #Key event for right => DPAD_RIGHT
    time.sleep(1)
    dut.shell("input keyevent 66") #Key event for enter => KEYCODE_ENTER
    time.sleep(10)
    dut.refreshScreenshot()

	
#####################################################################################################################################
#####################################################################################################################################


#Function to stop/kill ADB
def __killADB__(sut):
    os.system('adb.exe kill-server')#sut.shell("adb kill-server") #Battery Init State
    time.sleep(5)
    return True
	
#####################################################################################################################################
#####################################################################################################################################	
    
#Function to Tap on appropriate bitMap	
def TapOnBitMap(sut, BitMapToTap):
    sut.refreshScreenshot()
	
    if BitMapToTap == "BluetoothActivated":
        whatISee = sut.waitAnyBitmap(["Nexus_5_BluetoothIconActivated.png"]) 
        whatISee1 = sut.waitAnyBitmap(["Nexus_5_BluetoothIconActivatedAppaired.png"])
        if whatISee | whatISee1:
            result = sut.tapBitmap("Nexus_5_BluetoothIconActivated.png")	
            result1 = sut.tapBitmap("Nexus_5_BluetoothIconActivatedAppaired.png")
            if result | result1 :
                print("Bluetooth activated successfully")
                return True
            if not result | result1:
                print("Error, bluetooth is not activated or not appaired")
                return False
	    if not (whatISee | whatISee1):
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "BluetoothDeactivated":
        whatISee = sut.waitAnyBitmap(["Nexus_5_BluetoothDeactivated_Button.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_BluetoothDeactivated_Button.png")
            if result:
                print("Bluetooth is Deactivated")
                return True
            if not result:
                print("Bluetooth is not Deactivated")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "PI16TCRWH004982":
        whatISee = sut.waitAnyBitmap(["Nexus_5_PI16TCRWH004982.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_PI16TCRWH004982.png")
            if result:
                print("Starting association with the Head Unit PI16TCRWH004982")
                return True
            if not result:
                print("Cannot Start association with the Head Unit PI16TCRWH004982")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
 
    elif BitMapToTap == "PI15TCRMH501946":
        whatISee = sut.waitAnyBitmap(["Nexus_5_PI15TCRMH501946.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_PI16TCRWH004982.png")
            if result:
                print("Starting association with the Head Unit PI15TCRMH501946")
                return True
            if not result:
                print("Cannot Start association with the Head Unit PI15TCRMH501946")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "Associate":
        whatISee = sut.waitAnyBitmap(["Nexus_5_AssociatePhonePopUp_CallLog.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_AssociatePhonePopUp_CallLog.png")
            if result:
                print("Association accepted to the Head Unit")
                return True
            if not result:
                print("Association cannot be done")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False

    elif BitMapToTap == "LaunchSPVR":
        whatISee = sut.waitAnyBitmap(["Nexus_5_LaunchSPVR.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_LaunchSPVR.png")
            if result:
                print("SPVR Launched")
                return True
            if not result:
                print("Cannot launch SPVR")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "ContactsMenu":
        whatISee = sut.waitAnyBitmap(["Nexus_5_ContactIcon.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_ContactIcon.png")
            if result:
                print("Contact Menu is displayed")
                return True
            if not result:
                print("Cannot display Contact Menu")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "Phonebook":
        whatISee = sut.waitAnyBitmap(["Nexus_5_PhonebookIcon.png"])
        if whatISee:
            result = sut.tapBitmap("Nexus_5_PhonebookIcon.png")
            if result:
                print("Phonebook is displayed")
                return True
            if not result:
                print("Cannot display Phonebook")
                return False
        if not whatISee:
            print("Cannot found the right BitMap Image")
            return False
			
    if BitMapToTap == "ContactOptions":
        whatISee = sut.waitAnyBitmap(["Nexus_5_ContactOptions.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_ContactOptions.png")	
            if result:
                print("Contact options is displayed successfully")
                return True
            if not result:
                print("Contact options is not displayed")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "ContactParameters":
        whatISee = sut.waitAnyBitmap(["Nexus_5_ContactParameters.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_ContactParameters.png")	
            if result:
                print("Contact Parameters is displayed successfully")
                return True
            if not result:
                print("Error, Contact Parameters is not displayed ")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False

    elif BitMapToTap == "ContactImport":
        whatISee = sut.waitAnyBitmap(["Nexus_5_ContactImport.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_ContactImport.png")	
            if result:
                print("Import option is tapped successfully")
                return True
            if not result:
                print("Error, Cannot tap contact import option.")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "TapVCF":
        whatISee = sut.waitAnyBitmap(["Nexus_5_TapOnVCF.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_TapOnVCF.png")	
            if result:
                print("Import option is displayed is displayed successfully")
                return True
            if not result:
                print("Error, Contact Parameters is not displayed ")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "Tap_1000Contacts":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_1000Contacts.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_1000Contacts.png")	
            if result:
                print("1000Contacts will be imported")
                return True
            if not result:
                print("Error, Cannot tap 1000Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
									
    elif BitMapToTap == "Tap_2000Contacts":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_2000Contacts.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_2000Contacts.png")	
            if result:
                print("2000Contacts will be imported")
                return True
            if not result:
                print("Error, Cannot tap 2000Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
						
    elif BitMapToTap == "Tap_4000Contacts":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_4000Contacts.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_4000Contacts.png")	
            if result:
                print("4000Contacts will be imported")
                return True
            if not result:
                print("Error, Cannot tap 4000Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "Tap_DefaultContacts":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_DefaultContacts.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_DefaultContacts.png")	
            if result:
                print("Defaults Contacts will be imported")
                return True
            if not result:
                print("Error, Cannot tap Defaults Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False
			
    elif BitMapToTap == "Tap_Device1":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_Device1.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_Device1.png")	
            if result:
                print("Device1 will be imported")
                return True
            if not result:
                print("Error, Cannot tap Device1 Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			
			
    elif BitMapToTap == "Tap_Device2":
        whatISee = sut.waitAnyBitmap(["Nexus_5_VCF_Device2.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_VCF_Device2.png")	
            if result:
                print("Device2 will be imported")
                return True
            if not result:
                print("Error, Cannot tap Device2 Contacts Card")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			
			
    elif BitMapToTap == "ComptesGoogle":
        whatISee = sut.waitAnyBitmap(["Nexus_5_ComptesGoogle.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_ComptesGoogle.png")	
            if result:
                print("Tap on Comptes Google!")
                return True
            if not result:
                print("Error, Cannot tap on Comptes Google")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			
			
    elif BitMapToTap == "GoogleIcon":
        whatISee = sut.waitAnyBitmap(["Nexus_5_Check_GoogleIcon.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_Check_GoogleIcon.png")	
            if result:
                print("Tap on Comptes Google!")
                return True
            if not result:
                print("Error, Cannot tap on Comptes Google")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			
		
    elif BitMapToTap == "GoogleSync":
        whatISee = sut.waitAnyBitmap(["Nexus_5_Check_GoogleSync.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_Check_GoogleSync.png")	
            if result:
                print("Tap on Comptes Google!")
                return True
            if not result:
                print("Error, Cannot tap on Comptes Google")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			

    elif BitMapToTap == "importSource":
        whatISee = sut.waitAnyBitmap(["Nexus_5_Check_ImportMenu.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_Check_ImportMenu.png")	
            if result:
                print("Tap on Open Directory")
                return True
            if not result:
                print("Error, Cannot tap on Open Directory")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False

    elif BitMapToTap == "importSourceInternal":
        whatISee = sut.waitAnyBitmap(["Nexus_5_InternalStorage.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_InternalStorage.png")	
            if result:
                print("Tap on Open Directory")
                return True
            if not result:
                print("Error, Cannot tap on Open Directory")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			
			
    elif BitMapToTap == "TapDownloadFolder":
        whatISee = sut.waitAnyBitmap(["Nexus_5_DownloadFolder.png"]) 
        if whatISee:
            result = sut.tapBitmap("Nexus_5_DownloadFolder.png")	
            if result:
                print("Tap on Download Directory")
                return True
            if not result:
                print("Error, Cannot tap on Download Directory")
                return False
	    if not whatISee:
		    print("Cannot found the right BitMap Image")
            return False			

#####################################################################################################################################
#####################################################################################################################################
			
#Function to invoke an Intent
def setIntent(sut, Command):
    sut.refreshScreenshot()
    if Command == "DeleteAllContacts":
        print("Delete all contacts from Phonebook")
        sut.shell("pm clear com.android.providers.contacts")
        sut.refreshScreenshot()
        time.sleep(5)
        return True 

    elif Command == "DisplayPhonebook":
        print("Display Phonebook")
        #sut.shell("am start -a android.intent.action.MAIN -p com.google.android.contacts")
        sut.shell("input keyevent 207")
        sut.refreshScreenshot() 
        time.sleep(5)
		
        return True 
		
    elif Command == "SetBattery":
        print("Set battery Level to 5")
        sut.shell("dumpsys battery set level 5")
        sut.refreshScreenshot() 
        time.sleep(5)
        return True 
	
    elif Command == "UnsetBattery":
        print("Set battery level to init level")
        sut.shell("dumpsys battery reset")
        sut.refreshScreenshot()
        time.sleep(5)
        return True

    elif Command == "PlayMusic":
        print("Play the following Track: USA_T01_240Hz.mp3")
        sut.shell("")
		
    elif Command == "SettingsMenu":
        print("Display Settings Menu")
        sut.shell("am start -a android.settings.SETTINGS")
        sut.refreshScreenshot()
        time.sleep(5)
        return True
#####################################################################################################################################
#####################################################################################################################################

		
def SendSMS(sut, number, text):
    print("Command to Send SMS")
    sut.shell("am start -a android.intent.action.SENDTO -d sms:"+number+" --es sms_body "+text+" --ez exit_on_sent true")
    print("Execute Push button to send SMS")
    time.sleep(10)
    sut.shell("input touchscreen tap 945 1670")
    time.sleep(5)
    sut.refreshScreenshot()
    return True 

#####################################################################################################################################
#####################################################################################################################################
	

def PlayMusic(sut, TrackName):
    print("Command to Play Music")
    sut.shell("am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Music/"+TrackName+" -t audio/mp3")
    print("Music Player is displayed and Music is played")
    time.sleep(10)
    sut.refreshScreenshot()
    return True
	
#####################################################################################################################################
#####################################################################################################################################

	
def Pairing(sut, HUName):    
    sut.refreshScreenshot()
    boolVar = __check__(sut, HUName)
    result = sut.verifyOcrText(HUName)
    if result:
        assert sut.tapOcrText(HUName), "Cannot Tap on"+HUName+" Device"

    if not (result | boolVar):
        sut.tapOcrText(HUName)
    #    sut.PressButton(
    print("Don't found, continue searching by swipe 1")
    print("Don't found, continue searching by swipe 1")
    sut.shell("input touchscreen swipe 800 800 50 50")
    sut.refreshScreenshot()
    time.sleep(20)
    if sut.verifyOcrText(HUName):
        sut.tapOcrText(HUName)
		
    print("Don't found, continue searching by swipe 2")
    sut.shell("input touchscreen swipe 800 800 50 50")
    sut.refreshScreenshot()
    time.sleep(20)
    if sut.verifyOcrText(HUName):
        sut.tapOcrText(HUName)
    print("Search for Autoriser... Button")
    sut.refreshScreenshot()
    result = sut.verifyOcrText("Autoriser MYCAR à accéder à vos contacts et au journal d'appel")
    if result:
        assert sut.tapOcrText("Autoriser MYCAR à accéder à vos contacts et au journal d'appel"), "Could not found button Autoriser"
		
#####################################################################################################################################
#####################################################################################################################################

def LoadVCF(sut):
    sut.refreshScreenshot()
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Device1.vcf /storage/emulated/0/Download')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Device2.vcf /storage/emulated/0/Download')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Default_Contacts.vcf /storage/emulated/0/Download')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/4000Contacts.vcf /storage/emulated/0/Download')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/2000Contacts.vcf /storage/emulated/0/Download')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/1000Contacts.vcf /storage/emulated/0/Download')
	

def LoadImage(sut):
    sut.refreshScreenshot()
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE1.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE2.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE3.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE4.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE5.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE6.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE7.jpg /storage/emulated/0/Pictures')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Image/IMAGE8.jpg /storage/emulated/0/Pictures')
	
	
def LoadMusic(sut):
    sut.refreshScreenshot()
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/NomPiste3_Error.mp3 /storage/emulated/0/Music')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T01_240Hz.mp3 /storage/emulated/0/Music')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T02_260Hz.mp3 /storage/emulated/0/Music')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T03_280Hz.mp3 /storage/emulated/0/Music')
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T04_300Hz.mp3 /storage/emulated/0/Music')	
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T05_320Hz.mp3 /storage/emulated/0/Music')	
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T06_340Hz.mp3 /storage/emulated/0/Music')	
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T07_360Hz.mp3 /storage/emulated/0/Music')	
    os.system('adb push C:/"TestStand AIVI"/fMBT/InitFiles/Music/USA_T08_380Hz.mp3 /storage/emulated/0/Music')	
	
	
#####################################################################################################################################
#####################################################################################################################################		

def DeleteMusic(sut):
    sut.refreshScreenshot()
    sut.shell("rm -r /storage/emulated/0/Music/")

#####################################################################################################################################
#####################################################################################################################################		

def DeleteImage(sut):
    sut.refreshScreenshot()
    sut.shell("rm -r /storage/emulated/0/Image/")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    

