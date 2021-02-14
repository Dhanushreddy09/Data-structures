# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:15:02 2021

@author: pothu
"""

def quicksort(array):
    length=len(array)
    if length<=1:
        return array
    else:
        pivot=array.pop()
    
    lowest_elements=[]
    highest_elements=[]
    
    for item in array:
        if item>pivot:
            highest_elements.append(item)
        else:
            lowest_elements.append(item)
    
    return quicksort(lowest_elements)+[pivot]+quicksort(highest_elements)

array=[56,32,89,54,79,666,2587,3,28,17]
print(quicksort(array))