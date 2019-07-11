#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:52:20 2019

@author: bakunobu
"""


import numpy as np


b = np.arange(24)
print(b)
b = b.reshape((2, 3, 4))
print(b)
print(b.shape)
#first element
print(b[0,0,0])
#first elements in both matrixes
print(b[:,0,0])
#first matrix
print(b[0, :, :])
#or
print(b[0])
#or even
print(b[0, ...])
#adding step
print(b[0,1,::2])
#for any column
print(b[0,::2,-1])
#second column
print(b[:,:,1])
#or
print(b[..., 1])
#second row
print(b[:, 1])
#negative indexin works too
print(b[0, :, -1])
#and reverse
print(b[0,::-1, -1])
#just reverse for matrices, not all the elements
print(b[::-1])