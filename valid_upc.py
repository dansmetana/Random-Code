# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:27:12 2020

@author: dsmet
"""

#given 
def valid_upc(upc):
    is_valid = False
    
    total = 0
    multiplier = 3
    
    for i in upc:
        total += multiplier*int*(i)
        
        if multiplier ==3:
            multiplier = 1
        else:
            multiplier = 3
    
    if total % 10 == 0:
        is_valid = True
        
    return is_valid

#using indexing 

def valid_upc1(upc):
    is_valid = False
    
    total = 0
    
    for i in range(12):
        if i % 2 == 0:
            total +=3*int(upc[i])
        else:
            total +=int(upc[i])
    
    if total % 10 == 0:
        is_valid = True
        
    return is_valid