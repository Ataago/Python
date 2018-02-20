
list1 = [1, -3, -5, 4, -7, 2, 0, 3]

count = 0

num = len(list1)

for i in range(0,num):
    if list1[i] < 0:
        list1.remove(list1[i])
print(list1)