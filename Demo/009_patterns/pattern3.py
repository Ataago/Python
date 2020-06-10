# print Odd numbers

n = int(input("Enter number: "))

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i, end=" ")

print()