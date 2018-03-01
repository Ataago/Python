#10 python program to check whether a list contains a sub list.
My_list = [1, [2, 3], 4, 1, 2, 3, 4]
flag = 0

print("My list is: ",My_list)
for item in My_list:
    if type(item) is list:
        print("The list contains a sublist")
        flag = 1

if flag is 0:
    print("The list does not contain a sublist.")

