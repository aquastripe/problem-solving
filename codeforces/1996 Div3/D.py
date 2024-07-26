"""
n x
7 1000

1 1 1
1 1 2
1 1 3
1 2 1
1 3 1
2 1 1
3 1 1


1 1

1 1
1 2
2 1

1 1
1 2
1 3
2 1
3 1

a * b + b * c + a * c <= n and a + b + c <= x

bc + ac <= n - ab
c <= (n-ab)/(a+b)
c = (n-ab)//(a+b)

c(1) = (n-a*1)//(a+1)
c(2) = (n-a*2)//(a+2)
"""


def check(a, b, c, n, x):
    return a * b + b * c + a * c <= n and a + b + c <= x


def solve(n, x):
    ans = 0
    max_a = min((n - 1) // 2 + 1, x - 2)
    for a in range(1, max_a + 1):
        b = 1
        while check(a, b, 1, n, x):
            c = min((n - a * b) // (a + b), x - a - b)
            ans += c
            b += 1

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        ans = solve(n, x)
        print(ans)


if __name__ == '__main__':
    main()
