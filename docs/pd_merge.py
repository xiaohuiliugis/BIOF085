#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: abhijit
"""

#%% Merging data

import numpy as np
import pandas as pd

person = pd.read_csv('data/survey_person.csv')
site = pd.read_csv('data/survey_site.csv')
survey = pd.read_csv('data/survey_survey.csv')
visited = pd.read_csv('data/survey_visited.csv')

#%% Joins

s2v_merge = survey.merge(visited, how = 'left', 
                         left_on = 'taken',
                         right_on = 'ident') 


s2v2loc_merge = s2v_merge.merge(site, how = 'left', 
                                left_on = 'site', 
                                right_on = 'name')

merged = s2v2loc_merge.merge(person, how = 'left',
                             left_on = 'person',
                             right_on = 'ident')


ps = person.merge(survey, left_on = 'ident', right_on = 'person')
vs = visited.merge(survey, left_on = 'ident', right_on = 'taken')

ps_vs = ps.merge(vs, 
                 left_on = ['ident','taken', 'quant','reading'],
                 right_on = ['person','ident','quant','reading'])
