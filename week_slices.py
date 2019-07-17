#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:42:33 2019

@author: bakunobu
"""


import numpy as np


class DivideToWeeks():
    
    def __init__(self, week_days, dates):
        self.week_days = np.array(week_days)
        self.m_dates = dates
    
    
    def separate(self):
        self.monday = np.ravel(np.where(self.week_days == 0))[0]
        self.friday = np.ravel(np.where(self.week_days == 4))[-1]
        # need a divisor to check how many weeks are there in the month
#        days = abs(self.m_dates[self.monday] - self.m_dates[-1])
#        div = days.astype(int) // 7
        #don't need it really, but it's good way to find timedelta in days
        self.week_ind = np.arange(self.monday, self.friday+1)
        self.week_indices = np.split(self.week_ind, 5)
        