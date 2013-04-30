
import sys

'''
Don't allow duplicates.
'''
class BSTree(object):


    def __init__(self):
        self.size = 0
        self.root = None
        
    '''
    Get ceil for 'value' from bstree elements.
    time: O(lgN) if tree balanced, or O(N) if not
    space: O(1) 
    '''    
    def ceil(self, value):   
        
        search_value = value + 1     
        ceil_candidate = sys.maxsize
        
        cur = self.root
        
        while cur != None:
            
            if search_value == cur.value:
                return cur.value
            
            if search_value < cur.value:
                ceil_candidate = min(ceil_candidate, cur.value)
                cur = cur.left
            else:                
                cur = cur.right
            
        if ceil_candidate == sys.maxsize:
            ceil_candidate = None
            
        return ceil_candidate 
    
    
    def add(self, value):
        
        if( self.root == None):
            self.root = Node(value)
        else:
            cur = self.root
            
            while(True):
                if cur.value == value:
                    return False
                
                if value > cur.value:
                    if cur.right == None:
                        cur.right = Node(value) 
                        break
                    cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = Node(value)
                        break
                    cur = cur.left 
        
        self.size += 1
        return True
    
    def contains(self, value):
        cur = self.root
        
        while cur != None:
            if cur.value == value:
                return True
            if value > cur.value:
                cur = cur.right
            else:
                cur = cur.left
                
        return False
    
    def get_size(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0
    
    def __repr__(self):
        return "BSTree, size '%s'" % self.size
    
    __str__ = __repr__
    
    
'''
Single node of a binary search tree. 
'''  
class Node(object):
    
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
    def __repr__(self):
        return str(self.value)
    
    __str__ = __repr__



import unittest  
  
class BSTreeTest(unittest.TestCase):
    
    
    def setUp(self):
        self.tree = BSTree()
        self.tree.add(8)  
        self.tree.add(6)
        self.tree.add(12)
        self.tree.add(2)
        self.tree.add(7)
        self.tree.add(11)
        self.tree.add(14)
    
    def test_str(self):
        self.assertEqual("BSTree, size '7'", str(self.tree) )

        
    def test_add(self): 
          
        tree = BSTree()
        
        self.assertTrue( tree.is_empty() )
        self.assertEqual(0, tree.get_size() )
        
        tree.add(8)        
        self.assertFalse( tree.is_empty() )
        self.assertEqual(1, tree.get_size() )
        self.assertTrue( tree.contains(8) )
        
        tree.add(6)
        self.assertFalse( tree.is_empty() )
        self.assertEqual(2, tree.get_size() )
        self.assertTrue( tree.contains(8) )
        self.assertTrue( tree.contains(6) )
        
        tree.add(12)
        tree.add(2)
        tree.add(7)
        tree.add(11)
        tree.add(14) 
        
        self.assertFalse( tree.is_empty() )
        self.assertEqual(7, tree.get_size() )
        self.assertTrue( tree.contains(8) )
        self.assertTrue( tree.contains(6) )  
        self.assertTrue( tree.contains(12) )
        self.assertTrue( tree.contains(2) )
        self.assertTrue( tree.contains(7) )
        self.assertTrue( tree.contains(11) )
        self.assertTrue( tree.contains(14) )     
        
    def test_ceil(self):
        
        self.assertEquals(2, self.tree.ceil(1))
        self.assertEquals(6, self.tree.ceil(2))
        self.assertEquals(6, self.tree.ceil(3))
        self.assertEquals(6, self.tree.ceil(4))        
        self.assertEquals(6, self.tree.ceil(5))
        self.assertEquals(7, self.tree.ceil(6))
        self.assertEquals(8, self.tree.ceil(7))
        self.assertEquals(11, self.tree.ceil(8))
        self.assertEquals(11, self.tree.ceil(9))
        self.assertEquals(11, self.tree.ceil(10))
        self.assertEquals(12, self.tree.ceil(11))
        self.assertEquals(14, self.tree.ceil(12))
        self.assertEquals(14, self.tree.ceil(13))
        self.assertEquals(None, self.tree.ceil(14))
        
if __name__ == "__main__":
    unittest.main()
    