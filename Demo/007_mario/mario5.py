# print("   # #   ")
# print("  ## ##  ")
# print(" ### ### ")
# print("#### ####")


x = int(input("Please enter a number for pattern: "))

for i in range (1, x + 1):
    print(" " * (x - i) + "#" * i + " " + "#" * i)