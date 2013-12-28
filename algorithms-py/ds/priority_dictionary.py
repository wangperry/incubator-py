import unittest


class MaxPriorityDictionary:

    def __init__(self, arr):

        if arr is None:
            raise ValueError("NULL array parameter passed to heap")

        self.index_map = {}

        for index, value in enumerate(arr):
            self.index_map[value[0]] = index

        self.data = arr
        self.last = len(arr)
        self.__heapify()

    def __heapify(self):

        index = len(self.data)/2

        while index >= 0:
            self.__fix_down(index)
            index -= 1

    @staticmethod
    def __left(index):
        return (index << 1) + 1

    @staticmethod
    def __right(index):
        return (index << 1) + 2

    @staticmethod
    def __parent(index):
        return index >> 1

    def __fix_down(self, index):

        while index < self.last:

            left = self.__left(index)
            right = self.__right(index)

            if left > self.last and right > self.last:
                break

            max_index = index

            if left < self.last and self.data[left][1] > self.data[index][1]:
                max_index = left

            if right < self.last and self.data[right][1] > self.data[max_index][1]:
                max_index = right

            if max_index == index:
                break

            self.__swap_elements(index, max_index)

            index = max_index

    def __swap_elements(self, from_index, to_index):

        from_value = self.data[from_index][0]
        to_value = self.data[to_index][0]

        self.data[from_index], self.data[to_index] = self.data[to_index], self.data[from_index]

        self.index_map[from_value] = to_index
        self.index_map[to_value] = from_index

    def __fix_up(self, index):

        parent = self.__parent(index)

        while index != 0 and self.data[parent][1] < self.data[index][1]:
            self.__swap_elements(parent, index)
            index = parent
            parent = self.__parent(index)

    def decrease_priority(self, value, offset):
        index = self.index_map[value]
        node = self.data[index]

        self.data[index] = (node[0], node[1] - offset)
        self.__fix_down(index)

    def is_empty(self):
        return self.last == 0

    def size(self):
        return self.last

    def extract_max(self):

        if self.last == 0:
            raise ValueError("Can't extract max value from emtpy priority queue")

        node_value = self.data[0]
        self.data[0] = self.data[self.last-1]
        self.data[self.last-1] = None
        self.index_map.pop(node_value[0], None)

        self.last -= 1

        self.__fix_down(0)

        return node_value[0]

    def __repr__(self):
        return str(self.data)

    __str__ = __repr__


class MaxPriorityDictionaryTest(unittest.TestCase):

    def test_decrease_priority(self):
        q = MaxPriorityDictionary([("s1", 1), ("s2", 2), ("s3", 3), ("s4", 4)])

        self.assertEqual([("s4", 4), ("s2", 2), ("s3", 3), ("s1", 1)], q.data)
        self.assertEqual({"s4": 0, "s2": 1, "s3": 2, "s1": 3}, q.index_map)

        q.decrease_priority("s2", 2)

        self.assertEqual([("s4", 4), ("s1", 1), ("s3", 3), ("s2", 0)], q.data)
        self.assertEqual({"s4": 0, "s2": 3, "s3": 2, "s1": 1}, q.index_map)

        q.decrease_priority("s4", 2)

        self.assertEqual([("s3", 3), ("s1", 1), ("s4", 2), ("s2", 0)], q.data)
        self.assertEqual({"s4": 2, "s2": 3, "s3": 0, "s1": 1}, q.index_map)

    def test_create(self):

        q = MaxPriorityDictionary([("s1", 1), ("s2", 2), ("s3", 3), ("s4", 4)])

        self.assertEqual([("s4", 4), ("s2", 2), ("s3", 3), ("s1", 1)], q.data)

        self.assertEqual({"s4": 0, "s2": 1, "s3": 2, "s1": 3}, q.index_map)

        self.assertEqual(4, q.size())
        self.assertFalse(q.is_empty())

        self.assertEqual("s4", q.extract_max())
        self.assertEqual([("s3", 3), ("s2", 2), ("s1", 1), None], q.data)
        self.assertEqual(3, q.size())
        self.assertFalse(q.is_empty())

        self.assertEqual("s3", q.extract_max())
        self.assertEqual([("s2", 2), ("s1", 1), None, None], q.data)
        self.assertEqual(2, q.size())
        self.assertFalse(q.is_empty())

        self.assertEqual("s2", q.extract_max())
        self.assertEqual([("s1", 1), None, None, None], q.data)
        self.assertEqual(1, q.size())
        self.assertFalse(q.is_empty())

        self.assertEqual("s1", q.extract_max())
        self.assertEqual([None, None, None, None], q.data)
        self.assertEqual(0, q.size())
        self.assertTrue(q.is_empty())
