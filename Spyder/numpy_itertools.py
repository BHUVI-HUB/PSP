# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:35:17 2021

@author: BHUVI
"""

import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))
