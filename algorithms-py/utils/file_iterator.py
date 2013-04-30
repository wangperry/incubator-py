'''
Created on Apr 15, 2013

@author: mstepanenko
'''
class FileIterator(object):
    
    def __init__(self, filePath):
        self.__data = open(filePath).readlines()
        self.__index = 0
        self.__length = len(self.__data)        
        
    def __next__(self):
        
        if self.__index < self.__length:            
            self.__index += 1            
            return self.__data[self.__index-1]
        
        raise StopIteration
    
    def __iter__(self):
        return self
