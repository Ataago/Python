#aat2 project for python

#@author Mohammed Ataaur Rahaman
#Submited to: Prof. Anil T Sagar
#USN: 1DS16CS721
#Date: 28th Feb, 2018

def default(x):
    print("Invalid Entry")

def run(ProNum):
    if(ProNum == 1):
        print( "#################################################################################################################################################################################")
        My_list = ['abc', 'ataa', '121', 'hello', 'Yapay']

        print("Given List is :", My_list)
        count = 0

        for item in My_list:
            if item[0] == item[len(item) - 1]:
                count += 1

        print("Number of strings ending with same characters are: ", count)
        print("#################################################################################################################################################################################")

    elif(ProNum == 2):
        print("#################################################################################################################################################################################")

        # Python program for implementation of MergeSort

        # Merges two subarrays of arr[].
        # First subarray is arr[l..m]
        # Second subarray is arr[m+1..r]
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            # create temp arrays
            L = [0] * (n1)
            R = [0] * (n2)

            # Copy data to temp arrays L[] and R[]
            for i in range(0, n1):
                L[i] = arr[l + i]

            for j in range(0, n2):
                R[j] = arr[m + 1 + j]

            # Merge the temp arrays back into arr[l..r]
            i = 0  # Initial index of first subarray
            j = 0  # Initial index of second subarray
            k = l  # Initial index of merged subarray

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Copy the remaining elements of L[], if there
            # are any
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            # Copy the remaining elements of R[], if there
            # are any
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        # l is for left index and r is right index of the
        # sub-array of arr to be sorted
        def mergeSort(arr, l, r):
            if l < r:
                # Same as (l+r)/2, but avoids overflow for
                # large l and h
                m = (l + (r - 1)) // 2

                # Sort first and second halves
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)

        # Driver code to test above
        arr = [12, 11, 13, 5, 6, 7]
        n = len(arr)
        print("Given array is")
        for i in range(n):
            print("%d" % arr[i], end=' ')

        mergeSort(arr, 0, n - 1)
        print("\n\nSorted array is")
        for i in range(n):
            print("%d" % arr[i], end=' ')

        print("#################################################################################################################################################################################")

    elif(ProNum == 3):
        print("#################################################################################################################################################################################")
        # b.	Write a Python program to implement stackoperations  using  functions.

        # list as stack
        stack = []
        size = 3

        def Display_Stack():
            print("Stack :")
            for item in stack:
                print(item)

        def Push(item):
            if len(stack) < size:
                stack.append(item)
            else:
                print("Stack is full!")

        def Pop():
            if len(stack) > 0:
                stack.pop()  # pre defined function
            else:
                print("Stack is empty.")

        # type what ever u want here
        Push(1)
        Push(2)
        Push(3)
        Display_Stack()
        Push(4)
        Display_Stack()
        Pop()
        Display_Stack()
        print("#################################################################################################################################################################################")

    elif(ProNum == 4):
        print("#################################################################################################################################################################################")
        # 4.	python program to implement Queue Operations.
        queue = []
        size = 10

        def display_q():
            if len(queue) == 0:
                print("Empty")
            else:
                print("Queue is:", end=' ')
                for item in queue:
                    print(item, end=' ')

        def enQ(item):

            if len(queue) < size:
                queue.append(item)

            else:
                print("Queue is full")

        def deQ():
            print("\ndeleted: ", queue[0])
            del queue[0]

        display_q()
        enQ(5)
        enQ(1)
        enQ(2)
        enQ(4)
        enQ(3)
        display_q()
        deQ()
        display_q()
        print("#################################################################################################################################################################################")

    elif(ProNum == 5):
        print("#################################################################################################################################################################################")
        # b.	Using functions write a python program to calculate the factorial  of a number(a non negative number). The function should accept the number#
        #  as an argument. Print the accepted number, its factorial and the reverse of the factorial

        num = int(input("Enter Number: "))

        def fact(num):
            if num == 0:
                return 1
            return fact(num - 1) * num

        facto = fact(num)
        print("factorial is : ", facto)

        rev = 0
        print("reverse: ", end='')
        while facto != 0:
            digit = int(facto % 10)
            facto = int(facto / 10)
            print(digit, end='')

        print("#################################################################################################################################################################################")

    elif(ProNum == 6):
        print("#################################################################################################################################################################################")
        # 6.	python program to find Fibonacci series upto a given number.
        num = int(input("enter nth number: "))

        a = 0
        b = 1

        def fib(x):
            if x <= 1:
                return x
            return fib(x - 1) + fib(x - 2)

        print("Fibonacci series is: ", end=' ')
        fib(num)
        for i in range(num):
            print(fib(i), end=' ')
        print("#################################################################################################################################################################################")

    elif(ProNum == 7):
        print("#################################################################################################################################################################################")
        # 7.	python program to sort the elements of a list in descending order and separate the list into lists of +ve elements and –ve elements.
        My_List = [1, 2, 5, 8, -1, -8, -7, 0]

        print("My list is: ",My_List)
        for i in range(0, len(My_List)):
            for j in range(0, len(My_List) - i - 1):
                if My_List[j] < My_List[j + 1]:
                    temp = My_List[j]
                    My_List[j] = My_List[j + 1]
                    My_List[j + 1] = temp

        print("Sorted in Descending order: ", My_List)

        print("Postive array: ", end=' ')
        pos_list = list(filter(lambda x: x >= 0, My_List))
        print(pos_list)

        print("Negative array: ", end=' ')
        neg_list = list(filter(lambda x: x < 0, My_List))
        print(neg_list)

        print("#################################################################################################################################################################################")

    elif(ProNum == 8):
        print("#################################################################################################################################################################################")
        # a.	Write a python program that returns a given string in the reverse order.

        str = input("Enter String: ")

        # 1 preDefined
        print("Reverse with Pre-defined function: ", ''.join(reversed(str)))

        # 2 userDefined recursive
        def reverse(string):
            if len(string) == 1:
                return string
            return reverse(string[1:]) + string[0]

        print("Reverse with User-defined Function: ", reverse(str))

        # 3 slice
        def reverse_s(string):
            return string[::-1]

        print("Reverse: ", reverse_s(str))

        # 4 character Concatination
        reverse_str = ''
        for char in str:
            reverse_str = char + reverse_str

        print("Char concat : ", reverse_str)
        print("#################################################################################################################################################################################")

    elif(ProNum == 9):
        print("#################################################################################################################################################################################")
        # 10 python program to check whether a list contains a sub list.
        My_list = [1, [2, 3], 4, 1, 2, 3, 4]
        flag = 0

        print("My list is: ", My_list)
        for item in My_list:
            if type(item) is list:
                print("The list contains a sublist")
                flag = 1

        if flag is 0:
            print("The list does not contain a sublist.")

        print("#################################################################################################################################################################################")

    elif(ProNum == 10):
        print("#################################################################################################################################################################################")
        # 10.	python program to remove duplicates from a list.
        visited_dict = {}
        My_list = [1, 2, 3, 4, 1, 2, 5, 6, 1]

        print("My List is:", My_list)
        for item in My_list:
            visited_dict[item] = False

        for item in My_list:
            if visited_dict[item] is False:
                visited_dict[item] = True
            else:
                My_list.remove(item)

        print("After Removing Duplicates: ", My_list)
        print("#################################################################################################################################################################################")

    elif(ProNum == 11):
        print("#################################################################################################################################################################################")
        # python program to implement transpose of a matrix.A
        m = int(input('number of rows, m = '))
        n = int(input('number of columns, n = '))
        matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                print('entry in row: ', i + 1, ' column: ', j + 1)
                matrix[i][j] = int(input())

        print("Matrix entered is:")
        for i in range(m):
            for j in range(n):
                print(matrix[i][j], end=' ')
            print("")

        print("Transpose of the Matrix is:")
        for i in range(n):
            for j in range(m):
                print(matrix[j][i], end=' ')
            print("")
        print("#################################################################################################################################################################################")

    elif(ProNum == 12):
        print("#################################################################################################################################################################################")

        # Python program for implementation of Quicksort Sort

        # This function takes last element as pivot, places
        # the pivot element at its correct position in sorted
        # array, and places all smaller (smaller than pivot)
        # to left of pivot and all greater elements to right
        # of pivot
        def partition(arr, low, high):
            i = (low - 1)  # index of smaller element
            pivot = arr[high]  # pivot

            for j in range(low, high):

                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
                    # increment index of smaller element
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index

        # Function to do Quick sort
        def quickSort(arr, low, high):
            if low < high:
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)

                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

        # Driver code to test above
        arr = [10, 7, 8, 9, 1, 5]
        print("Given Array: ", arr)
        n = len(arr)
        quickSort(arr, 0, n - 1)
        print("Sorted array is:", end=' ')
        print(arr)
        print("#################################################################################################################################################################################")

    elif(ProNum == 13):
        print("#################################################################################################################################################################################")
        # 13.	python program to find the second biggest number in the list.
        D = [1, 3, 7, 4, 6]

        l1 = D[0]
        l2 = D[1]

        for item in D:
            if l1 < item:
                l2 = l1
                l1 = item
            elif l1 != item and l2 < item:
                l2 = item
        print("List is: ", D)
        print("Second Largest is :", l2)

        print("#################################################################################################################################################################################")

    elif(ProNum == 14):
        print("#################################################################################################################################################################################")
        # a.	Given a list of numbers from 1 to 20. Write a program to print only the first 5 prime numbers.

        List = []
        for i in range(1, 21):
            List.append(i)
        print("List is: ", List)

        count = 0
        print("First 5 Prime numbers are: ", end=' ')
        for item in List:
            countp = 0
            for i in range(1, item):
                if item % i == 0:
                    countp += 1
            if countp == 1 and count < 5:
                count += 1
                print(item, end=' ')

        print("#################################################################################################################################################################################")

    elif (ProNum == 15):
        print("#################################################################################################################################################################################")
        # 15. 	python program to check weather the given year is leap year or not.
        year = int(input("Enter Year: "))

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Leap year")
                else:
                    print("Not a Leap Year")
            else:
                print("Leap Year")
        else:
            print("Not a Leap Year")
        print("#################################################################################################################################################################################")


