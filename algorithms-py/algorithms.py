
var = '''
Print all valid parentnesis
'''


def print_parenthesis(n):
    arr = ['' for _ in range(2*n)]
    gen(n, arr)


def gen(n, arr, index=0, left=0, right=0):

    if index == 2*n:
        print(''.join(arr))
        return

    if left < n:
        arr[index] = "("
        gen(n, arr, index+1, left+1, right)

    if right < left:
        arr[index] = ")"
        gen(n, arr, index+1, left, right+1)


def main():

    n = 4
    print_parenthesis(n)

    print("main done")
    


if __name__ == '__main__':
    main()