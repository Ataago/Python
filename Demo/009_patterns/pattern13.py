"""
    Program to display the following pattern

    example:
        Enter number of rows(n): 4
        pattern:
        1
        01
        101
        0101

"""

n = int(input("Enter n: "))

print("Method 1:")
a = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        a = 1
    else:
        a = 0
    for j in range(i):
        print(a, end="")
        if a == 1:
            a = 0
        else:
            a = 1
    print()


print("\nMethod 2:")
for i in range(1, n+1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()