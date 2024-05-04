import bisect


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    for _ in range(q):
        x = int(input())
        i = bisect.bisect_left(a, x)
        ans = n - i
        print(ans)


if __name__ == '__main__':
    main()
