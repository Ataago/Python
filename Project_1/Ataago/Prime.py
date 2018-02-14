num = int(input("Enter Number: "))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("Not a Prime")
            exit(0)
    print("Prime")
