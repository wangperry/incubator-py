        
'''
A array of N elements, we have to replace all the elements 
with nearest greater which is present on the right side of 
that elements. O(n) is required

time: O(N)
space: O(N)
'''  
def nearestGreater(arr):
    
    stack  = []        
    
    for i in range( len(arr)-1, -1, -1 ):
        
        temp = arr[i]
        
        while True:            
            if len(stack) == 0:
                arr[i] = -1
                stack.append(temp)               
                break
                          
            max_val = stack.pop()
                
            if max_val > temp:
                arr[i] = max_val
                stack.append(max_val)
                stack.append(temp)
                break
            
    arr[len(arr)-1] = -1
    
    

def main():
    
    
#    arr = [3,5,7,6,8,4,9]

    arr = [16, 17, 4, 3, 5, 2]
 
#  then it should be modified to {17, 5, 5, 5, 2, -1}.  
    
    nearestGreater(arr)

    print( arr )

    print("main done")

if __name__ == '__main__':
    main()