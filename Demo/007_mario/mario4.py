# print("    #")
# print("   ##")
# print("  ###")
# print(" ####")
# print("#####")

x = int(input("Enter a number: "))

for i in range(1, x + 1):
    spaces = (x - i)
    print(" " * spaces, end="")
    print("#" * i)