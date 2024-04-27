def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    a = read_list_int()
    b = read_list_int()

    print(max(0, sum(a) - sum(b) + 1))


if __name__ == '__main__':
    main()
