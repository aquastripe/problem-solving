def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, x, y, z = read_tuple_int()
    if x < z < y or x > z > y:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
