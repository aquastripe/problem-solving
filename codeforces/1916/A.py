from functools import reduce
from operator import mul

"""
b = [7, 7, 17]
a = [?]
a + b = [7, 7, 17, ?] mul= 2023
"""


def solve(k, b):
    a = []
    curr_product = reduce(mul, b)
    if 2023 % curr_product != 0 or curr_product > 2023:
        return False, None

    rest = 2023 // curr_product
    a = [rest]
    for _ in range(1, k):
        a.append(1)

    return True, a


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        b = list(map(int, input().split()))
        exist, a = solve(k, b)
        if exist:
            print('YES')
            print(' '.join(map(str, a)))
        else:
            print('NO')


if __name__ == '__main__':
    main()
