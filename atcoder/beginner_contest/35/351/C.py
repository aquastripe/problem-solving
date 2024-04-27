def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = read_list_int()
    q = []
    for i in range(n):
        q.append(a[i])

        while True:
            if len(q) == 1:
                break

            if q[-1] == q[-2]:
                e = q.pop()
                q.pop()
                q.append(e + 1)
            else:
                break

    print(len(q))


if __name__ == '__main__':
    main()
