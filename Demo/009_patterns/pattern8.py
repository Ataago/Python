# Powers of numbers

"""
to display 

3 9 27.. 
"""

n = int(input("Enter a number: "))
stop = int(input("Enter number of powers to display: "))

for i in range(1, stop + 1):
    print(n ** i, end=" ")

print()