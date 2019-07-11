#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:14:30 2019

@author: bakunobu
"""

import numpy as np

# creating an array
my_array =np.array([np.arange(2), np.arange(2)])

my_3x3_array = np.array([np.arange(3), np.arange(3), np.arange(3)])


#creating an array of a current tupe
my_float_array = np.array(np.arange(7), dtype='float')
#using a shorter names of types
my_f_array = np.array(np.arange(7), dtype='d') #f for float32, d or f8 for float64
my_complex_array = np.array(np.arange(7), dtype='D')
