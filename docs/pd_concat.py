#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abhijit
"""

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['a'+str(i) for i in range(4)],
    'B': ['b'+str(i) for i in range(4)],
    'C': ['c'+str(i) for i in range(4)],
    'D': ['d'+str(i) for i in range(4)]})

df2 =  pd.DataFrame({'A': ['a'+str(i) for i in range(4,8)],
    'B': ['b'+str(i) for i in range(4,8)],
    'C': ['c'+str(i) for i in range(4,8)],
    'D': ['d'+str(i) for i in range(4,8)]})



df3 =  pd.DataFrame({'A': ['a'+str(i) for i in range(8,12)],
    'B': ['b'+str(i) for i in range(8,12)],
    'C': ['c'+str(i) for i in range(8,12)],
    'D': ['d'+str(i) for i in range(8,12)]})


row_concatenate = pd.concat([df1, df2, df3])

row_concatenate[3:]

df1.append(df2).append(df3)

new_row = pd.Series(['n1','n2','n3','n4'])
pd.concat([df1, new_row])

new_row = pd.DataFrame([['n1','n2','n3','n4']], 
                       columns = ['A','B','C','D'])
pd.concat([df1, new_row])

pd.concat([df1, df2, df3], axis=1)

df2.columns = ['E','F','G','H']
df3.columns = ['A','D','F','H']

pd.concat([df1, df2, df3])
pd.concat([df1, df3], join = 'inner')





