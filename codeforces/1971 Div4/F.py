import bisect


def main():
    t = int(input())
    y2_table = []
    y = 0
    while y * y < 10 ** 10 + 1:
        y2_table.append(y * y)
        y += 1

    for _ in range(t):
        r = int(input())
        ans = 0
        x = r
        while x > 0:
            y2 = r * r - x * x
            y = bisect.bisect_right(y2_table, y2) - 1
            while r * r - x * x > y * y:
                y += 1
            y_lb = y

            y2 = (r + 1) * (r + 1) - x * x
            y = bisect.bisect_right(y2_table, y2) - 1
            y_ub = y

            count_y = y_ub - y_lb + 1 + (-1 if y_ub * y_ub == y2 else 0)

            if count_y > 0:
                ans += count_y

            x -= 1

        print(ans * 4)


if __name__ == '__main__':
    main()
