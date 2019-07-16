#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:03:47 2019

@author: bakunobu
"""


import numpy as np
from read_from_csv import read_and_prepare, np_read_csv, date_conv
from basic_stat_func import vwap, twap



class Asset():
    """The main asset class
    Loads data, support all the main asset stats"""
    
    def __init__(self, name, data_file, new_file):
        self.name = name
        self.data_file = data_file
        self.new_file = new_file

    
    #prepare the data and collect the header
    def prep_and_header(self):
        self.header = read_and_prepare(self.data_file, self.new_file)


    #the hint with column names
    def show_hint(self):
        for x in range(len(self.header)):
            print('{}: {}'.format(x, self.header[x]), end='; ')


    #creates an nparray with dates and a list with weekdays
    def create_dates(self):
        self.dates, self.weekdays = date_conv(self.new_file)

    
    #creates an ndarray with data
    def upload_stock_data(self):
        h = self.header[1:]
        self.stock_data = [np_read_csv(self.new_file,
                                       x+1) for x in range(len(h))]
        self.np_stock_data = np.array(self.stock_data, dtype='f8')

    
    # calculates Volume weighted average price
    def get_vwap(self):
        self.vwap = vwap(self.np_stock_data[-3], self.np_stock_data[-2])
        
    
    def basic_stats(self):
        self.mean = np.zeros(len(self.np_stock_data))
        self.median = np.zeros(len(self.np_stock_data))
        self.variance = np.zeros(len(self.np_stock_data))
        for i in range(len(self.np_stock_data)):
            self.mean[i] = np.mean(self.np_stock_data[i])
            self.median[i] = np.median(self.np_stock_data[i])
            self.variance[i] = np.var(self.np_stock_data[i])


    #calculates time weighted average price
    def get_twap(self):
        self.twap = twap(self.np_stock_data[-3])

    
    def min_and_max(self):
        self.day_dif = self.np_stock_data[4] - self.np_stock_data[3]
        # The ptp function returns the difference between the maximum
        #and minimum values of an array
        self.spread_h = np.ptp(self.np_stock_data[4])
        self.spread_l = np.ptp(self.np_stock_data[3])
    
    
    def print_min_max(self):
         print('Max price: {:0.5f}, min price: {:0.5f}'.format(
                max(self.np_stock_data[4]),
                min(self.np_stock_data[3])))
         print('Max day diff: {:0.5f}, min day diff: {:0.5f}'.format(
                 max(self.day_dif), min(self.day_dif)))
         print('Spread high price {:0.5f}'.format(self.spread_h))
         print('Spread low price {:0.5f}'.format(self.spread_l))
    
    
    def returns(self):
        arr = self.np_stock_data[-3]
        self.returns = np.diff(arr) / arr[:-1]
        self.sigma_sqrd = np.std(self.np_stock_data[-3])
        self.logreturns = np.diff(np.log(self.np_stock_data[-3]))
        self.pos_ret_indexes = np.where(self.returns > 0)
         
        
        
        
    
    
    

        