def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, l, r = read_tuple_int()
    a = list(range(1, n + 1))
    a[l - 1:r] = a[l - 1:r][::-1]
    print(*a)


if __name__ == '__main__':
    main()
