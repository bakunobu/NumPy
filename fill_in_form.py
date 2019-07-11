#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:06:04 2019

@author: bakunobu
"""


import numpy as np

# a template
t = np.dtype([('name', 'str', 40), #do not forget to enclose data types with ''
           ('numitems', 'int32'),
           ('price', 'float32')])


# adding data
my_items = np.array([('Meaning of life DVD', 42, 3.14),
                     ('Butter', 13, 2.72)], dtype=t)


print(* my_items)