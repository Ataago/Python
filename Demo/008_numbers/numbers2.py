# Check the number is prime or not
import sys   # Importing a Module called "sys"

n = int(input("Enter a number: "))

for i in range(2, n):   # 2, 3, 4, .. (n - 1)
    if n % i == 0:
        print("Not prime..")
        sys.exit()

print("Prime!")