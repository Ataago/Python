# print Odd numbers

n = int(input("Enter number: "))

for i in range(1, n + 1, 2):        # range(start, stop, step)
    print(i, end=" ")

print()