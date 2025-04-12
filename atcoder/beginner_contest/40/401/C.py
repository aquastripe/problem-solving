def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, k = read_tuple_int()
    if n < k:
        print(1)
    else:
        a = [0] * (n + 1)
        for i in range(k):
            a[i] = 1

        a[k] = k
        for i in range(k + 1, n + 1):
            a[i] = 2 * a[i - 1] - a[i - k - 1]
            a[i] %= 10 ** 9

        print(a[n])


if __name__ == '__main__':
    main()
