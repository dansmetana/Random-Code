# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:24:05 2020

@author: dsmet
"""

def word_index(filename):
    index = {}
    with open(filename, 'r') as f:
        n = 0
        line = f.readline()
        while line != '':
            n += 1
            words = line.strip().split(' ')
            for word in words:
                index[word] = list(set(index.get(word, []) + [n]))
            line = f.readline()
         
    return index