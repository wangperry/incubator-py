"""
Searching in two sorted arrays.
"""


def find_order_stat(arr1, arr2, k):
    """
    Bruteforce approach
    """

    if k <= 0:
        raise ValueError("Negative or zero order statistic index passed '%s'" % k)

    max_order_stat_index = len(arr1) + len(arr2)

    if k > max_order_stat_index:
        raise ValueError("Too big order statistic index passed, should be less or equals to '%s'" % max_order_stat_index)

    i = 0
    j = 0

    while k != 1:

        if i >= len(arr1):
            j += 1
        elif j >= len(arr2):
            i += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

        k -= 1

    if i >= len(arr1):
        return arr2[j]

    if j >= len(arr2):
        return arr1[i]

    return min(arr1[i], arr2[j])

