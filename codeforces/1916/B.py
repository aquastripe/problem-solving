import math

"""
8
2 3
    6 = 2*3 = a*b
1 2
    4 = 2*2 = b*b = b*b/g
3 11
    33 = 3*11 = a*b
1 5
    25 = 5*5 = b*b = b*b/g
5 10
    20 = 5*4 = 2*10 = b/a*b = b*b/a = b*b/g
4 6
    12 = 3*4 = 2*6 = a*b/g
3 9
    27 = 3*9 = 9*3 = a*b = b*b/a = b*b/g
250000000 500000000 = b/a*b = b*b/a
"""


def solve(a, b):
    gcd = math.gcd(a, b)
    if gcd == a:
        return b * b // gcd
    else:
        return a * b // gcd


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        x = solve(a, b)
        print(x)


if __name__ == '__main__':
    main()
