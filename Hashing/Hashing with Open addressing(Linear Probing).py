# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:14:46 2021

@author: pothu
"""

class HashTable(object):
    def __init__(self):
        self.max_length=11
        self.table = [None]*self.max_length
        self.length=0
        
        
    def length(self):
        return self.length
    
    def get_item(self,key):
        index=self.find_item(key)
        return self.table[index][1]
        
    
    def store(self,key,value):
        self.length+=1
        hv=self.calculate_hash(key)
        while self.table[hv] is not None:
            if self.table[hv][0]==key:
                self.length-=1
                print("Entered key already exists")
                break
            hv=self.increment(key)
        key_value=(key,value)
        self.table[hv]=key_value  
        
    def calculate_hash(self,key):
        return hash(key) % self.max_length
    
    def increment(self,key):
        hv= hash(key+1) % self.max_length
        return hv
    
    def find_item(self,key):
        hv=self.calculate_hash(key)
        if self.table[hv] is None:
            raise KeyError
        while self.table[hv][0]!=key:
            hv=self.increment(hv)
        return hv
    
    def delete(self,key):
        self.length-=1
        index=self.find_item(key)
        while index is None:
            self.length+=1
            break
        self.table[index]=None
            

# Setup
hash_table=HashTable()

#Returning Length
hash_table.store(11804562,"Dhanush")
print(hash_table.find_item(11804562))
print(hash_table.get_item(11804562))

hash_table.store(11804573,"Sravan")
print(hash_table.find_item(11804573))
print(hash_table.get_item(11804573))

hash_table.store(11804584,"Omeswar")
print(hash_table.length)
#print(hash_table.find_item(11804584))
#print(hash_table.get_item(11804584))



#hash_table.store(11804583,"Omeswar")
#print(hash_table.find_item(11804583))
#print(hash_table.get_item(11804583))



