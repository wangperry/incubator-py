
import unittest


class BsTree:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0


class BsTreeTest(unittest.TestCase):

    def test_add(self):
        tree = BsTree()
        self.assertTrue( tree.is_empty() )
        self.assertEqual( 0, tree.size() )


if __name__ == "__main__":
    unittest.main()


