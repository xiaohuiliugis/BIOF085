#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abhijit
"""

#%% Data transformations
#%% Arithmetic operations

import numpy as np
import pandas as pd

A = pd.DataFrame(np.random.randn(4, 6))
B = pd.DataFrame(np.random.rand(4, 6))
c = pd.Series([1,2,3,4,5,6])

A + 2.5
A * 5

A + B
A * B

A + c
A / c

A - A.mean()

D = (A - A.mean())/A.std()

#%% Extracting rows and columns

titanic=pd.read_csv('data/titanic.csv')

titanic['Survived']
titanic[:2]
titanic[3:25]

titanic.loc[:, ['Survived','Fare']]
titanic.loc[0:6, ['Survived', 'Fare']]
titanic.loc[0:6, 'PassengerId':'Pclass']
titanic.iloc[0:6, :3]

titanic[titanic['Pclass'] == 1]
titanic[(titanic['Pclass'] == 1) & (titanic['Fare'] > 50)]

titanic.query('(Pclass == 1) & (Fare > 50)')
titanic.query('(Pclass == 1) & (Embarked == "S")')
titanic.query("(Pclass == 1) & (Embarked == 'S')")














