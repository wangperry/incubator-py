import unittest
from collections import deque


class BoundedPriorityQueue:
    """
    Min bounded priority queue.
    """

    MAX_QUEUE_CAPACITY = 1024

    def __init__(self, max_value):
        if max_value > BoundedPriorityQueue.MAX_QUEUE_CAPACITY:
            raise ValueError("maxValue = %s is too big for BoundedPriorityQueue, should be less or equals to %s" %
                             (str(max_value), str(BoundedPriorityQueue.MAX_QUEUE_CAPACITY)))
        self.__size = 0
        self.__top = max_value + 2
        self.__max_key = max_value
        self.__data = [deque() for _ in range(max_value+1)]

    def add(self, key, value):

        if key < 0:
            raise ValueError("Negative key passed, %s" % str(key))
        if key > self.__max_key:
            raise ValueError("key = %s is too big, should be less or equals to %s" % (str(key), str(self.__max_key)))

        index = int(key)

        if self.__data[index] is None:
            self.__data[index] = deque(value)
        else:
            self.__data[index].append(value)

        self.__top = min(self.__top, index)
        self.__size += 1

    def find_min(self):
        if self.__size == 0:
            raise IndexError("Queue is empty")

        return self.__data[self.__top][0]

    def extract_min(self):
        if self.__size == 0:
            raise IndexError("Queue is empty")

        bucket_data = self.__data[self.__top]

        min_value = bucket_data.popleft()

        if len(bucket_data) == 0:
            # only one element left
            if self.__size == 1:
                self.__top = self.__max_key+2
            else:
                while len(self.__data[self.__top]) == 0:
                    self.__top += 1

        self.__size -= 1

        return min_value

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0


class BoundedPriorityQueueTest(unittest.TestCase):

    def testCreateBigQueue(self):
        with self.assertRaises(ValueError):
            BoundedPriorityQueue(10000)

    def testAdd(self):
        q = BoundedPriorityQueue(10)
        self.assertTrue(q.is_empty())
        self.assertEqual(0, q.get_size())

        with self.assertRaises(IndexError):
            q.extract_min()

        with self.assertRaises(IndexError):
            q.find_min()

        q.add(5, "5")
        self.assertEqual("5", q.find_min())

        q.add(4, "4")
        self.assertEqual("4", q.find_min())

        q.add(8, "8")
        self.assertEqual("4", q.find_min())

        q.add(3, "3")
        self.assertEqual("3", q.find_min())

        q.add(5, "5.2")
        self.assertEqual("3", q.find_min())

        q.add(5, "5.3")
        self.assertEqual("3", q.find_min())

        self.assertFalse(q.is_empty())
        self.assertEqual(6, q.get_size())

        self.assertEqual("3", q.extract_min())
        self.assertFalse(q.is_empty())
        self.assertEqual(5, q.get_size())
        self.assertEqual("4", q.find_min())

        self.assertEqual("4", q.extract_min())
        self.assertFalse(q.is_empty())
        self.assertEqual(4, q.get_size())
        self.assertEqual("5", q.find_min())

        self.assertEqual("5", q.extract_min())
        self.assertFalse(q.is_empty())
        self.assertEqual(3, q.get_size())
        self.assertEqual("5.2", q.find_min())

        self.assertEqual("5.2", q.extract_min())
        self.assertFalse(q.is_empty())
        self.assertEqual(2, q.get_size())
        self.assertEqual("5.3", q.find_min())

        self.assertEqual("5.3", q.extract_min())
        self.assertFalse(q.is_empty())
        self.assertEqual(1, q.get_size())
        self.assertEqual("8", q.find_min())

        self.assertEqual("8", q.extract_min())
        self.assertTrue(q.is_empty())
        self.assertEqual(0, q.get_size())

        with self.assertRaises(IndexError):
            q.extract_min()

        with self.assertRaises(IndexError):
            q.find_min()

        with self.assertRaises(ValueError):
            q.add(100, "100")

        with self.assertRaises(ValueError):
            q.add(-5, "-5")
