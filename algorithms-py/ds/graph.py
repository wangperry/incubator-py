import unittest
from StringIO import StringIO
from backtrack.permutations import PermutationsGenerator


class Graph():
    """
    Represent undirected/directed graph as an adjacency list.
    """

    def __init__(self, directed=False):
        self.data = {}
        self.directed = directed
        self.vertexes = 0
        self.edges = 0

    def adj_vertexes(self, ver):
        if not ver in self.data:
            return []
        return [ver for ver in self.data[ver].keys()]
    
    def add_edge(self, ver1, ver2, weight=1):
        
        if not ver1 in self.data:
            self.data[ver1] = {}            
            self.vertexes += 1
            
        if not ver2 in self.data:
            self.data[ver2] = {}            
            self.vertexes += 1

        if not ver1 in self.data[ver2]:
            self.data[ver2][ver1] = Edge(weight)
            self.edges += 1

        if not ver2 in self.data[ver1]:          
            self.data[ver1][ver2] = Edge(weight)
            self.edges += 1

    def has_edge(self, ver1, ver2):
        if ver1 in self.data and ver2 in self.data[ver1]:
            return True

        return False
        
    def __repr__(self):

        buf = StringIO()

        for vertex, adj_list in self.data.items():
            buf.write(str(vertex))
            buf.write(" -> ")
            for index, adj_ver in enumerate(adj_list.keys()):
                if index > 0:
                    buf.write(", ")
                buf.write(str(adj_ver))
            buf.write("\n")

        buf_value = buf.getvalue()
        buf.close()

        return buf_value

    def __vertexes_list(self):
        return [ver for ver in self.data.keys()]
    
    __str__ = __repr__

    def isomorphic(self, other):
        """
        time: O(V!*E)
        space: O(V)
        """
        if self is other:
            return True

        if self.vertexes != other.vertexes or self.edges != other.edges:
            return False

        original_vertexes = self.__vertexes_list()

        other_permutations = PermutationsGenerator(other.__vertexes_list())

        for other_vertexes in other_permutations.get_permutations():

            mapping = {}

            for index in range(len(original_vertexes)):
                mapping[original_vertexes[index]] = other_vertexes[index]

            all_same = True

            for original_ver, other_ver in mapping.items():
                if not self.__same_structure(other, mapping, original_ver, other_ver):
                    all_same = False
                    break

            if all_same:
                return True

        return False

    def __same_structure(self, other_graph, mapping, original_vertex, other_vertex):
        adj_vertexes = self.adj_vertexes(original_vertex)

        adj_mapped = set()

        for ver in adj_vertexes:
            adj_mapped.add(mapping[ver])

        adj_other = set(other_graph.adj_vertexes(other_vertex))

        return adj_mapped == adj_other


class Edge():

    def __init__(self, weight=1):
        self.weight = weight

    def __repr__(self):
        return "weight: %s" % self.weight

    __str__ = __repr__


class GraphTest(unittest.TestCase):

    def test_isomorphic(self):

        graph1 = Graph()
        graph1.add_edge(1, 2)
        graph1.add_edge(1, 3)

        graph2 = Graph()
        graph2.add_edge("A", "B")
        graph2.add_edge("B", "C")

        # check isomorphism symmetry
        self.assertTrue(graph1.isomorphic(graph2))
        self.assertTrue(graph2.isomorphic(graph1))

        # check automorphism
        self.assertTrue(graph1.isomorphic(graph1))
        self.assertTrue(graph2.isomorphic(graph2))

    def test_create_undirected_graph(self):
        graph = Graph()

        self.assertEqual(0, graph.vertexes)
        self.assertEqual(0, graph.edges)
        self.assertFalse(graph.has_edge(1, 2))
        self.assertFalse(graph.has_edge(2, 1))

        graph.add_edge(1, 2)

        self.assertEqual(2, graph.vertexes)
        self.assertEqual(2, graph.edges)
        self.assertTrue(graph.has_edge(1, 2))
        self.assertTrue(graph.has_edge(2, 1))

        graph.add_edge(1, 2)

        self.assertEqual(2, graph.vertexes)
        self.assertEqual(2, graph.edges)
        self.assertTrue(graph.has_edge(1, 2))
        self.assertTrue(graph.has_edge(2, 1))

        graph.add_edge(2, 1)

        self.assertEqual(2, graph.vertexes)
        self.assertEqual(2, graph.edges)
        self.assertTrue(graph.has_edge(1, 2))
        self.assertTrue(graph.has_edge(2, 1))

        self.assertEqual("1 -> 2\n2 -> 1\n", str(graph))


if __name__ == "__main__":
    unittest.main()
