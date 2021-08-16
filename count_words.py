# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:18:21 2020

@author: dsmet
"""

#personal
def count_words(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        if line != "":
            count += len(line.strip())
    file.close()
    return count
        
        
#given

def count_words2(filename):
    words = 0
    
    with open(filename, 'r') as f:
        for line in f:
            words +=len(line.strip())
        return words