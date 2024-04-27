def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = []
    for _ in range(n):
        a.append(input())

    b = []
    for _ in range(n):
        b.append(input())

    solve(a, b, n)


def solve(a, b, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                print(f'{i + 1} {j + 1}')
                return


if __name__ == '__main__':
    main()
