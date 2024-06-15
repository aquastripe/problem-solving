def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    s = [input() for _ in range(n)]
    d = []
    for i in range(n):
        x = 0
        for j in range(m):
            if s[i][j] == 'o':
                x |= 1 << j
        d.append(x)

    ans = n
    for stands in range(1 << n):
        x = 0
        n_stands = 0
        for i in range(n):
            if stands & (1 << i):
                x |= d[i]
                n_stands += 1

        if x == (1 << m) - 1:
            ans = min(ans, n_stands)

    print(ans)


if __name__ == '__main__':
    main()
