# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:16:46 2020

@author: dsmet
"""

def word_frequency(string): 
    words = string.split()
    
    word_counter = {}
    
    for w in words:
        if w.lower() not in word_counter:
            word_counter[w.lower()] = 1
        if w.lower() in word_counter:
            word_counter[w.lower()] +=1
    
    return word_counter

#given

def word_frequency1(s):
    frequency = {}
    for word in s.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

#also given

def word_frequency2(s):
    return {w: s.lower().split().count(w) for w in s.lower.split()}