#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:36:22 2019

@author: bakunobu
"""


import csv
import numpy as np

stock_file = '/home/bakunobu/Documents/gazp_june.csv'



c, v = np.loadtxt(stock_file, delimiter=',', usecols=(2, 3), unpack=True) 

title_file = '/home/bakunobu/Documents/gazp_june_label.csv'

with open(title_file, 'r') as tf:
    reader = csv.reader(tf, delimiter=',')
    header_row = next(reader)
    
