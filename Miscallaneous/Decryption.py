# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:07:45 2021

@author: pothu
"""

val=input("Enter the string you want to decrypt")
key=int(input("Enter key"))
string=''
for x in val:
    if x=='.':
        string+=" "
    else:
        value=key+ord(x)
        exachar=chr(value)
        string+=exachar
print(string)