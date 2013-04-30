   
from functools import lru_cache

from geolocation.geo_utils import *

@lru_cache(maxsize = None)
def numOfWays(dices, max_dice_value, base_sum):  
    
    if base_sum == 0:
        return 0
    
    if base_sum > max_dice_value * dices:
        return 0 
    
    if base_sum == dices or (dices == 1 and base_sum < max_dice_value):
        return 1
  
    total = 0
    
    for val in range(1, min(max_dice_value, base_sum) + 1): 
        
        if val > base_sum:
            break
                 
        if (base_sum - val) == 0 and dices == 1:
            total += 1        
        else:        
            total += numOfWays(dices-1, max_dice_value, base_sum - val)

    return total






def main():  
    
    aalborg = City("Aalborg, Denmark", +57.09700, +9.85000)
    
    print(aalborg)
    
    
#    dicesCount = 3  
#    maxDiceValue = 6
#    
#    
#    for sumToCheck in range(dicesCount, dicesCount*maxDiceValue + 1):      
#    
#        actualCount = numOfWays(dicesCount, maxDiceValue, sumToCheck)   
#        
#        expectedCount = 0
#        dices = [1,1,1]
#        
#        for val1 in range(1, 7):
#            for val2 in range(1, 7):
#                for val3 in range(1, 7):
##                    for val4 in range(1, 7):
#                    dices[0] = val1
#                    dices[1] = val2  
#                    dices[2] = val3  
##                        dices[3] = val4  
#                     
#                    if array_sum(dices) == sumToCheck:
#    #                    print( dices )     
#                        expectedCount += 1 
#         
#
#        if actualCount != expectedCount:  
#            print("NOT MATCHED: No of ways (%s) =  %s with '%s' dices"  % (sumToCheck, actualCount, dicesCount)  )  
#            print( "Actual count: %s"  % (expectedCount)  )
             
    print("main done")

if __name__ == '__main__':
    main()