# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:12:04 2018

@author: student
"""

def convertFtoC(tempF):
    temperatureC = 5/9*(float(tempF)-32)
    return temperatureC





tempF = input("Enter a temperature value (in F): ")

tempC = convertFtoC(tempF)

print("Corresponding Temperature in C: ", tempC)




