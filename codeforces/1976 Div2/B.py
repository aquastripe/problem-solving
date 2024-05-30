def solve(n, a, b):
    n_ops = 1  # appended
    min_n_ops_last = 10 ** 10

    for i in range(n):
        n_ops += abs(a[i] - b[i])
        min_n_ops_last = min(min_n_ops_last, abs(a[i] - b[-1]), abs(b[i] - b[-1]))
        if a[i] < b[-1] < b[i] or b[i] < b[-1] < a[i]:
            min_n_ops_last = 0
    n_ops += min_n_ops_last

    return n_ops


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ans = solve(n, a, b)
        print(ans)


if __name__ == '__main__':
    main()
