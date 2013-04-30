'''
Created on Apr 10, 2013

@author: mstepanenko
'''
import random
from BitVector import BitVector


def random_shuffle(strValue):
    
    arr = list(strValue)
    
    for index in range(len(arr) - 1):
        randIndex = random.randrange(index, len(arr))
        arr[index], arr[randIndex] = arr[randIndex], arr[index] 
    
    return "".join(arr)
    
    

def generateUniqueAscii():
    
    data = [];
        
    for value in range( 33, 127 , 1):        
        data += chr(value)
        
    random.shuffle( data )
            
    return "".join(data);
    

def countingSort(strValue):
    
    bitVector = BitVector( size = 256 ) # 0 - 255
    
    for ch in strValue:
        chValue = ord( ch );
        if bitVector[chValue]:
            raise ValueError("Duplicate character found '%s' in string '%s'" % (ch, strValue) )        
        bitVector[chValue] = True; 
        
    sortedArr = []
        
    for index in range( len(bitVector)):
        if bitVector[index]:
            sortedArr += chr(index)
        
    return "".join(sortedArr);     
    
 
def charsToCodes(strValue):     
    codes = [];
     
     
    for ch in strValue:
        codes += str(ord(ch)) + "_";
        
    return "".join(codes);
        
def isSorted(strValue):
    
    for index in range(1, len(strValue)):
        if strValue[index-1] > strValue[index]:
            return False;
          
    return True;