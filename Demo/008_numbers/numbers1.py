# Check the number is prime or not

n = int(input("Enter a number: "))
is_prime = True

for i in range(2, n):   # 2, 3, 4, .. (n - 1)
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime!")
else:
    print("Not Prime...")