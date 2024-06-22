from collections import defaultdict


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = read_list_int()
    d = defaultdict(list)
    for i, a_i in enumerate(a):
        d[a_i].append(i)

    ans = 0
    for a_i, (i, j) in d.items():
        ans += int((j - i) == 2)

    print(ans)


if __name__ == '__main__':
    main()
