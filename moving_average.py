#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:24:55 2019

@author: bakunobu
"""


import numpy as np
import matplotlib.pyplot as plt


def sma(data_list, n):
    weights = np.ones(n) / n
    sma = np.convolve(weights, data_list)[n-1: -n+1]
    t = np.arange(n-1, len(data_list))
    plt.plot(t, data_list[n-1:], lw=1.0)
    plt.plot(t, sma, lw=2.0)
    plt.show()
    return sma


def ema(data_list, n):
    weights = np.exp(np.linspace(-1., 0., n))
    weights /= weights.sum() #normalization
    ema = np.convolve(weights, data_list)[n-1: -n+1]
    t = np.arange(n-1, len(data_list))
    plt.plot(t, data_list[n-1:], lw=1.0)
    plt.plot(t, ema, lw=2.0)
    plt.show()
    

def bollinger_bands(data_list, n):
    my_sma = sma(data_list, n)
    deviation = []
    c = len(data_list)
    for i in range(n-1, c):
        if i + n < c:
            dev = data_list[i: i + n]
        else:
            dev = data_list[-n:]
        
        
        averages = np.zeros(n)
        averages.fill(my_sma[i - n - 1])
        dev = dev - averages
        dev = dev ** 2
        dev = np.sqrt(np.mean(dev))
        deviation.append(dev)
    
    deviation = 2 * np.array(deviation)
    upper_bb = my_sma + deviation
    lower_bb = my_sma - deviation
    t = np.arange(n-1, c)
    plt.plot(t, data_list[n-1:], lw=1.0)
    plt.plot(t, my_sma, lw=2.0)
    plt.plot(t, upper_bb, lw=3.0)
    plt.plot(t, lower_bb, lw=4.0)
    plt.show
        
                