def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    s_x, s_y = read_tuple_int()
    t_x, t_y = read_tuple_int()

    # Left alignment
    if (s_x + s_y) % 2 == 1:
        s_x -= 1
    if (t_x + t_y) % 2 == 1:
        t_x -= 1

    d_y = abs(t_y - s_y)
    s_x_lb, s_x_ub = s_x - d_y, s_x + d_y

    # t_x in [s_x_lb, s_x_ub]
    if s_x_lb <= t_x <= s_x_ub:
        d_x = 0
    else:
        d_x = min(abs(t_x - s_x_lb), abs(t_x - s_x_ub))

    ans = d_y + d_x // 2
    print(ans)


if __name__ == '__main__':
    main()
