import unittest


class Graph:

    def __init__(self):
        self.data = {}

    def add_edge(self, ver1, ver2):

        if not ver1 in self.data:
            self.data[ver1] = set()

        if not ver2 in self.data:
            self.data[ver2] = set()

        self.data[ver1].add(ver2)
        self.data[ver2].add(ver1)

    def has_edge(self, ver1, ver2):
        if ver1 in self.data and ver2 in self.data:
            return ver2 in self.data[ver1]
        return False


class GraphTest(unittest.TestCase):


    def test_add_edge(self):
        graph = Graph()

        self.assertFalse(graph.has_edge(1, 2))
        self.assertFalse(graph.has_edge(2, 1))

        graph.add_edge(1, 2)


        self.assertTrue(graph.has_edge(1, 2))
        self.assertTrue(graph.has_edge(2, 1))




if __name__ == "__main__":
    unittest.main()
