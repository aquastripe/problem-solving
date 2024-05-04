import bisect
from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    table = defaultdict(list)
    for i, a_i in enumerate(a):
        table[a_i].append(i)

    for _ in range(q):
        l, r, x = map(int, input().split())
        n_before_l = bisect.bisect_left(table[x], l - 1)
        n_before_r = bisect.bisect_right(table[x], r - 1)
        ans = n_before_r - n_before_l
        print(ans)


if __name__ == '__main__':
    main()
