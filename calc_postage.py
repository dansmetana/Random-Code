# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:03:42 2020

@author: dsmet
"""

postage_weight = float(input("Please enter postage weight (oz): "))

import math as math

postage_weight = math.ceil(postage_weight)
add_ounces= postage_weight -1

def calc_postage(postage_weight):
    if postage_weight<=1:
        postage_cost = .05*postage_weight
    else:
        postage_cost = (.05 +.10*add_ounces)
    return round(postage_cost, 2)
    
calc_postage(postage_weight)


---------------------

import math as math 

def calc_postage(oz):
    ounces = math.ceil(oz)
    
    if ounces == 1:
        postage = .05
    else:
        postage = .05 + (ounces - 1)*10
    
    return round(postage, 2)