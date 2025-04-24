"""

a = ...
b = ???

b:
- 0 <= b[i] <= k
- a[i] + b[i] is constant
"""


def solve(a, b, n, k):
    count_missing = 0
    sum_a_b = -1
    min_a = 10 ** 10
    max_a = -1
    for i in range(n):
        if b[i] == -1:
            count_missing += 1
            min_a = min(min_a, a[i])
            max_a = max(max_a, a[i])
        else:
            # sum_a_b is not updated
            if sum_a_b == -1:
                sum_a_b = a[i] + b[i]
            # is updated
            else:
                if sum_a_b != a[i] + b[i]:
                    return 0

    if max_a == -1:
        return 1

    max_b = k - min_a
    min_b = k - max_a

    if 0 <= max_b <= k and 0 <= min_b <= k:
        if count_missing == n:
            return k - max_a + min_a + 1
        else:
            if 0 <= (sum_a_b - max_a) and (sum_a_b - min_a) <= k:
                return 1
            else:
                return 0
    else:
        return 0


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans = solve(a, b, n, k)
        print(ans)


if __name__ == '__main__':
    main()
