def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    ans = 0
    d = 0
    for _ in range(n):
        a, b = read_tuple_int()
        ans += a
        d = max(d, b - a)
    ans += d
    print(ans)


if __name__ == '__main__':
    main()
