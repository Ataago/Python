#b.	Using functions write a python program to calculate the factorial  of a number(a non negative number). The function should accept the number#
#  as an argument. Print the accepted number, its factorial and the reverse of the factorial

num = int(input("Enter Number: "))

def fact(num):
    if num == 0:
        return 1
    return fact(num -1) * nu    m
facto = fact(num)
print("factorial is : ", facto)

rev = 0
print("reverse: ", end='')
while facto != 0:
    digit = int(facto % 10)
    facto = int(facto / 10)
    print(digit, end='')

