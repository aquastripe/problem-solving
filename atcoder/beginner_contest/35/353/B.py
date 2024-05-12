def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, k = read_tuple_int()
    a = read_list_int()
    ans = 1
    curr = 0
    for a_i in a:
        if curr + a_i <= k:
            curr += a_i
        else:
            curr = a_i
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
