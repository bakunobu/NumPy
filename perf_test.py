#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:45:29 2019

@author: bakunobu
"""

from sum_of_powered import python_gen_sum, numpy_sum, python_sum
from chrono_module import find_duration

bare_python = find_duration(python_sum(5000000))
gen_python = find_duration(python_gen_sum(5000000))
numpy_python = find_duration(numpy_sum(5000000))

print(f'{bare_python} \n {gen_python} \n {numpy_python}')
