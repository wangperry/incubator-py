from bisect import bisect_left

def find_cut_value(arr, desired_value):
    """
    S - desired value
    N - array length
    time: O(N*lgN + N*lgS)
    space: O(1)
    """
    arr.sort()

    #sum_arr = [0 for _ in range(len(arr))]
    #sum_arr[0] = arr[0]

    #for i in range(1, len(sum_arr)):
    #    sum_arr[i] = arr[i] + sum_arr[i-1]

    max_sum = sum(arr)

    if desired_value > max_sum:
        return None

    if desired_value == max_sum:
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

                prefix_sum = 0
                for i in range(0, index):
                    prefix_sum += arr[i]

                cur_sum = prefix_sum + mid * greater_elements_count

            if cur_sum == desired_value:
                return mid

            if cur_sum < desired_value:
                lo = mid+1
            else:
                hi = mid-1

    return None
