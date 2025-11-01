# vin_decoder.py
from vininfo import Vin


vin = Vin("WBA5A7C53FG143210")
vin = Vin("00000000000000000")

manu = vin.manufacturer
modelyear = vin.years
country = vin.country
valid = vin.verify_checksum()

def checkvin(vin = None):
    if vin == None:
        vin = str(input("Enter the VIN#: "))
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
        print("That's all I got, pa'tnah.")

    else:
        print("VIN entered is not valid, try again")
    