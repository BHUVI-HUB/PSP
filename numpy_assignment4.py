# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:45:47 2021

@author: BHUVI
"""

import numpy as np
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)