def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a_c_i = []
    for i, _ in enumerate(range(n)):
        a_x, c_x = read_list_int()
        a_c_i.append((a_x, c_x, i + 1))
    a_c_i.sort(reverse=True)

    c_y = 10 ** 9 + 1
    ans = []
    for _, c_x, i in a_c_i:
        if c_x <= c_y:
            ans.append(i)
            c_y = c_x
    ans.sort()

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
