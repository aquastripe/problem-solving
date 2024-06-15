def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, a = read_tuple_int()
    t = read_list_int()
    last = 0
    for t_i in t:
        if last < t_i:
            print(t_i + a)
            last = t_i + a
        else:
            print(last + a)
            last = last + a


if __name__ == '__main__':
    main()
