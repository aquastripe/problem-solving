def check(a, b, c, n, x):
    return a * b + b * c + a * c <= n and a + b + c <= x


def solve(n, x):
    ans = 0
    a = 1
    while check(a, 1, 1, n, x):
        b = 1
        while check(a, b, 1, n, x):
            c_1 = (n - a * b) // (a + b)
            c_2 = x - a - b
            c = min(c_1, c_2)
            ans += c
            b += 1
        a += 1

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        ans = solve(n, x)
        print(ans)


if __name__ == '__main__':
    main()
