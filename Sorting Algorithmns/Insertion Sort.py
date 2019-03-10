# 
#   Insertion Sort.py
#   Insertion Sort ALogrithmn
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

def insertionSort(array):
    """ Insertion sort for the array """
    n = len(array)

    for i in range(1, n):   # Select a key from range 1 to n
        key = array[i]      # Key
        j = i
        while j > 0 and array[j - 1] > key:     # Slide all elements which are greater than key to right
            array[j] = array[j - 1]
            j -= 1
        array[j] = key                          # Insert Key after sliding all the elements which are greater than key.

    return array


# Main Function
randomArray = createArray()
print("\nArray:")
print(randomArray)

sortedArray = insertionSort(randomArray)
print("\nSorted array: ")
print(sortedArray)
