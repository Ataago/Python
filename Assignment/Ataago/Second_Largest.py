#b.	Let D[] be a list of numbers. Assume that the numbers are unique. Write a python program to find the second biggest number in the list.

D = [1, 3, 7, 4, 6]

l1 = D[0]
l2 = D[1]

for item in D:
    if l1 < item:
        l2 = l1
        l1 = item
    elif l1 != item and l2 < item:
        l2 = item

print("Second Largest is :", l2)
