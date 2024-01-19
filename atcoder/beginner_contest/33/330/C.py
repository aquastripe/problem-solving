import math


def main():
    d = int(input())
    x = 0
    ans = d
    while (x_2 := x * x) < d + 1:
        y_2 = abs(d - x_2)
        y1 = int(math.sqrt(y_2))
        y2 = y1 + 1
        ans = min(ans, abs(x_2 + y1 * y1 - d), abs(x_2 + y2 * y2 - d))
        x += 1

    print(ans)


if __name__ == '__main__':
    main()
