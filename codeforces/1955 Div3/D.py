from collections import defaultdict


def solve(n, m, k, a, b):
    a_count = defaultdict(int)
    b_count = defaultdict(int)
    b_m_set = set()
    for i in range(m):
        a_count[a[i]] += 1
        b_count[b[i]] += 1
        b_m_set.add(b[i])

    k_ = 0
    for b_i in b_m_set:
        k_ += min(a_count[b_i], b_count[b_i])

    ans = int(k_ >= k)
    for i in range(m, n):
        a_count[a[i]] += 1
        if b_count[a[i]] > 0:
            k_ += int(a_count[a[i]] <= b_count[a[i]])

        a_count[a[i - m]] -= 1
        if b_count[a[i - m]] > 0:
            k_ -= int(a_count[a[i - m]] + 1 <= b_count[a[i - m]])

        if k_ >= k:
            ans += 1

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
