'''
Created on Jul 31, 2013

@author: mstepanenko
'''

class User(object):


    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname 
        self.age = age 
        
        
    def __hash__(self):
        return hash( (self.surname, self.name) )
    
    def __eq__(self, other):
        return (self.surname, self.name) == (other.surname, other.name)
        
    def __repr__(self):
        return "%s %s, age: %s" % (self.name, self.surname, self.age) 
    
    __str__ = __repr__
        