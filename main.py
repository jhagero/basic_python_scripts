import math
import vin
import robco_terminal
print = robco_terminal.fallout_print

e = math.e
# math.sqrt()1
# math.ceil()
# math.floor()

def radiusfunc():
    print()
    radius = float(input('Enter the radius of a circle: '))
    circumference = 2 * math.pi * radius
    print(f"\t\tCircumference is {round(circumference,2)}cm")

def areafunc():
    print()
    radius = float(input('Enter the radius of a circle: '))
    area = math.pi * pow(radius, 2)
    print(f"\t\tArea is: {round(area,2)}cm^2")

def hypotenusefunc():
    print()
    side_a = float(input('Enter side a: '))
    side_b = float(input('Enter side b: '))
    hypotenuse = math.sqrt((pow(side_a, 2) + pow(side_b, 2)))
    print(f"\t\tHypotenuse is {round(hypotenuse,2)}")

def kgstolbsfunc():
    print()
    print("Converting kilograms to pounds is done by multiplying pounds by 2.205.")
    kg = float(input('Enter kgs: '))
    lbs = round(kg * 2.205, 2)
    print(f"\t\t{lbs} lbs!")

def lbstokgsfunc():
    print()
    print("Converting pounds to kilograms is done by dividing pounds by 2.205.")
    lbs = float(input('Enter pounds: '))
    kg = round(lbs / 2.205, 2)
    print(f"\t\t{kg} kilograms! ")

def tempconversionfunc():
    print()
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")
    temp = float(input("What is the temperature?: "))
    if unit == "C":
        temp = round((9 * temp) / 5 + 32, 1)
        print(f"The temperature in Fahrenheit is: {temp}°F")
    elif unit == "F":
        temp = round((temp-32)*5/9,1)
        print(f"The temperature in Celcius is: {temp}°C")
    else:
        print(f"{unit} is not a valid unit of measurement!")

def madlib():
    choice = ""
    while choice != "q":
        if choice == "quit":
            break
        print("Give me some silly words!") 
        adjective1 = input("Enter an adjective (description): ")
        noun1 = input("Enter a noun (person, place, thing): ")
        adjective2 = input("Enter an adjective (description): ")
        verb1 = input("Enter a verb ending with 'ing': ")
        adjective3 = input("Enter an adjective (description): ")

        print(f'Today I went to a {adjective1.lower()} zoo.')
        print(f'In an exhibit, I saw a {noun1.lower()}')
        print(f'{noun1.title()} was {adjective2.lower()} and {verb1.lower()}')
        print(f'I was {adjective3.lower()}!')

        choice = input("Do another one? (y/n): ")
        if choice == "y":
            continue
        if choice == "n" or choice == "q":
            print("Thanks for playing! Bye!")
            break
        else:
            print("Uhh ok lets do another one anyway! :)")

def __main__():
    choice = ""
    while choice != "quit":
        print()
        print("Choose one of the following options:")
        print("(1) Find CIRCUMFERENCE of a circle with known radius")
        print("(2) Find AREA of a circle with known radius")
        print("(3) Find HYPOTENUSE of a triangle with known side a and side b")
        print("(4) To convert pounds to kilogram!")
        print("(5) To convert kilograms to pounds!")
        print("(6) For temperature conversions!")
        print("(7) To check a VIN number!")
        print("(8) For a silly madlib")
        choice = str(input("\tMake choice (q for quit): ")).strip()

        if choice == "1":
            radiusfunc()
        elif choice == "2":
            areafunc()
        elif choice == "3":
            hypotenusefunc()
        elif choice == "4":
            lbstokgsfunc()
        elif choice == "5":
            kgstolbsfunc()
        elif choice == "6":
            tempconversionfunc()
        elif choice == "7":
            vin.checkvin()
        elif choice == "8":
            madlib()
        elif choice.lower() == "q" or choice == "quit":
            print("Thanks for stoppin' by!")
            break
        else:
            print("Invalid input! Enter the number that corresponds to your choice.")

__main__()
