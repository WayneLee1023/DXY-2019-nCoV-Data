# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:25:32 2020

@author: lw_bu
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.optimize import curve_fit
import numpy as np
 
def exp_fit(t, A, tao):
    return A*np.exp(-t/tao)

import csv

data = []
with open('DXYArea.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            title = row
            print('Column names are,'.join(row))
            line_count += 1
        else:
            data.append(row)
            line_count += 1
    print(f'Processed {line_count} lines.')
    
