'''
Created on Apr 15, 2013

@author: mstepanenko
'''

'''
High-order function for filtering file content.
'''
def filterContent( it, predicate ):
    
    res = []
    
    for line in it:
        line = line.strip()
        if predicate( line ):
            res.append( line )
    del line
            
    return res 

'''
Composite predicate as a high-order function.
Can be:  'and', 'or' 
'''
def compoundPredicate(combineFunc, *args):
    
    def retFunc(value):        
        res = True
        
        for arg in args:
            res = combineFunc( res, arg(value) )
            
        return res
    
    return retFunc 


def andPredicate(*args):    
    return compoundPredicate( lambda x,y: x and y, *args)

def orPredicate(*args):    
    return compoundPredicate( lambda x,y: x or y, *args)
