# Demo lists

# List Declared
a = [1, 2, 3, 4]
print(a)

# Accessing first element of list
print(a[1])

# updating the list
a[3] = 5
print(a)

# Adding into a list
a.append(6)
print(a)

# Inserting an intem into a list at some i postion
i = 3
a.insert(i, 4)
print(a)

# Removing a item
a.remove(5)
print(a)

a.append(3)
print(a)

# Counting item in a list
print("Number of times item:'3' is in my list: " + str(a.count(3)))
