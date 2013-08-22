'''
Single linked list
'''

class LinkedList(object):


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    
    def push(self, value):
        self.addLast(value)
        
    def pop(self):
        return self.removeLast()
    
    def enqueue(self, value):
        self.addLast(value)
        
    def deque(self):
        return self.removeFirst()
    
    
    def removeFirst(self):
        
        self._checkEmpty()
        
        retValue = None
        
        if self.head == self.tail:
            retValue = self.head.value
            self.head = self.tail = None
        else: 
            oldHead = self.head
            retValue = self.head.value
            
            self.head = self.head.next
            oldHead.clear()         
        
        self.size -= 1
        
        return retValue
    
    def removeLast(self):
        
        self._checkEmpty()
        
        retValue = None
        
        if self.head == self.tail:
            retValue = self.head.value
            self.head = self.tail = None
        else:    
            
            # not very optimal, cause we need to traverse the whole  list to find pre last element   
            cur = self.head
            
            while cur.next != self.tail:
                cur = cur.next
                
            retValue = cur.next.value
                
            cur.next = None
            self.tail = cur
            
        self.size -= 1
        
        return retValue
       
    def _checkEmpty(self):
        if self.size == 0:
            raise ValueError("Stack is empty") 
    
    '''
    Add to the end of list
    '''
    def addLast(self, value):
        
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next 
            
        self.size += 1
        
    '''
    Add to the beginning of list
    '''
    def addFirst(self, value):
        
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value, self.head)
            self.head = newNode 
            
        self.size += 1


    def __repr__(self):
        strBuf = ""
        
        cur = self.head
        
        while cur:
            strBuf += str(cur.value) + ","
            cur = cur.next
            
        return strBuf         
    

    __str__ = __repr__
    
    
class Node(object):
    
    
    
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
    def clear(self):
        self.value = None
        self.next = None
        
    def __repr__(self):
        return str(self.value)
    
    __str__ = __repr__