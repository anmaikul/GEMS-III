# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:16:39 2018

@author: student
"""

def convertFtoC(tempF):
    temperatureC = 5/9*(float(tempF)-32)
    return temperatureC




stream_handler = open("../data/maxtemps.txt", "r")

all_data = stream_handler.read()

number_list = all_data.rstrip().split("\n")


float_list = [] 
for number in number_list:
    float_list.append(float(number))


float_list_C = []
for tempF in float_list:
    float_list_C.append(convertFtoC(tempF))
    

