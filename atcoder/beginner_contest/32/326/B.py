def main():
    n = int(input())
    hundred_digit = n // 100
    ten_digit = (n // 10) % 10
    one_digit = n % 10
    while one_digit < 10 and hundred_digit * ten_digit != one_digit:
        n += 1
        hundred_digit = n // 100
        ten_digit = (n // 10) % 10
        one_digit = n % 10

    print(n)


if __name__ == '__main__':
    main()
