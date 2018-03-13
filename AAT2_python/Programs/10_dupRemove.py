#10.	python program to remove duplicates from a list.
visited_dict = {}
My_list = [1, 2, 3, 4, 1, 2, 5, 6, 1]

print("My List is:",My_list)
for item in My_list:
    visited_dict[item] = False

for item in My_list:
        if visited_dict[item] is False:
            visited_dict[item] = True
        else:
            My_list.remove(item)

print("After Removing Duplicates: ",My_list)
