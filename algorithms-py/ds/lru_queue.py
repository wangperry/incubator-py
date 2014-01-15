__author__ = 'admin'
__all__ = ["LruQueue"]


class LruQueue:

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.map = {}
        self.head = Node("HEAD", "HEAD")
        self.head.next = self.head
        self.head.prev = self.head

    def add(self, key, value):
        new_node = Node(key, value)

        if self.size == self.capacity:
            self.__remove_last()
            self.size -= 1

        self.__add_first(new_node)
        self.map[key] = new_node
        self.size += 1

    def __remove_last(self):

        if self.size == 0:
            raise ValueError("Can't delete element from empty LRU queue")

        last = self.head.prev
        pre_last = last.prev

        pre_last.next = self.head
        self.head.prev = pre_last

        last.next = None
        last.prev = None

        self.map.pop(last.key, None)

    def __add_first(self, new_node):
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

    def get(self, key):

        if not key in self.map:
            return None

        node = self.map[key]

        prev_node = node.prev
        next_node = node.next

        prev_node.next = node.next
        next_node.prev = node.prev

        node.next = None
        node.prev = None

        self.__add_first(node)

        return node.value

    def __str__(self):

        buf = "["

        cur = self.head.next

        if cur is not self.head:
            buf += str(cur.value)
            cur = cur.next

        while cur is not self.head:
            buf += ", " + str(cur.value)
            cur = cur.next

        buf += "]"
        return buf

    def __repr__(self):
        return "<LruQueue: %s>" % (str(self))


class Node:

    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return "%s" % str(self.value)