def display(ProNum):
    if(ProNum == 1):
        print('''
#################################################################################################################################################################################
1. Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

My_list = ['abc', 'ataa', '121', 'hello', 'Yapay']
count = 0

for item in My_list:
    if item[0] == item[len(item)-1]:
        count += 1

print("Result = ", count)
#################################################################################################################################################################################
''')

    elif(ProNum == 2):
        print('''
#################################################################################################################################################################################'
# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=' ')

mergeSort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=' ')
#################################################################################################################################################################################
        ''')
    elif (ProNum == 3):
        print('''
#################################################################################################################################################################################
#b.	Write a Python program to implement stackoperations  using  functions.

#list as stack
stack = []
size = 3

def Display_Stack():
    print("Stack :")
    for item in stack:
        print(item)

def Push(item):
    if len(stack) < size:
        stack.append(item)
    else:
        print("Stack is full!")

def Pop():
    if len(stack) > 0:
        stack.pop()         #pre defined function
    else:
        print("Stack is empty.")

#type what ever u want here
Push(1)
Push(2)
Push(3)
Display_Stack()
Push(4)
Display_Stack()
Pop()
Display_Stack()
#################################################################################################################################################################################
        ''')
    elif (ProNum == 4):
        print('''
#################################################################################################################################################################################
#4.	python program to implement Queue Operations.
queue = []
size = 10

def display_q():
    if len(queue) == 0:
        print("Empty")
    else:
        print("Queue is:", end=' ')
        for item in queue:
            print(item, end=' ')

def enQ(item):

    if len(queue) < size:
        queue.append(item)

    else:
        print("Queue is full")

def deQ():
    print("\ndeleted: ",queue[0])
    del queue[0]

display_q()
enQ(5)
enQ(1)
enQ(2)
enQ(4)
enQ(3)
display_q()
deQ()
display_q()
#################################################################################################################################################################################
        ''')
    elif (ProNum == 5):
        print('''
#################################################################################################################################################################################
#b.	Using functions write a python program to calculate the factorial  of a number(a non negative number). The function should accept the number#
#  as an argument. Print the accepted number, its factorial and the reverse of the factorial

num = int(input("Enter Number: "))

def fact(num):
    if num == 0:
        return 1
    return fact(num -1) * num
facto = fact(num)
print("factorial is : ", facto)

rev = 0
print("reverse: ", end='')
while facto != 0:
    digit = int(facto % 10)
    facto = int(facto / 10)
    print(digit, end='')
#################################################################################################################################################################################
        ''')
    elif (ProNum == 6):
        print('''
#################################################################################################################################################################################
#6.	python program to find Fibonacci series upto a given number.
num = int(input("enter nth number: "))

a = 0
b = 1

def fib(x):
    if x <= 1:
        return x
    return fib(x-1)+fib(x-2)

print("Fibonacci series is: ", end=' ')
fib(num)
for i in range(num):
    print(fib(i), end=' ')
#################################################################################################################################################################################
        ''')
    elif (ProNum == 7):
        print('''
#################################################################################################################################################################################
#7.	python program to sort the elements of a list in descending order and separate the list into lists of +ve elements and –ve elements.
My_List = [1, 2, 5, 8, -1, -8, -7, 0]

print("My list is: ",My_list)
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
#################################################################################################################################################################################
        ''')
    elif (ProNum == 8):
        print('''
#################################################################################################################################################################################
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
#################################################################################################################################################################################
        ''')
    elif (ProNum == 9):
        print('''
#################################################################################################################################################################################
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
#################################################################################################################################################################################
        ''')
    elif (ProNum == 10):
        print('''
#################################################################################################################################################################################
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
#################################################################################################################################################################################

        ''')
    elif (ProNum == 11):
        print('''
#################################################################################################################################################################################
#python program to implement transpose of a matrix.A
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
  for j in range(n):
    print('entry in row: ', i+1, ' column: ', j+1)
    matrix[i][j] = int(input())

print("Matrix entered is:")
for i in range (m):
    for j in range (n):
        print(matrix[i][j], end=' ')
    print("")


print("Transpose of the Matrix is:")
for i in range(n):
    for j in range(m):
        print(matrix[j][i], end=' ')
    print("")
#################################################################################################################################################################################

        ''')
    elif (ProNum == 12):
        print('''
#################################################################################################################################################################################
# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
print("Given Array: ", arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", end=' ')
print( arr)
#################################################################################################################################################################################

        ''')
    elif (ProNum == 13):
        print('''
#################################################################################################################################################################################
#13.	python program to find the second biggest number in the list.
D = [1, 3, 7, 4, 6]

l1 = D[0]
l2 = D[1]

for item in D:
    if l1 < item:
        l2 = l1
        l1 = item
    elif l1 != item and l2 < item:
        l2 = item
print("List is: ",D)
print("Second Largest is :", l2)
#################################################################################################################################################################################

        ''')
    elif (ProNum == 14):
        print('''
#################################################################################################################################################################################
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
#################################################################################################################################################################################

        ''')
    elif (ProNum == 15):
        print('''
#################################################################################################################################################################################
#15. 	python program to check weather the given year is leap year or not.
year = int(input("Enter Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
#################################################################################################################################################################################

        ''')


