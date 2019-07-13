#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 21:36:22 2019

@author: bakunobu
"""


import csv
import numpy as np
from class_asset import Asset



stock_file = '/home/bakunobu/Documents/gazp_june.csv'

title_file = '/home/bakunobu/Documents/gazp_june_label.csv'

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday']

gazprom = Asset('GAZP', stock_file, title_file)
gazprom.get_data()
gazprom.get_titles()
gazprom.print_hint()
gazprom.calc_basic_stats()
gazprom.min_and_max()
gazprom.returns()
gazprom.volatility()
gazprom.get_date()

days_test = np.array(gazprom.weekdays)
averages = np.zeros(5,)
for i in range(5):
    indices = np.where(days_test==i)
    prices = np.take(gazprom.aver_pr, indices)
    aver = np.mean(prices)
    averages[i] = aver
    print('The average price on {}s was {:0.5f}.'.format(week_days[i], aver))
    top = np.max(averages)
    topday = np.argmax(averages)
    bottom = np.min(averages)
    bottomday = np.argmin(averages)
    print('Top day of the week is {} with price {}'.format(week_days[topday],
          top))
    print('Bottom day of the week is {} with price {}'.format(
            week_days[bottomday], bottom))