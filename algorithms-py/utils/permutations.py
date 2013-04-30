'''
Created on Mar 1, 2013

@author: mstepanenko
'''

'''
Generate permutations with 'min change' property
'''
def generatePermutations(value):
    data = []
    
    for i in range(1, value + 1, 1):
        data.append(i)
        
    return __genPermForSet(data)



def __genPermForSet(data):
    
    if len(data) == 1:
        return [data]
    
    baseValue = data[0]    
    perms = __genPermForSet( data[1:] )
    
    allPerms = []
    
    index = 0
    for singlePerm in perms:
                
        # even
        if (index & 1) == 0:
            singlePerm = [baseValue] + singlePerm
            allPerms.append( singlePerm[:] )
            lastIndex = 1
            
            while lastIndex < len(singlePerm):
                singlePerm[lastIndex-1], singlePerm[lastIndex] = singlePerm[lastIndex], singlePerm[lastIndex-1]
                allPerms.append( singlePerm[:] )
                lastIndex += 1            
        #odd
        else:
            
            singlePerm.append( baseValue )            
            allPerms.append( singlePerm[:] )
            
            lastIndex = len( singlePerm ) - 2
            
            while lastIndex >= 0:                
                singlePerm[lastIndex], singlePerm[lastIndex+1] = singlePerm[lastIndex+1], singlePerm[lastIndex]
                allPerms.append( singlePerm[:] )
                
                lastIndex -= 1            
        
        index += 1
        
        
    return allPerms
    
    
