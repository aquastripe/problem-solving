# 10/21/2023
from itertools import product

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    h, w = list(map(int, input().split()))
    s = [list(input()) for _ in range(h)]

    ans = 0
    for y_0 in range(h):
        for x_0 in range(w):
            if s[y_0][x_0] == '#':
                stack = [(y_0, x_0)]
                while len(stack) != 0:
                    y, x = stack.pop()
                    if s[y][x] == '.':
                        continue

                    s[y][x] = '.'
                    for dy, dx in product([-1, 0, 1], [-1, 0, 1]):
                        y_n, x_n = y + dy, x + dx
                        if 0 <= y_n < h and 0 <= x_n < w and s[y_n][x_n] == '#':
                            stack.append((y_n, x_n))

                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
