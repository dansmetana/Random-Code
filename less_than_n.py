# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:18:52 2020

@author: dsmet
"""
#written
def less_than_n(filename, n):
    import numpy as np
    scores = []
    with open(filename, 'r') as f:
        for s in f:
            scores.append()
    scores_arr = np.array(scores)
    
    return scores_arr[scores_arr < 30].size

#given using loops

def less_than_n1(filename, n):
    count = 0
    with open(filename, 'r') as f:
        for s in f:
            if int(s) < n:
                count +=1
    return count

#given without loops

def less_than_n2(filename, n):
    import numpy as np
    arr = np.load(filename, dtype = np.int64)
    
    return arr[arr < 30].size