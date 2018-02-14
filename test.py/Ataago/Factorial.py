num = int(input("Enter Number for Fact: "))

fact = 1
if num < 0:
    exit(0)
while num > 0:
    fact *= num
    num -= 1
print("Factorial is : ",fact)