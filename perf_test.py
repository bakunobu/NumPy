#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:45:29 2019

@author: bakunobu
"""

from sum_of_powered import python_gen_sum, numpy_sum, pythonsum 
from chrono_module import find_durationn

n = 100000 # number of iterations
my_funcs = [pythonsum, python_gen_sum, numpy_sum] #list of functions to be tested


for func in my_funcs:
    print(func, find_duration(func, n)[0]) # print an object and time
    
    
