#6.	python program to find Fibonacci series upto a given number.
num = int(input("enter nth number: "))

a = 0
b = 1

def fib(x):
    if x <= 1:
        return x
    return fib(x-1)+fib(x-2)

print("Fibonacci series is: ", end=' ')
fib(num)
for i in range(num):
    print(fib(i), end=' ')