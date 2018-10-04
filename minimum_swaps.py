'''You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
without any duplicates. You are allowed to swap any two elements. 

You need to find the minimum number of swaps required to sort the array in ascending order.

>>> minimumswaps([7, 1, 3, 2, 4, 5, 6])
5
>>> minimumswaps([4, 3, 2, 1])
2
>>> minimumswaps([2, 3, 4, 1, 5])
3
>>> minimumswaps([1, 3, 5, 2, 4, 6, 8])
3

'''
import math
import os
import random
import re
import sys


def minimumswaps(arr):
    
    # create list of tuples [(element, position)]
    arrpos = []
    for i, v in enumerate(arr):
        arrpos.append((i,v))
    
    #sort by element value
    arrpos.sort(key=lambda x: x[1] )
    
    #create dictionary to track visited nodes
    visited = {}
    for i in range(len(arrpos)):
        visited[i] = False
    
    swaps = 0
    #checking each node and count lenth and number of cycles
    for i in range(len(arrpos)):
        if visited[i] or arrpos[i][0] == i:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            cycle_len += 1
            j = arrpos[j][0]
        swaps += cycle_len - 1
    
    return swaps


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
