def solve(n, p):
    for i in range(n):
        if p[p[i]] == i:
            return 2

    return 3


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(lambda x: int(x) - 1, input().split()))
        ans = solve(n, p)
        print(ans)


if __name__ == '__main__':
    main()
