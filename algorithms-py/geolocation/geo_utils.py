'''
Map projection functions.
'''

import math

SCALE_FACTOR = 6378137

def longituda_to_x(longituda):
    return longituda * (math.pi() / 180) * SCALE_FACTOR

def x_to_longituda(x):
    return x / (math.pi()/180) / SCALE_FACTOR 

def y_to_latituda(y):
    return 180.0/math.pi * (2.0 * math.atan(math.exp(y*math.pi/180.0)) - math.pi/2.0)

def latituda_to_y(latituda):
    return 180.0/math.pi * math.log(math.tan(math.pi/4.0 + latituda*(math.pi/180.0)/2.0))


#  Read all cities from 'http://www.golombek.com/locations.html'
class City(object):
    
#Aalborg, Denmark        +57.09700         +9.85000
    
    def __init__(self, name, longituda, latituda):
        self.name = name
        self.longituda = longituda
        self.latituda = latituda
        
    def __repr__(self):
        return "%s (%s, %s)" % (self.name, self.longituda, self.latituda)
    
    __str__ = __repr__
