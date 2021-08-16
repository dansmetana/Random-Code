# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:28:20 2020

@author: dsmet
"""
#personal
def words_per_line(filename):
    words = 0
    count = 0
    file = open(filename, 'r')
    for line in file:
            words += len(line.strip())
            count += 1
    average = words/count
    file.close()
    return round(average, 2)
            

#given

def words_per_line2(filename):
    words = 0
    lines = 0
    
    with open(filename, 'r') as f:
        for line in f:
            lines +=1
            words += len(line.strip())
        return words/lines