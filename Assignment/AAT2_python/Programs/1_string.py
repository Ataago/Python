My_list = ['abc', 'ataa', '121', 'hello', 'Yapay']

count = 0

for item in My_list:
    if item[0] == item[len(item)-1]:
        count += 1

print("Result = ", count)
