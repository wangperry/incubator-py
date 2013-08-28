

'''
Represent directed graph as an adjacency list.
'''
class Graph(object):


    def __init__(self):
        self.data = {}
        self.vertexes = 0
       
        
    
    def add(self, ver1, ver2, weight=1):
        
        if not ver1 in self.data:
            self.data[ver1] = {}            
            self.vertexes += 1
            
        if not ver2 in self.data:
            self.data[ver2] = {}            
            self.vertexes += 1
            
        if not ver2 in self.data[ver1]:          
            self.data[ver1][ver2] = Edge(weight)
            return True
        
        return False
    
    def connected_component(self):
        
        left_vertexes = self.data.copy()
        
        while len(left_vertexes) > 0:
            
            ver = left_vertexes.iterkeys().next()
            
            search_set = self.bfs(ver)
            
            yield ver
                        
            left_vertexes.pop(ver)
        
    def bfs(self, ver):
        pass
        
        
    def __repr__(self):
        
        buf = "vertexes:%s\n" % self.data.keys()
            
        buf += "edges:\n"
        
        for ver, neighbour in self.data.iteritems():
            
            for adj_ver, edge in neighbour.iteritems():            
                buf += ("%s => %s [%s]\n" % (ver, adj_ver, edge.weight))
        
          
        return buf
    
    __str__ = __repr__
            
        
    
    
class Edge(object):
        
    
    def __init__(self, weight = 1):
        self.weight = weight
        