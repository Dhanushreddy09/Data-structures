# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:26:50 2021

@author: pothu
"""

class HashTable(object):
    def __init__(self):
        self.length=0
        self.max_length=11
        self.table=[None]*self.max_length
        
    def length(self):
        return self.length
        
    def store(self,key,value):
        hv=self.calculate_hash_value(key)
        key_value=(key,value)
        self.length+=1
        if self.table[hv] is None:
            self.table[hv]=key_value
        else:
            for j in range(self.max_length):
                index=(hv+j*j)%self.max_length
                if self.table[index] is None:
                    self.table[index]=key_value
                    break
                
    def calculate_hash_value(self,key):
        hv=key%self.max_length
        return hv
    def find_item(self,key):
        hv=self.calculate_hash_value(key)
        if self.table[hv] is None:
            raise KeyError
        if self.table[hv][0]==key:
            return hv
        else:
            for j in range(self.max_length):
                index=(hv+j*j)%self.max_length
                if self.table[index][0]==key:
                    return index
    def get_item(self,key):
        index=self.find_item(key)
        return self.table[index][1]
    def delete_item(self,key):
        self.length-=1
        index=self.find_item(key)
        self.table[index]=None
    

hash_table=HashTable()

hash_table.store(11804562,"Dhanush")    
  

print(hash_table.find_item(11804562))   
print(hash_table.get_item(11804562)) 

hash_table.store(11804573,"Sravan")    
  

print(hash_table.find_item(11804573)) 
print(hash_table.get_item(11804573))

hash_table.store(11804584,"Omeswar")    
  

print(hash_table.find_item(11804584))
print(hash_table.get_item(11804584))

hash_table.store(11804595,"Vamshi")    
  

print(hash_table.find_item(11804595))
print(hash_table.get_item(11804595))

hash_table.delete_item(11804562)

print(hash_table.length)




            
            
        
            
        