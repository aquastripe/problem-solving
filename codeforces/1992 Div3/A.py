"""
2 3 4
3 3 4
3 4 4
4 4 4
4 4 5
4 5 5
"""


def solve(a, b, c):
    for _ in range(5):
        min_abc = min(a, b, c)
        if a == min_abc:
            a += 1
        elif b == min_abc:
            b += 1
        else:
            c += 1

    return a * b * c


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        ans = solve(a, b, c)
        print(ans)


if __name__ == '__main__':
    main()
