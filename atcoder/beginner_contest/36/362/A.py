def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    r, g, b = read_tuple_int()
    c = input()
    if c == 'Red':
        print(min(g, b))
    elif c == 'Green':
        print(min(r, b))
    else:
        print(min(r, g))


if __name__ == '__main__':
    main()
