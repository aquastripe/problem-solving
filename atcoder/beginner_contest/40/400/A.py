def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    a = read_int()
    if (400 % a) != 0:
        print('-1')
    else:
        print(400 // a)


if __name__ == '__main__':
    main()
