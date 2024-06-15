def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    a = read_list_int()
    b = read_list_int()

    a.sort()
    b.sort()
    ans = 0
    i, j = 0, 0
    while i < n and j < m:
        if a[i] >= b[j]:
            ans += a[i]
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1

    if j == m:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
