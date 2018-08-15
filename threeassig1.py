"""
This program compute the area of a sector
and display result
"""
#import math function
from math import pi
#Input angle value
teta = float(input('Enter Value for Angle: '))
#input radius value
radius = float(input('Enter Value for radius: '))
#calculate Area 
area = (teta/360) * pi * radius * radius
#print Area
print('The area of the sector is',area)
