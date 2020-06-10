# print Prime numbers

n = int(input("Enter number: "))

for i in range(2, n + 1):  # 1, 2, 3, 4, 5, ... n
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i, end=" ")

print()