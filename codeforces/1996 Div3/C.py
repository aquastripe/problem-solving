import string


def solve(prefix_sum_a, prefix_sum_b, l, r):
    ans = 0
    for c in string.ascii_lowercase:
        ans += abs((prefix_sum_a[c][r] - prefix_sum_a[c][l - 1]) - (prefix_sum_b[c][r] - prefix_sum_b[c][l - 1]))
    ans //= 2
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        a = input()
        b = input()
        prefix_sum_a = {c: [0] * (n + 1) for c in string.ascii_lowercase}
        prefix_sum_b = {c: [0] * (n + 1) for c in string.ascii_lowercase}

        for i in range(n):
            for c in string.ascii_lowercase:
                prefix_sum_a[c][i + 1] = prefix_sum_a[c][i] + (a[i] == c)
                prefix_sum_b[c][i + 1] = prefix_sum_b[c][i] + (b[i] == c)

        for _ in range(q):
            l, r = map(int, input().split())
            ans = solve(prefix_sum_a, prefix_sum_b, l, r)
            print(ans)


if __name__ == '__main__':
    main()
