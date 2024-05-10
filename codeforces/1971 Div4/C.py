def solve(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a > c:
        a, b, c, d = c, d, a, b

    """
    a < b < c < d: NO
    a < c < b < d: YES
    a < c < d < b: NO
    """

    if a < c < b < d:
        return 'YES'
    else:
        return 'NO'


def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        ans = solve(a, b, c, d)
        print(ans)


if __name__ == '__main__':
    main()
