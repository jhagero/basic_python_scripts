
print("Oh hello there!")
name = str(input("What's your name? "))
print(f"Nice to meet you, {name}")
food = input("What do you want for dinner?: ")

if food == "Pizza":
    print(f'Oh, I like {food.lower()} too!')
if food.lower() == "Steak".lower():
    print(f'{food.title()} is my favorite!')
else:
    print(f'Never heard of it...')
