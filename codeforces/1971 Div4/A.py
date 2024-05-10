def solve(x, y):
    return f'{min(x, y)} {max(x, y)}'


def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        ans = solve(x, y)
        print(ans)


if __name__ == '__main__':
    main()
