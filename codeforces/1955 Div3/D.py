a_count = [0] * (10 ** 6 + 1)
b_count = [0] * (10 ** 6 + 1)


def solve(n, m, k, a, b):
    for i in range(m):
        b_count[b[i]] += 1

    k_ = 0
    for i in range(m):
        a_count[a[i]] += 1
        k_ += int(b_count[a[i]] - a_count[a[i]] >= 0)

    ans = int(k_ >= k)
    for i in range(m, n):
        k_ -= int(b_count[a[i - m]] - a_count[a[i - m]] >= 0)
        a_count[a[i - m]] -= 1

        a_count[a[i]] += 1
        k_ += int(b_count[a[i]] - a_count[a[i]] >= 0)

        ans += k_ >= k

    for i in range(m):
        a_count[a[i]] = 0
        b_count[b[i]] = 0

    for i in range(m, n):
        a_count[a[i]] = 0

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ans = solve(n, m, k, a, b)
        print(ans)


if __name__ == '__main__':
    main()
