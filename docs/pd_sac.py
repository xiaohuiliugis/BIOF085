#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: abhijit
"""

#%% preamble

import numpy as np
import pandas as pd

#%% split-apply-combine

df = pd.read_csv('data/gapminder.tsv', sep = '\t') # data is tab-separated, so we use `\t` to specify that

f"This dataset has {len(df['country'].unique())} countries in it"

df.groupby('country')['lifeExp'].mean()

df.groupby('country')

df.groupby('country').get_group('India')


avg_lifeExp_country = df.groupby('country')['lifeExp'].mean()


df.groupby(['continent', 'year'])['lifeExp'].mean().reset_index()

df.groupby('continent')['lifeExp'].describe()

df.groupby('continent').nth(10)

df.groupby('continent')['lifeExp'].agg(np.mean)


def my_mean(values):
    s = 0
    n = len(values)
    
    for value in values:
        s += value
    return(s / n)

df.groupby('continent')['lifeExp'].agg(my_mean)

df.groupby('continent')['lifeExp'].agg([np.count_nonzero, np.mean, np.median])

df.groupby('continent').agg({'lifeExp': np.mean,
                             'pop': np.median,
                             'gdpPercap': np.median})

def my_zscore(values):
    m = np.mean(values)
    s = np.std(values)
    
    return((values - m)/s)

df['lifeExp_z'] = df.groupby('year')['lifeExp'].transform(my_zscore)
