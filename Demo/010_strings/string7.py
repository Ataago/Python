# String Format types

age = 10
year = 1999

print("Franklin's age is " + str(age) + ", who was born in " + str(year) + ".")     # Not Recommeneded
print(f"Franklin's age is {age}, who was born in {year}.")
print("Franklin's age is {}, who was born in {}.".format(age, year))