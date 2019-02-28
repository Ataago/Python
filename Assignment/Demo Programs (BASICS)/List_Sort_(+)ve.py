#	Write a Python program to remove all negative elements from
#   the list and return all positive elements sorted in ascending order.

list1 = [1, -3, -5, 4, -7, 2, 0, 3]

count = 0
for i in range(0,len(list1)):
    if list1[i] < 0:
        list1[i] = -1
        count += 1
for i in range(0,count):
    list1.remove(-1)

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)