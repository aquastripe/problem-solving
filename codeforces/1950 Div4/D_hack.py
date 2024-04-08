from tqdm.rich import trange


def is_binary_decimal_1(n, binary_decimal):
    if n in binary_decimal:
        return True

    for m in binary_decimal:
        if m != 0 and m != 1 and n % m == 0 and is_binary_decimal_1(n // m, binary_decimal):
            return True

    return False


def is_binary_decimal_2(n, binary_decimal):
    if n in binary_decimal:
        return True

    for m in binary_decimal:
        while m != 0 and m != 1 and n % m == 0:
            n //= m

    return n == 1


def main():
    binary_decimal = set()
    for n in range(33):
        b = int(f'{n:b}')
        binary_decimal.add(b)

    for n in trange(1, 10 ** 5 + 1, 1):
        if is_binary_decimal_1(n, binary_decimal) != is_binary_decimal_2(n, binary_decimal):
            print(n)
            return

    print('No hacked')


if __name__ == '__main__':
    main()
