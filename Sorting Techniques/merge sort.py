# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:54:45 2021

@author: pothu
"""

def mergesort(array):
    if len(array)>1:
        
        mid=len(array)//2
        l=array[:mid]
        r=array[mid:]
    
        mergesort(l)
        mergesort(r)
    
        i=j=k=0
    
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                array[k]=l[i]
                i+=1
            
            else:
                array[k]=r[j]
                j+=1
            k+=1
        
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
 
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
            

def printlist(array):
    for i in range(len(array)):
        print(array[i],end=" ")

array=[15,43,12,9,66,125,48,97,69]
print("Elements before sorting..")
print(array)
mergesort(array)
print("Elements after sorting..")
printlist(array)
