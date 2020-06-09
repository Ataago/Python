x = input("please enter yes or no: ").lower()


if x == "yes" or x == 'y':
    print("Game Loading...")
elif x == "no" or x == 'n':
    print("Exiting game...")
else:
    print("Invalid input")