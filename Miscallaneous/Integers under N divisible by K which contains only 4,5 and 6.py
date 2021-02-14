# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:55:08 2021

@author: pothu
"""
def checkcondition(i):
     while(i>0):
         r=i%10
         if r>=0 and r<=3 or r>=7 and r<=9:
             return False
#         else:
#             print("satisfied")
         i=i//10
     return True
     
n=int(input("Enter n: "))
k=int(input("Enter k: "))
for i in range(0,n):
    if i>0 and i%k==0:
        if i==4 or i==5 or i==6:
            print(i)
        elif checkcondition(i):
            print(i)
        