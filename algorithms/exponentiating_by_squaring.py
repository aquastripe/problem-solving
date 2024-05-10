from functools import lru_cache


@lru_cache()
def exp_by_squaring_recursive(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return x * exp_by_squaring_recursive(x, n - 1)
    else:
        return exp_by_squaring_recursive(x, n // 2) * exp_by_squaring_recursive(x, n // 2)


def exp_by_squaring_iterative(x, n):
    if n == 0:
        return 1

    y = 1
    while n > 0:
        if n % 2 == 1:
            y *= x

        x *= x
        n >>= 1

    return y


def main():
    assert exp_by_squaring_recursive(2, 32) == 4294967296
    assert exp_by_squaring_iterative(2, 32) == 4294967296


if __name__ == '__main__':
    main()
