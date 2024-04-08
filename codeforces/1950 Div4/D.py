def is_binary_decimal(n, binary_decimal):
    if n in binary_decimal:
        return True

    for m in binary_decimal:
        if m != 0 and m != 1 and n % m == 0 and is_binary_decimal(n // m, binary_decimal):
            return True

    return False


def main():
    t = int(input())
    binary_decimal = set()
    for n in range(33):
        b = int(f'{n:b}')
        binary_decimal.add(b)

    for _ in range(t):
        n = int(input())
        ans = 'YES' if is_binary_decimal(n, binary_decimal) else 'NO'
        print(ans)


if __name__ == '__main__':
    main()
