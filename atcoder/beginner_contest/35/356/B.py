def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    a = read_list_int()
    b = [0] * m
    for _ in range(n):
        x = read_list_int()
        for i in range(m):
            b[i] += x[i]

    ans = 'Yes' if all(a[i] <= b[i] for i in range(m)) else 'No'
    print(ans)


if __name__ == '__main__':
    main()
