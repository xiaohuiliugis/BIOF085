#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abhijit
"""

#%% preamble

import numpy as np
import pandas as pd
from glob import glob

#%% Tidy data

filenames = glob('data/table*.csv') 
filenames = sorted(filenames)

table1, table2, table3, table4a, table4b, table5 = [pd.read_csv(f) for f in filenames] # Use a list comprehension

#%%
pew = pd.read_csv('data/pew.csv')


pew_long = pd.melt(pew, id_vars = ['religion'],
                    var_name = 'income_group',
                    value_name = 'count')

#%% Splitting variables

var_expand = table3['rate'].str.split('/', expand = True)
var_expand.columns = ['cases','population']

table3_parsed = pd.concat([table3, var_expand], axis = 1)

del table3_parsed['rate']

#%% Pivot/spread

table2_long = table2.pivot_table(index = ['country','year'],
                   columns = 'type',
                   values = 'count')

table2_long.reset_index()

table2.pivot_table(index = ['country','year'],
                   values = 'count').reset_index()





