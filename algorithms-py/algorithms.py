from interview.task_11_7 import *

from interview.task_11_8 import *


def main():

    a = [2, 4, 7, 9, 12, 13, 15, 22]
    b = [4, 5, 6, 7, 9, 12, 17, 18]


    i = 1
    j = len(a) + len(b) + 1

    for k in range(i, j):

        order_stat1 = find_order_stat_bruteforce(a, b, k)
        order_stat2 = find_order_stat(a, b, k)

        print "%s-th, bruteforce: %s, optimal: %s" % (k,order_stat1, order_stat2)

    print "Main done"


if __name__ == '__main__':
    main()