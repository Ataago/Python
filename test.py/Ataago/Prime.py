num = int(input("Enter Number: "))

#for i in (2,num-1):
#    if num % i == 0:
#        print("Not a Prime")
#        exit(0)
print("Prime")

for i in range(2, num):
    print(i)
    i = i + 1