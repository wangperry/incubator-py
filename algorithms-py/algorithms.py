import platform
from ds.lru_queue import *


def main():

    q = LruQueue(10)

    for val in range(10):
        q.add(val, ("elem-%s" % val))

    q.get(5)
    q.get(3)
    q.get(1)

    print(q)

    q.add(13, "elem-13")
    q.add(15, "elem-15")

    print(q)

    print("===========================\nMain done...\nUsed python version: %s" % platform.python_version())


if __name__ == '__main__':
    main()