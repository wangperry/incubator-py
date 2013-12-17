

class LinkedList(object):
    """
    Single linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        self.add_last(value)
        
    def pop(self):
        return self.remove_last()
    
    def enqueue(self, value):
        self.add_last(value)
        
    def deque(self):
        return self.remove_first()

    def remove_first(self):
        
        self.__check_empty()
        
        if self.head == self.tail:
            ret_value = self.head.value
            self.head = self.tail = None
        else: 
            old_head = self.head
            ret_value = self.head.value
            
            self.head = self.head.next
            old_head.clear()
        
        self.size -= 1
        
        return ret_value
    
    def remove_last(self):
        
        self.__check_empty()
        
        if self.head == self.tail:
            ret_value = self.head.value
            self.head = self.tail = None
        else:    
            
            # not very optimal, cause we need to traverse the whole  list to find pre last element   
            cur = self.head
            
            while cur.next != self.tail:
                cur = cur.next
                
            ret_value = cur.next.value
                
            cur.next = None
            self.tail = cur
            
        self.size -= 1
        
        return ret_value
       
    def __check_empty(self):
        if self.size == 0:
            raise ValueError("Stack is empty") 

    def add_last(self, value):
        """ Add to the end of list"""
        
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next 
            
        self.size += 1

    def add_first(self, value):
        """
        Add to the beginning of list.
        """
        
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            
        self.size += 1

    def __repr__(self):
        str_buf = ""
        
        cur = self.head
        
        while cur:
            str_buf += str(cur.value) + ","
            cur = cur.next
            
        return str_buf

    __str__ = __repr__
    
    
class Node(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
        
    def clear(self):
        self.value = None
        self.next = None
        
    def __repr__(self):
        return str(self.value)
    
    __str__ = __repr__