def ReadExecute(ProNum):
    print('''   
            Choose 1 to Display the code.
            Choose 2 to Run the code.
            Choose 3 to Menu
            ''')
    value = int(input("Enter Choice: "))
    while value != 3:
        def switchFunR(value):
            switchReadExecute = {
                1: display,
                2: run,
            }
            return switchReadExecute.get(value, default)(ProNum)
        switchFunR(value)
        print("\nFor Program",ProNum)
        print('''            Choose 1 to Display the code.
            Choose 2 to Run the code.
            Choose 3 to Menu
                    ''')
        value = int(input("Enter Choice: "))


def pro_1(x):
    print("\n 1. Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.")
    ReadExecute(x)

def pro_2(x):
    print("\n 2. Ppython program to implement merge sort.")
    ReadExecute(x)

def pro_3(x):
    print("\n 3. Program to implement Stack operations. ")
    ReadExecute(x)

def pro_4(x):
    print("\n 4. Python program to implement Queue Operations.  ")
    ReadExecute(x)

def pro_5(x):
    print("\n  5. Python program to find the factorial of a given number.")
    ReadExecute(x)

def pro_6(x):
    print("\n  6. Python program to find Fibonacci series upto a given number.")
    ReadExecute(x)

def pro_7(x):
    print("\n  7. Python program to sort the elements of a list in descending order and separate the list into lists of +ve elements and –ve elements. ")
    ReadExecute(x)

