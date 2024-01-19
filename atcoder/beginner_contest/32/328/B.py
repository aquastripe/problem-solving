def split_into_digits(n):
    digits = {n % 10}
    while (n := n // 10) != 0:
        digits.add(n % 10)

    return digits


def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i, days in enumerate(d):
        month = i + 1
        month_digits = split_into_digits(month)
        for day in range(1, days + 1):
            day_digits = split_into_digits(day) | month_digits
            if len(day_digits) == 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
