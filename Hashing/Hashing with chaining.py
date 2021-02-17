# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:38:51 2021

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
      key_value=[key,value]
      self.length+=1
      if self.table[hv] is not None:
          self.table[hv].append(key_value)
      else:
          self.table[hv]=[key_value]
          
    def calculate_hash_value(self,key):
        return hash(key)%self.max_length
    def find_item(self,key):
        hv=self.calculate_hash_value(key)
        if self.table[hv] is None:
            raise KeyError
        else:
            for [i,info] in self.table[hv]:
                if i==key:
                    return hv
    def get_item(self,key):
        index=self.find_item(key)
        for [i,info] in self.table[index]:
            if i==key:
                return info
    def delete_item(self,key):
        index=self.find_item(key)
        self.length-=1
        for [i,info] in self.table[index]:
            if i==key:
                self.table[index]=None
                
          
            
hash_table=HashTable()
hash_table.store(11804562,"Dhanush")
hash_table.store(11804564,"Omeswar")
hash_table.store(11804573,"Sravan")

hash_table.delete_item(11804564)

print(hash_table.length)

print(hash_table.get_item(11804562))

