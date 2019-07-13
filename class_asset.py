#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 07:03:50 2019

@author: bakunobu
"""


import csv
import numpy as np
from datetime import datetime


class Asset():
    """A main asset data class"""
    def __init__(self, name, data_file, titles):
        self.name = name
        self.data_file = data_file
        self.titles = titles
    
    def get_data(self):
        """load data from csv"""
        self.aver_pr, self.total = np.loadtxt(self.data_file, delimiter=',',
                                    usecols=(7, 8), unpack=True)    

    
    def get_titles(self):
        """loads title from another csv"""
        with open(self.titles, 'r') as tf:
            reader = csv.reader(tf, delimiter=',')
            self.header_row = next(reader)
    
    
    def get_date(self):
        """Loads dates and converts it to NumPy datetime64 format"""
        with open(self.data_file, 'r') as df:
            reader = csv.reader(df, delimiter=',')
            
            dates = []
            for row in reader:
                dates.append(datetime.strptime(row[0], "%d.%m.%Y"))
            self.dates = np.array(dates, dtype='datetime64[D]')
            self.weekdays = [datetime.date(day).weekday() for day in 
                             dates]
            print(self.dates[0])
            
    
    
    def print_hint(self):
        """prints titles and indexes"""
        for title in self.header_row:
            print(f'{title}: {self.header_row.index(title)}, ', end=' ')
    
    
    def calc_basic_stats(self):
        """calculates some basic statistic parameters"""
        # calculates Volume weighted average price
        self.vwap = np.average(self.aver_pr, weights=self.total)
        print('VWAP = {:0.5f}'.format(self.vwap))
        #calculates time weighted average price
        t = np.arange(len(self.aver_pr)) #to get a series
        self.twap = np.average(self.aver_pr, weights=t)
        print('TWAP = {:0.5f}'.format(self.twap))
        #calculates mean
        self.mean = np.mean(self.aver_pr)
        print('Mean = {:0.5f}'.format(self.mean))
        #calculates median
        self.median = np.median(self.aver_pr)
        print('Median = {:0.5f}'.format(self.median))
        #calculates variance
        self.variance = np.var(self.aver_pr)
        print('Variance = {:0.5f}'.format(self.variance))

        
    
    def min_and_max(self):
        """finds minimimum and maximum price for each day"""
        self.p_min, self.p_max = np.loadtxt(self.data_file, delimiter=',',
                                    usecols=(4, 5), unpack=True)
        self.day_dif = self.p_max - self.p_min
        print('Max price: {:0.5f}, min price: {:0.5f}'.format(
                max(self.p_max), min(self.p_min)))
        print('Max day diff: {:0.5f}, min day diff: {:0.5f}'.format(
                max(self.day_dif), min(self.day_dif)))
        # The ptp function returns the difference between the maximum
        #and minimum values of an array
        print('Spread high price {:0.5f}'.format(np.ptp(self.p_max)))
        print('Spread low price {:0.5f}'.format(np.ptp(self.p_min)))
        
    
    def returns(self):
        self.returns = np.diff(self.aver_pr) / self.aver_pr[:-1]
        self.sigma_sqrd = np.std(self.returns)
        self.logreturns = np.diff(np.log(self.aver_pr))
        self.pos_ret_indexes = np.where(self.returns > 0)


    def volatility(self):
        self.ann_vol = np.std(self.logreturns) / np.mean(self.logreturns)
        self.ann_vol_d = self.ann_vol / np.sqrt(1./252.)
        self.mon_vol = self.ann_vol_d * np.sqrt(1./12.)
        print('Volatility:')
        print('Monthly = {:0.5f}'.format(self.mon_vol))
        print('Annually = {:0.5f}'.format(self.ann_vol_d))
        


        
        