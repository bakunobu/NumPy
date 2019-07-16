#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:56:50 2019

@author: bakunobu
"""



from asset_class import Asset


data_file = 'gazprom-moscow-exchange.csv'
new_file = 'gazp_prepared.csv'

gazprom = Asset('GAZP', data_file, new_file)

gazprom.prep_and_header()
gazprom.show_hint()
print()
gazprom.upload_stock_data()
gazprom.get_vwap()
gazprom.get_twap()
gazprom.basic_stats()
gazprom.min_and_max()
gazprom.print_min_max()
gazprom.returns()
print(gazprom.returns)

