#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:34:55 2019

@author: bakunobu
"""


import numpy as np

N = int(input('Choose the time gap to calculate ATR: '))
h = []
l = []
close = []



h = h[-N:]
l = l[-N:]
prev_close = close[-N-1:-1]

day_diff = h-l
h_diff = h - prev_close
l_diff = prev_close - l

true_range = np.maximum(day_diff, h_diff, l_diff)


atr = np.zeros(N)


atr[0] = np.mean(true_range)
for i in range(1, N):
    atr[i] = ((N-1) * atr[i-1] + true_range[i]) / N

