def solve(n, x):
    ans = []
    for i in range(x):
        ans.append(i)

    for i in range(n - 1, x - 1, -1):
        ans.append(i)

    return ' '.join(map(str, ans))


def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        ans = solve(n, x)
        print(ans)


if __name__ == '__main__':
    main()
