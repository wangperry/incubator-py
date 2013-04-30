import unittest

import random


def array_sum(arr):
    total = 0
    for value in arr:
        total += value
    return total

def create_random_arr(length, values = None):
    
    data = []     
    
    if values == None:
        for _ in range(length):                
            data.append( random.randrange(0, 1000001) )
    else:
        for _ in range(length):                
            data += random.choice(values)
                    
    return data


'''
time: O(n)
space: O(1)
'''
def partition(arr):
    
    blueStart = 0
    whiteStart = 0    
    
    for index in range(len(arr)):
        
        if arr[index] == 'R':
            arr[whiteStart], arr[index] = arr[index], arr[whiteStart]
            whiteStart += 1
            
            arr[blueStart], arr[whiteStart-1] = arr[whiteStart-1], arr[blueStart]
            blueStart += 1
        
        elif arr[index] == 'B':            
            arr[whiteStart], arr[index] = arr[index], arr[whiteStart]
    
            whiteStart += 1
            
'''
time: O(n)
space: O(1)

Do in-place counting sort.
'''
def partition2(arr, values):
    
    
    valueToIndex = {}
    
    for i in range(len(values)):
        valueToIndex[ values[i] ] = i
    
    freq = [0 for _ in range(len(values))]
    
    for value in arr:            
        freq[ valueToIndex[value] ] += 1
            
    baseIndex = 0
            
    for index in range(len(freq)):
        
        elemValue = values[index]
        charFreq = freq[index]
        
        while charFreq > 0:
            arr[baseIndex] = elemValue                
            charFreq -= 1
            baseIndex += 1

    



'''
Find 'mode' element. Element with highest frequency in array.
 
time: O(N)
space: O(N)
'''
def mode(arr): 
    
    if arr == None:
        raise ValueError("NULL array passed")      
       
    freqMap = {}
    
    maxFreq = 0
    modeElem = None
    
    if len(arr) > 0:
        modeElem = arr[0]
        maxFreq = 1
    
    for value in arr:
        
        if value in freqMap:
            curFreq = freqMap[value] + 1
            
            if curFreq > maxFreq:
                maxFreq = curFreq
                modeElem = value
                
            freqMap[value] = curFreq
            
        else:
            freqMap[value] = 1 
    
    return modeElem


class ModeTest(unittest.TestCase):
    
    def testMode(self):
        arr = [ 2, 3, 1, 4, 2, 1, 3, 4, 4 ]
        self.assertEqual( 4, mode( arr ) )
        
        self.assertEqual( 1, mode( [1] ) )
        
        self.assertEqual( None, mode( [] ) )
        
        try:
            self.assertEqual( None, mode( None ) )
            self.fail("ValueError wasn't thrown")
        except ValueError:
            pass



if __name__ == '__main__':
    unittest.main()
