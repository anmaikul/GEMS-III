# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:47:13 2018

@author: Michael An
"""

def find_max(number_list):
    max_value = -1

    for number in number_list:
        if number > max_value:
            max_value = number            

    return max_value



# Tests for the function find_max
test_list = [1, 2, 3, 4]


print(find_max(test_list) == 1)