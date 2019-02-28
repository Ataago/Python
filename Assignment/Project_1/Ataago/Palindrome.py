str = input("Enter String: ")

str = str.casefold()
print(str)
rev_str = reversed(str)
if list(str) == list(rev_str):
    print("Palindrome")
else:
    print("Not Palindrome")
print(rev_str)