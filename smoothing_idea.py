# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:03:48 2018

@author: hamed
"""

import numpy as np
import matplotlib.pyplot as plt


n_signal = 10000
chunk_size = 20

x = np.arange(n_signal)
y = 10 * np.sin(0.002 * x) + 0.01 * x
y_noisy = np.array([i + 10 * np.random.rand()  for i in y])

def smoother(x, prev_high):
    n = len(x)
    n_block = n//10
    
    low = np.mean( x[0:n_block] )
    low = (9 * low+prev_high)/10.
    high= np.mean( x[-1:-n_block:-1] )
    
    x = np.array( [low + i*1.*(high-low)/n_block for i in range(n)])
    return x, high
        
y_cleaned = np.zeros(n_signal)

prev_high = np.mean(y_noisy[:chunk_size])

for i in range(len(y_noisy)//chunk_size - 1):
    y_temp, prev_high = smoother( y_noisy[ i*chunk_size:(i+1)*chunk_size ], prev_high  )
    y_cleaned[ i*chunk_size:(i+1)*chunk_size ] = y_temp
    
    
#%%
plt.figure()
plt.plot(y_noisy)
plt.figure()
plt.plot(y_cleaned, 'r')