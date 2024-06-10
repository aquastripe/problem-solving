def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    h = read_list_int()

    ans = 0
    h_total = 0
    for h_i in h:
        if h_total + h_i <= m:
            h_total += h_i
            ans += 1
        else:
            break

    print(ans)


if __name__ == '__main__':
    main()
