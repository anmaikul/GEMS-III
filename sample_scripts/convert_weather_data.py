# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:24:38 2018

@author: student
"""


import csv

with open("./1400128.csv") as file:
    reader = csv.DictReader(file)
    data = [r for r in reader]
    
    
temps = [(pt['DATE'], pt['DAILYMaximumDryBulbTemp'], pt['DAILYMinimumDryBulbTemp']) for pt in data if pt['DAILYMaximumDryBulbTemp'] != '']    
    
with open('maxtemps.txt', 'w') as file:
    [file.write('{0}\n'.format(t[1])) for t in temps]
