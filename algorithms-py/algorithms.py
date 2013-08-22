
from ds.linked_list import LinkedList


def main():
    
    data = LinkedList()
    
    for val in range(10):
        data.enqueue(val)
        
        
    while not data.isEmpty():
        print( data.deque() )
        
    
    print("main done")
    


if __name__ == '__main__':
    main()