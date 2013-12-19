"""
Searching in two sorted arrays.
"""




def find_order_stat(a, b, k):
    """

    Given sorted arrays, you know that the nth largest will appear somewhere before or at A[n-1] if it is in array A,
    or B[n-1] if it is in array B

    Consider item at index a in A and item at index b in B.

    Perform binary search as follows

    If a + b > n, then reduce the search set
        if A[a] > B[b] then b = b / 2, else a = a / 2

    If a + b < n, then increase the search set
        if A[a] > B[b] then b = 3/2 * b, else a = 3/2 * a (halfway between a and previous a)

    If a + b = n then the nth largest is max(A[a], B[b])

    """

    validate_params(a, b, k)

    if k == 1:
        return min(a[0], b[0])

    #todo finish this

    return None


def validate_params(arr1, arr2, k):
    if k <= 0:
        raise ValueError("Negative or zero order statistic index passed '%s'" % k)

    max_order_stat_index = len(arr1) + len(arr2)

    if k > max_order_stat_index:
        raise ValueError("Too big order statistic index passed, should be less or equals to '%s'" % max_order_stat_index)


def find_order_stat_bruteforce(arr1, arr2, k):
    """
    Bruteforce approach
    """

    validate_params(arr1, arr2, k)

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

