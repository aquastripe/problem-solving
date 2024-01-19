def main():
    n = int(input())
    even_numbers = list(range(0, 9, 2))
    digits = []
    n -= 1
    while n != 0:
        digits.append(even_numbers[n % 5])
        n //= 5

    if digits:
        digits = reversed(digits)
    else:
        digits.append(0)
    print(''.join(map(str, digits)))


if __name__ == '__main__':
    main()
