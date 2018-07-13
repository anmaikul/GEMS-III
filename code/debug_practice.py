# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:47:13 2018

@author: student
"""

def find_max(number_list):
    max_value = -1

    for number in number_list:
        if number > max_value:
            max_value = number            
            













import csv

with open("./1400128.csv") as file:
    reader = csv.DictReader(file)
    data = [r for r in reader]
    
    
temps = [(pt['DATE'], pt['DAILYMaximumDryBulbTemp'], pt['DAILYMinimumDryBulbTemp']) for pt in data if pt['DAILYMaximumDryBulbTemp'] != '']    
    
with open('maxtemps.txt', 'w') as file:
    [file.write('{0}\n'.format(t[1])) for t in temps]
