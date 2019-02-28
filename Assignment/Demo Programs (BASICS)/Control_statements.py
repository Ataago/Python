# Demonstrate the use of various Python control statements.

str = "Ataago"

#   break statement
#   Terminates the loop statement and transfers execution to the statement immediately following the loop.
for letter in str:
    if letter == 't':
        break
    print(letter)

#   2	continue statement
#   Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
for letter in str:
    if letter == 't':
        continue
    print(letter)

#   3	pass statement
#   The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
for letter in str:
    if letter == 't':
        pass
    print(letter)
