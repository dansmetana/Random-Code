# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:52:20 2020

@author: dsmet
"""

import pandas as pd

train = pd.read_csv('train.csv')

#Isolating a column
train.IsHoliday #creates a dynamic reference, not preferred
train['IsHoliday'] #preferred

#Count the number of records containing a holiday
train['IsHoliday'].sum()

#Count the number of records not containing a holiday
(train['IsHoliday'] == False).sum()
(~train['IsHoliday']).sum #~ works to do the opposite

#Number of records for each store
train['Store'].value_counts()

# Sorted by store # (index)
train['Store'].value_counts().sort_index()
#Sorted by record count (values)
train['Store'].index_counts().sort_values()
#Sorted by record ceount in descending order
train['Store'].index_counts().sort_values(ascending = False)

#Add a column for average daily sales
train['Daily_Sales'] = train['Weekly_Sales'] / 7

#rank
train['Weekly_Sales'].rank(method = 'min') #default, ranks in ascending order
train['Weekly_Sales'].rank(ascending = False, method = 'min') #ranks in descending order

#add a column for the rank
train['Sales_Rank'] = train['Weekly_Sales'].rank(ascending = False, method = 'min')
train.sort_values('Sales_Rank') #essentially the same as sorting on the sales column

#Select the record with weekly sales of 9755.56
train['Weekly_Sales'] == 9755.56 #returns a series of Booleans
train[train['Weekly_Sales'] == 9755.56] #Boolean indexing, will produce the full record

#import data with no header, and create headers
stats = pd.read_csv('usstates.csv', header = None, names = ['state', 'abbrev', 'area', 'population'] )

#All record for dept 14 of store 20
train[(train['Dept'] == 14) & (train['Store'] == 20)]

#Max weekly sales
train[train['Weekly_Sales'] == train['Weekly_Sales'].max()]

#Min weekly sales on Holiday weeks
train[train['IsHoliday']]['Weekly_Sales'].min()
#what record is this? 
train[train['Weekly_Sales'] ==train[train['IsHoliday']]['Weekly_Sales'].min()]

                         