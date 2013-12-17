from bisect import bisect_left


def find_cut_value(arr, desired_value):
    """
    time: O(N*lgN + lgS*lgN)
    space: O(N)
    """
    arr.sort()

    sum_arr = [0 for _ in range(len(arr))]
    sum_arr[0] = arr[0]

    for i in range(1, len(sum_arr)):
        sum_arr[i] = arr[i] + sum_arr[i-1]

    if desired_value > sum_arr[-1]:
        return None

    if desired_value == sum_arr[-1]:
        return desired_value

    lo = 0
    hi = desired_value

    while lo <= hi:

        mid = lo + (hi-lo)/2
        index = bisect_left(arr, mid)

        if index >= len(arr):
            hi = mid - 1
        else:
            if index == 0:
                cur_sum = mid * len(arr)
            else:
                greater_elements_count = len(arr) - index
                cur_sum = sum_arr[index-1] + mid * greater_elements_count

            if cur_sum == desired_value:
                return mid

            if cur_sum < desired_value:
                lo = mid+1
            else:
                hi = mid-1

    return None


def main():

    arr = [90, 30, 100, 40, 20]

    for sum_value in range(0, 500):
        desired_sum = sum_value

        cut_value = find_cut_value(arr, desired_sum)

        if cut_value is None:
            print "No solution for sum = %s" % desired_sum
        else:
            arr_sum = sum([min(val, cut_value) for val in arr])
            print "cut_value = %s, expected_sum = %s, actual_sum = %s" % (cut_value, desired_sum, arr_sum)

    print "Main done"


if __name__ == '__main__':
    main()