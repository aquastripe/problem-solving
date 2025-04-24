"""

    0 1 2 3 4 5 6 7 8
a = 3 5 2 3 3 5 8 1 2
b = 4 6 2 4 6

prefix: [1, 6, 8, -1, -1]
suffix: [-1, -1, 4, 5, 6]

"""


def solve(a, b, n, m):
    prefix = [-1] * m
    suffix = [-1] * m

    j = 0
    for i in range(m):
        while j < n and a[j] < b[i]:
            j += 1

        if j == n:
            break

        prefix[i] = j
        j += 1

    j = n - 1
    for i in range(m - 1, -1, -1):
        while j >= 0 and a[j] < b[i]:
            j -= 1

        if j == -1:
            break

        suffix[i] = j
        j -= 1

    if prefix[-1] != -1:
        return 0

    ans = 10 ** 10
    for i in range(m):
        if m == 1:
            is_satisfied = True
        elif i == 0:
            is_satisfied = suffix[i + 1] != -1
        elif i == m - 1:
            is_satisfied = prefix[i - 1] != -1
        else:
            is_satisfied = (prefix[i - 1] != -1 and suffix[i + 1] != -1) and (prefix[i - 1] < suffix[i + 1])

        if is_satisfied:
            ans = min(ans, b[i])

    if ans == 10 ** 10:
        return -1

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans = solve(a, b, n, m)
        print(ans)


if __name__ == '__main__':
    main()
