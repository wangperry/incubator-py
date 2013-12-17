from interview.task_11_7 import *

from interview.task_11_8 import *


def main():

    a = [2, 4, 7, 9, 12, 13, 15, 22]
    b = [4, 5, 6, 7, 9, 12, 17, 18]

    for k in range(1, len(a) + len(b) + 1):
        order_stat = find_order_stat(a, b, k)
        print "%s-th element: %s" % (k, order_stat)

    print "Main done"


if __name__ == '__main__':
    main()