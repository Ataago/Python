# 
#   Merge Sort.py
#   Merge Sort ALogrithmn
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


def merge(l, m, r):
    """ Merge left and right arrays """
    left = l            # left array iterator
    right = m + 1       # right array iterator
    sortedArray = []    # merge left and right array into sortedArray

    while left <= m  and right <= r:        # do Untill we exhust either of the Left or right array
        if randomArray[left] < randomArray[right]:
            sortedArray.append(randomArray[left])
            left += 1
        else:
            sortedArray.append(randomArray[right])
            right += 1

    while right <= r:
        sortedArray.append(randomArray[right])
        right += 1

    while left <= m:
        sortedArray.append(randomArray[left])
        left += 1

    left = l    
    for i in range(len(sortedArray)):       # Replace the sorted array into the main array
        randomArray[left] = sortedArray[i]
        left += 1


def mergeSort(l, r):
    """ Divide the array in recursive way """
    if l < r:
        m = int((l + r) / 2)    # Mid point
    
        mergeSort(l, m)         # Left Array
        mergeSort(m + 1, r)     # Right Array

        merge(l, m, r)
  


# Main Function
randomArray = createArray()
print("\nArray:")
print(randomArray)

l = 0
r = len(randomArray) - 1

mergeSort(l, r)
print("\nSorted array: ")
print(randomArray)
