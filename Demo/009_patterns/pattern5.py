# print Even numbers

n = int(input("Enter number: "))

for i in range(2, n + 1, 2):        # range(start, stop, step)
    print(i, end=" ")

print()