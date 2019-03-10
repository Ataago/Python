# 
#   Selection Sort.py
#   Selection Sort ALogrithmn
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

def selectionSort(array):
    """ Insertion sort for the array """
    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(1 + i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


# Main Function
randomArray = createArray()
print("\nArray:")
print(randomArray)

sortedArray = selectionSort(randomArray)
print("\nSorted array: ")
print(sortedArray)
