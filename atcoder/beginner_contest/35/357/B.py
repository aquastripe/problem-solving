import string


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    s = input()
    n_lower = sum(s_i.islower() for s_i in s)

    if n_lower * 2 > len(s):
        print(s.lower())
    else:
        print(s.upper())


if __name__ == '__main__':
    main()
