#7.	python program to sort the elements of a list in descending order and separate the list into lists of +ve elements and –ve elements.
My_List = [1, 2, 5, 8, -1, -8, -7, 0]

for i in range(0,len(My_List)):
    for j in range(0,len(My_List) -i -1):
        if My_List[j] < My_List[j+1]:
            temp = My_List[j]
            My_List[j] = My_List[j+1]
            My_List[j+1] = temp

print("Sorted in Descending order: ", My_List)

print("Postive array: ",end=' ')
pos_list = list(filter(lambda x: x >= 0, My_List))
print(pos_list)

print("Negative array: ",end=' ')
neg_list = list(filter(lambda x: x < 0, My_List))
print(neg_list)
