
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
    else:
        print("Uhh ok lets do another one anyway! :)")