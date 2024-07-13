def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    x_a, y_a = read_tuple_int()
    x_b, y_b = read_tuple_int()
    x_c, y_c = read_tuple_int()

    x_ab = x_a - x_b
    y_ab = y_a - y_b
    x_bc = x_b - x_c
    y_bc = y_b - y_c
    x_ac = x_a - x_c
    y_ac = y_a - y_c

    cond_1 = (x_ab * x_bc + y_ab * y_bc) == 0
    cond_2 = (x_bc * x_ac + y_bc * y_ac) == 0
    cond_3 = (x_ab * x_ac + y_ab * y_ac) == 0

    if cond_1 or cond_2 or cond_3:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
