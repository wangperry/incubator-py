
from ds.graph import Graph

def main():
    
    graph = Graph()
    
    graph.add(1, 2, 12)
    graph.add(1, 3, 13)
    graph.add(3, 1, 31)
    
    for comp in graph.connected_component():
        print( comp ) 
    
    print( graph )        
    
    print("main done")
    


if __name__ == '__main__':
    main()