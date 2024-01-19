import bisect


def main():
    n, q = map(int, input().split())
    r = list(map(int, input().split()))
    r.sort()
    prefix_sum = [0] * n
    for i in range(n):
        prefix_sum[i] += prefix_sum[i - 1] + r[i]

    for _ in range(q):
        query = int(input())
        ans = bisect.bisect_right(prefix_sum, query)
        print(ans)


if __name__ == '__main__':
    main()
