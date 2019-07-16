#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:47:30 2019

@author: bakunobu
"""


import csv
import numpy as np
from datetime import datetime


def read_and_prepare(my_file, new_file):
    """The basic csv manipulating class.
    Accepts a file with data, takes a header and returns a file without
    it (digits only).
    An input are two filepathes (filenames), an output is a list
    (contains column names).
    Also creates a file (uses the second argument for naming) that is ready
    for NumPy loadtxt() mainpulations.
    """
    with open(my_file) as df: #a file with data
        reader = csv.reader(df, delimiter=',')
        header = next(reader) #creates a list with column names
        
        #coolects data to be written into new file
        data = []
        for row in reader:
            data.append(row)

    #creates the new datafile for futher manipulations
    with open(new_file, 'w') as nf: #new file with data
        # QUOTE_MINIMAL quoting quotes fields only if they contain
        # the delimiter or the quoterchar
        my_writer = csv.writer(nf, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
        for row in data:
            my_writer.writerow(row)
        
    
    return header #return the header


def np_read_csv(new_file, num_col):
    """
    The loadtxt() manipulating class.
    The input are a filename and a number of a column (int),
    returns an ndarray with data.
    """
    data = np.loadtxt(new_file, delimiter=',',
                      usecols=(num_col,), unpack=True)
    return data


def date_conv(new_file):
    """
    A special function for datetime data processing.
    Accepts a filename, returns an ndarray with dates in datetime64
    format and a list of weekdays.
    """
    with open(new_file) as df:
        reader = csv.reader(df, delimiter=',')
        
        # dates processing
        dates = [] # a container for datetime objects. Do not hold time
        for row in reader:
            dates.append(datetime.strptime(row[0], "%d.%m.%Y"))
        #creates an ndarray with datetime64 date objects (no time)
        np_dates = np.array(dates, dtype='datetime64[D]')
        #creates a list of weekdays using 0-6 int where 0 is Monday
        np_weekdays = [datetime.date(day).weekday() for day in dates] 
    return np_dates, np_weekdays #returns two iterable objects


