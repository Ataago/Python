#a.	Given a list of numbers from 1 to 20. Write a program to print only the first 5 prime numbers.

List = []
for i in range(1, 21):
    List.append(i)
print("List is: ",List)

count = 0
print("First 5 Prime numbers are: ",end=' ')
for item in List:
    countp = 0
    for i in range(1, item):
        if item % i == 0:
            countp += 1
    if countp == 1 and count < 5:
        count += 1
        print(item, end=' ')

