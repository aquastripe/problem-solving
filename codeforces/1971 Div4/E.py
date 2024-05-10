"""
10 1 3
10
10
0
6
7

"""
import bisect


def solve():
    return


def main():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        b = [0] + list(map(int, input().split()))

        ans = []
        for _ in range(q):
            d = int(input())
            """
            a = [0, 4, 10]
            b = [0, 4, 7]
            v = [1, 2]
            d = 6 => a[1] = 4 => find i s.t. d >= a[i] is satisfied
            (d - a[1]) // v[0] = (d - a[1]) // ((a[2] - a[1]) / (b[2] - b[1])) = 
            """
            if d == 0:
                ans.append(0)
            else:
                i = bisect.bisect_left(a, d)
                ans.append(b[i - 1] + (d - a[i - 1]) * (b[i] - b[i - 1]) // (a[i] - a[i - 1]))

        print(*ans)


if __name__ == '__main__':
    main()
