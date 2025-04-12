def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    s = read_int()
    if 200 <= s <= 299:
        print('Success')
    else:
        print('Failure')


if __name__ == '__main__':
    main()
