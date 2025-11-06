# vin_decoder.py
from vininfo import Vin
import robco_terminal
print = robco_terminal.fallout_print

#vin = Vin("WBA5A7C53FG143210") # Sample VIN

def checkvin(vin = None):
    userfailed = False
    if vin == None or len(vin) < 17:
        vin = str(input("Enter the VIN#: "))
    if len(vin) < 17:
        vin = str(input("Must be 17 digits, try again: "))
        if len(vin) < 17:
            print("Try again later...")
            userfailed = True
    if userfailed != True:
        vin = Vin(vin)
        if vin.verify_checksum():
            print(f"Model Year: {vin.years}")
            print(f"Manufacturer: {vin.manufacturer}")
            print(f'Other information:')
            for attr in dir(vin):
                if not attr.startswith('_'): #skip private stuff
                    value = getattr(vin, attr)
                    if not callable(value): #skip methods
                        print(f"{attr}: {value}")
            print("That's all I got.")

        else:
            print("VIN entered is not valid, try again")
        