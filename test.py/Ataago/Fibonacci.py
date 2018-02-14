num = int(input("Enter nth number: "))
a = 0
b = 1
print("Fibonacci Series : ")
if(num > 1):
    print(a,b,end=' ')
    if num > 2:
        while num > 2:
            c = a + b
            print(c,end=' ')
            a = b
            b = c
            num -= 1

elif num < 1:
    print("No Digits")
else:
    print(a)