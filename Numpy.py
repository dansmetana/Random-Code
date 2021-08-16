# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:30:59 2020

@author: dsmet
"""
import numpy as np

lakes = np.array(["Huron", "Ontario", "Michigan", "Erie", "Superior"])
lake_areas = np.array([23000, 8000, 22000, 10000, 32000])

#Write an expression for each of the following:

#The number of great lakes
len(lakes) #don't do this
lakes.size #do this instead #reading an attribute #works for multi-dim arrays

#The area of the 5th lake in the list
lake_areas[4]

#The largest area in lake_areas
max(lake_areas) #don't do this
lake_areas.max() #do this
np.max(lake_areas) #or this

#The total area of all 5 lakes
sum(lake_areas) #don't do this
lake_areas.sum() #do this
np.sum(lake_areas) #or this

#All area figures greater than 22,000 sq mi
lake_areas > 22000 #produces a Boolean array, element wise comparison against the condition
#the Boolean array can then be used as as index
lake_areas[lake_areas > 22000] #will produce an array where only the condition is true

#The name of the lake with the largest area
lake_areas.max() #largest area
lake_areas == lake_areas.max() # True where area = largest

lakes[lake_areas == lake_areas.max()] #parallel Boolean indexing

#The name of all lakes smaller than 22,000 sq mi
lakes[lake_areas < 22000]

#The area of Lake Superior
lake_areas[lakes == 'Superior']

#The area of Lake Superior and Huron
lake_areas[(lakes == 'Superior') | (lakes == 'Huron')]

#The names of all lakes in alphabetical order
lakes.sort() #bad and should be avoided most times, fundamentally changes the array and in turn messes up the parallel arrays #sorts "in-place"
np.sort(lakes) #original array remains in the original order #copy is returned

#The names of all lakes in order by area, largest to smallest (hint: explore argsort)
np.argsort(lake_areas) #produces an array that would sort the array, can then be used as an index

lakes[np.argsort(lake_areas)[::-1]] #produces the output we desire