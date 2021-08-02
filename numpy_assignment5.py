# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:57:35 2021

@author: BHUVI
"""

import numpy as np
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)
