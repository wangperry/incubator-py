'''
Created on Feb 12, 2013

@author: mstepanenko
'''


'''
Fibonacci sequence generator
'''
def fib():
    a = 1
    b = 1
    
    while True:
        yield a
        a, b = b, a+b
  
'''
Number of combination 'k' from 'n' elements set.
''' 
def combinationsCount(k, n):
    
    val = n - k + 1
    mul = 1
    
    while val <= n:
        mul *= val
        val += 1
    
    
    return int( mul / factorial(k) )
   
        
def permutationsCount(val):
    if val <= 0:
        raise ValueError("Number of permutations can be generated only for positive value not '%s'" % val )
    
    return factorial(val)
    
        
'''
Calculate factorial
'''
def factorial(n):
    
    if n < 0:
        raise ValueError(" Can't calculate factorial for negative value: %s" % n)
    
    res = 1
    
    while n > 1:
        res *= n
        n -= 1
        
    return res
         
    

if __name__ == '__main__':
    pass