def pro_8(x):
    print("\n  8. Python program to reverse a string using string functions.")
    ReadExecute(x)

def pro_9(x):
    print("\n 9. Python program to check whether a list contains a sub list. ")
    ReadExecute(x)

def pro_10(x):
    print("\n  10. Python program to remove duplicates from a list.")
    ReadExecute(x)

def pro_11(x):
    print("\n 11. Python program to implement transpose of a matrix. ")
    ReadExecute(x)

def pro_12(x):
    print("\n  12. Python program to implement Quick sort.")
    ReadExecute(x)

def pro_13(x):
    print("\n  13. Python program to find the second biggest number in the list.")
    ReadExecute(x)

def pro_14(x):
    print("\n  14. Python program to print only the first 5 prime numbers.")
    ReadExecute(x)

def pro_15(x):
    print("\n 15. Python program to check weather the given year is leap year or not. ")
    ReadExecute(x)


def menu():
    print('''\n\n##############  Menu:  ##################	\n
Choose the corresponding program no to display / excecute:
    1.	python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
    2.	python program to implement merge sort.
    3.	program to implement Stack operations.
    4.	python program to implement Queue Operations. 
    5.	python program to find the factorial of a given number.
    6.	python program to find Fibonacci series upto a given number.
    7.	python program to sort the elements of a list in descending order and separate the list into lists of +ve elements and –ve elements. 
    8.	python program to reverse a string using string functions.
    9.	python program to check whether a list contains a sub list.
    10.	python 	to remove duplicates from a list.
    11.	python program to implement transpose of a matrix.
    12.	python program to implement Quick sort.
    13.	python program to find the second biggest number in the list.
    14.	python program to print only the first 5 prime numbers.
    15. python program to check weather the given year is leap year or not.
    0. 	Exit. 
                ''')
    choice = int(input("Enter Your Choice: "))
    def switchFun(choice):
        switchDic = {
            1: pro_1,
            2: pro_2,
            3: pro_3,
            4: pro_4,
            5: pro_5,
            6: pro_6,
            7: pro_7,
            8: pro_8,
            9: pro_9,
            10: pro_10,
            11: pro_11,
            12: pro_12,
            13: pro_13,
            14: pro_14,
            15: pro_15,
            0: exit
        }
        return switchDic.get(choice, default)(choice)
    switchFun(choice)


#Driver Program
print('''\n\nAuthor: Mohammed Ataaur Rahaman''')
print("Submited to: Prof. Anil T Sagar")
print("USN: 1DS16CS721")
print("Date: 28th Feb, 2018")

print("                                                                       Python CIA - 1: AAT2")


print("Continue to the programs (y/n)?")
YesNo = input()
if( YesNo == 'n'):
    exit(0)
elif(YesNo == 'y'):
    while 1:
        menu()