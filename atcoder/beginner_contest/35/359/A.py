def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    s = [input() for _ in range(n)]
    ans = len(list(filter(lambda s_i: s_i == 'Takahashi', s)))
    print(ans)


if __name__ == '__main__':
    main()
