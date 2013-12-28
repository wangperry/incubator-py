
def my_sqrt(x):

    if x < 0:
        raise ValueError("")

    lo = 1.0
    hi = float(x)

    while True:
        mid = lo + (hi-lo)/2.0

        val = mid*mid

        if abs(val-x) < 0.0001:
            return mid

        if val > x:
            hi = mid+1
        else:
            lo = mid-1


def my_div(x, y):

    approximation_step = 0.1
    lo = approximation_step
    hi = x*y

    while True:
        mid = lo + (hi-lo)/2.0

        cur = mid*y

        if cur == x:
            return mid

        if cur > x:
            hi = mid - approximation_step
        else:
            lo = mid + approximation_step




def main():

    x = 16.0
    y = 17.0

    print x/y

    print my_div(x, y)

    print "Main done"


if __name__ == '__main__':
    main()