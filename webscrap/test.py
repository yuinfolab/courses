#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:08:29 2019

@author: maliozer
@script: informatics workshop

"""

import pandas as pd

df_oscar_man = pd.read_csv("./data.csv", index_col="Index")

#%%


oscar_ages = df_oscar_man['Age']

mean_age_oscar = sum(oscar_ages) / len(oscar_ages)

