"""
Searching in two sorted arrays.
"""




def find_order_stat(a, b, k):

    validate_params(a, b, k)

    if k == 1:
        return min(a[0], b[0])

    top1 = min(k-1, len(a)-1)
    top2 = min(k-1, len(b)-1)

    off1 = (top1+1)/2
    off2 = (top2+1)/2

    count = top1+1 + top2+1

    while count != k:

        if count > k:
        #decrease
            if a[top1] > b[top2]:
                top1 -= off1
                off1 /= 2
            else:
                top2 -= off2;
                off2 /= 2
        else:
        # count < k => increase
            if a[top1] < b[top2]:
                top1 += off1
                off1 /= 2
            else:
                top2 += off2
                off2 /= 2

        count = top1+1 + top2+1



    return max(a[top1], b[top2])


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

