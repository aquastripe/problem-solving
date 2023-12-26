def main():
    a, m, l, r = map(int, input().split())
    if l < a:
        k = (a - l) // m
        l = a - k * m
    else:
        k = (l - a + m - 1) // m
        l = a + k * m

    if a < r:
        k = (r - a) // m
        r = a + k * m
    else:
        k = (a - r + m - 1) // m
        r = a - k * m

    if l > r:
        ans = 0
    else:
        ans = (r - l) // m + 1

    print(ans)


if __name__ == '__main__':
    main()
