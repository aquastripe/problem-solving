def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    x = 0
    n_i = 1
    for i in range(m + 1):
        x += n_i
        n_i *= n

        if x > 10 ** 9:
            print('inf')
            exit()
    print(x)


if __name__ == '__main__':
    main()
