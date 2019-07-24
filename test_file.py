#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:56:50 2019

@author: bakunobu
"""



from asset_class import Asset
from week_slices import DivideToWeeks
from summarize import summarize
import numpy as np
from moving_average import sma, ema, bollinger_bands


data_file = 'gazprom-moscow-exchange.csv'
new_file = 'gazp_prepared.csv'

gazprom = Asset('GAZP', data_file, new_file)

gazprom.prep_and_header()
gazprom.show_hint()
print()
gazprom.upload_stock_data()
gazprom.create_dates()
gazprom.get_vwap()
gazprom.get_twap()
gazprom.basic_stats()
gazprom.min_and_max()
gazprom.print_min_max()
gazprom.returns()
#print(gazprom.returns)
gazprom.volatility()
gazprom.week_stats()

may = DivideToWeeks(gazprom.weekdays, gazprom.dates)
may.separate()

week_summary = np.apply_along_axis(summarize, 1, may.week_indices,
                                   gazprom.stock_data[2],
                                   gazprom.stock_data[4],
                                   gazprom.stock_data[3],
                                   gazprom.stock_data[5])




np.savetxt('weeksummary.csv', week_summary, delimiter=',', fmt='%s')


n = int(input('Type in the length of the interval (in days): '))
sma(gazprom.stock_data[5], n)
ema(gazprom.stock_data[5], n)
bollinger_bands(gazprom.stock_data[5], n)
