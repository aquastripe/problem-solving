import bisect
from itertools import product


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = tuple(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))

        sum_coins = []
        for b_i, c_i in product(b, c):
            sum_coins.append(b_i + c_i)

        sum_coins.sort()
        ans = bisect.bisect_right(sum_coins, k)
        print(ans)


if __name__ == '__main__':
    main()
