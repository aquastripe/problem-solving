def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    s, t = input().split()
    if s == 'AtCoder' and t == 'Land':
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
