import unittest

var = '''
Unbalanced binary search tree.
Don't allow to store None values.
'''


class BsTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__root is None


    def delete(self, value):

        if value is None:
            return False

        if self.__root is None:
            return False

        node = self.__find_node(value)

        if node is None:
            return False

        self.__delete_node(node)

        self.__size -= 1


    def __delete_node(self, node):

        # leaf node
        if node.is_leaf():
            parent = node.parent
            node.parent = None

            if parent.left is node:
                parent.left = None
            else:
                parent.right = None

        # has only 1 child
        elif node.has_one_child():
            child_node = node.first_not_null_child()
            child_node.parent = node.parent

            if node is self.__root:
                self.__root = child_node
            else:
                if node.parent.left is node:
                    node.parent.left = child_node
                else:
                    node.parent.right = child_node

            node.parent = None
            node.left = None
            node.right = None

        # has 2 children
        else:
            min_from_right = node.right
            while min_from_right.left is not None:
                min_from_right = min_from_right.left

            self.__delete_node(min_from_right)

            min_from_right.parent = node.parent

            if self.__root is node:
                self.__root = min_from_right
            else:
                if node.parent.left is node:
                    node.parent.left = min_from_right
                else:
                    node.parent.right = min_from_right

            min_from_right.left = node.left

            if node.left is not None:
                node.left.parent = min_from_right

            if node.right is not None:
                node.right.parent = min_from_right

            min_from_right.right = node.right

            node.parent = None
            node.left = None
            node.right = None



    def min(self):
        if self.__root is None:
            return None

        cur = self.__root

        while cur.left is not None:
            cur = cur.left

        return cur.value

    def max(self):
        if self.__root is None:
            return None

        cur = self.__root

        while cur.right is not None:
            cur = cur.right

        return cur.value

    def add(self, value):

        if self.__root is None:
            self.__root = Node(value)
        else:
            parent = self.__find_parent_node(value)

            if value < parent.value:
                if parent.left is not None:
                    parent.left.parent = None
                parent.left = Node(value, parent)
            else:
                if parent.right is not None:
                    parent.right.parent = None
                parent.right = Node(value, parent)

        self.__size += 1

    def contains(self, value):
        if value is None:
            return False

        if self.__root is None:
            return False

        node = self.__find_node(value)

        return node is not None

    def __find_node(self, value):

        parent = self.__find_parent_node(value)

        if parent is None:
            return None

        # root node case
        if parent.value == value:
            return parent

        # other nodes cases
        if value < parent.value:
            return parent.left

        return parent.right


    def __find_parent_node(self, value):

        if value is None:
            return None

        parent = self.__root
        cur = self.__root

        while cur is not None:
            if cur.value == value:
                return parent

            parent = cur

            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        return parent


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_one_child(self):
        return bool(self.left is None) ^  bool(self.right is None)

    def first_not_null_child(self):
        if self.left is not None:
            return self.left
        return self.right

    def __repr__(self):
        return str(self.value)

    __str__ = __repr__


class BsTreeTest(unittest.TestCase):

    def test_delete_with_two_children(self):
        tree = BsTree()
        tree.add(8)
        tree.add(6)
        tree.add(7)
        tree.add(10)
        tree.add(4)
        tree.add(3)
        tree.add(12)

        tree.delete(6)
        self.assertFalse(tree.is_empty())
        self.assertEqual(6, tree.size())

        self.assertTrue(tree.contains(8))
        self.assertFalse(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(12))

        tree.delete(8)
        self.assertFalse(tree.is_empty())
        self.assertEqual(5, tree.size())

        self.assertFalse(tree.contains(8))
        self.assertFalse(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(12))

    def test_delete_with_one_child(self):
        tree = BsTree()
        tree.add(8)
        tree.add(6)
        tree.add(10)
        tree.add(4)
        tree.add(3)
        tree.add(12)

        tree.delete(4)
        self.assertFalse(tree.is_empty())
        self.assertEqual(5, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertFalse(tree.contains(4))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(12))

        tree.delete(10)
        self.assertFalse(tree.is_empty())
        self.assertEqual(4, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(6))
        self.assertFalse(tree.contains(10))
        self.assertFalse(tree.contains(4))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(12))



    def test_delete_leaf(self):
        tree = BsTree()
        tree.add(8)
        tree.add(6)
        tree.add(10)
        tree.add(4)
        tree.add(3)
        tree.add(5)

        tree.delete(3)
        self.assertFalse(tree.is_empty())
        self.assertEqual(5, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(4))
        self.assertFalse(tree.contains(3))
        self.assertTrue(tree.contains(5))

        tree.delete(5)
        self.assertFalse(tree.is_empty())
        self.assertEqual(4, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(4))
        self.assertFalse(tree.contains(3))
        self.assertFalse(tree.contains(5))

        tree.delete(4)
        tree.delete(6)

        self.assertFalse(tree.is_empty())
        self.assertEqual(2, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertFalse(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertFalse(tree.contains(4))
        self.assertFalse(tree.contains(3))
        self.assertFalse(tree.contains(5))


    def test_add(self):
        tree = BsTree()
        self.assertTrue(tree.is_empty())
        self.assertEqual(0, tree.size())

        self.assertFalse(tree.contains(8))
        self.assertFalse(tree.contains(6))
        self.assertFalse(tree.contains(10))
        self.assertFalse(tree.contains(4))
        self.assertFalse(tree.contains(3))
        self.assertFalse(tree.contains(5))

        self.assertEqual(None, tree.min())
        self.assertEqual(None, tree.max())

        tree.add(8)
        self.assertEqual(8, tree.min())
        self.assertEqual(8, tree.max())

        self.assertFalse(tree.is_empty())
        self.assertEqual(1, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertFalse(tree.contains(6))
        self.assertFalse(tree.contains(10))
        self.assertFalse(tree.contains(4))
        self.assertFalse(tree.contains(3))
        self.assertFalse(tree.contains(5))

        tree.add(6)
        self.assertEqual(6, tree.min())
        self.assertEqual(8, tree.max())

        tree.add(10)
        self.assertEqual(6, tree.min())
        self.assertEqual(10, tree.max())

        tree.add(4)
        self.assertEqual(4, tree.min())
        self.assertEqual(10, tree.max())

        tree.add(3)
        self.assertEqual(3, tree.min())
        self.assertEqual(10, tree.max())

        tree.add(5)
        self.assertEqual(3, tree.min())
        self.assertEqual(10, tree.max())

        self.assertFalse(tree.is_empty())
        self.assertEqual(6, tree.size())
        self.assertTrue(tree.contains(8))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(5))


if __name__ == "__main__":
    unittest.main()
