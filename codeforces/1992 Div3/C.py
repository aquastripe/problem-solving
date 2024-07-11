"""
f(i): >= k
g(i): <= m

n m k
5 2 5

1 2 3 4 5

5 3 4 1 2

  f g
1 5 0
2 5 0
3 5 0
4 5 1
5 5 3

5 4 3 1 2

  f g
1 5 0
2 5 0
3 5 0
4 5 1
5 5 3

 n m k
10 3 8

10 9 8 7 6 5 4 1 2 3

"""


def solve(n, m, k):
    a = list(range(1, n + 1))
    b, c = a[:m], a[m:]
    ans = c[::-1] + b
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        ans = solve(n, m, k)
        print(*ans)


if __name__ == '__main__':
    main()
