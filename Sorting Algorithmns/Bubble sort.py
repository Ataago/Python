# 
#   Bubble sort.py
#   Bubble Sort ALogrithmn
#   
#   Created by Mohammed Ataa on 28/02/19.
#   Copyright © 2019 Ataago. All rights reserved.
#

import numpy

def createArray():
    """ Function to create an array of n elements promted to user """
    array = []
    n = "should be an integer"

    # Taking a valid input
    while not isinstance(n, int):
        try:
            n = int(input("Enter Array Length: "))
        except:
            pass

    for i in range(n):  # Getting a random value for each element
        array.append(numpy.random.randint(100))

    return array


def bubbleSort(array):
    """ to sort the array using bubble sort """
    # Here we bubble the largest element towards the right
    n = len(array)  # Length of array

    for i in range(n):  # Outer loop
        swapCounter = 0     # every outer loop we count number of swaps done
        for j in range(n - i - 1):  # Inner loop
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]    # Swaping
                swapCounter += 1    # Increment Swap counter for every swap
        
        if swapCounter == 0:
            return array
    



# Main Function
randomArray = createArray()
print("\nArray:")
print(randomArray)

sortedArray = bubbleSort(randomArray)
print("\nSorted array: ")
print(sortedArray)