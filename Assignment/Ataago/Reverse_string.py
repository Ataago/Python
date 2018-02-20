#a.	Write a python program that returns a given string in the reverse order.

str = input("Enter String: ")

#1 preDefined
print("Reverse with Pre-defined function: ", ''.join(reversed(str)))


#2 userDefined recursive
def reverse(string):
    if len(string) == 1:
        return string
    return reverse(string[1:]) + string[0]

print("Reverse with User-defined Function: ", reverse(str))


#3 slice
def reverse_s(string):
    return string[::-1]

print("Reverse: ", reverse_s(str))


#4 character Concatination
reverse_str = ''
for char in str:
    reverse_str = char + reverse_str

print("Char concat : ", reverse_str)

