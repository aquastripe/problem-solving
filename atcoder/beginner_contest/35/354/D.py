def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def rectangle_area(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    dx_area = 4 * ((dx - 1) // 4) + (0, 1, 3, 4)[(dx - 1) % 4]
    dx_area_shift = 4 * ((dx - 1) // 4) + (1, 1, 2, 4)[(dx - 1) % 4]
    return (dy - 1) // 2 * (dx_area + dx_area_shift) + (dy - 1) % 2 * dx_area_shift + dx_area


def main():
    ox = -10 ** 9 - 2
    oy = -10 ** 9

    a, b, c, d = read_tuple_int()
    ocd = rectangle_area(ox, oy, c, d)
    oab = rectangle_area(ox, oy, a, b)
    oad = rectangle_area(ox, oy, a, d)
    ocb = rectangle_area(ox, oy, c, b)
    ans = ocd - oad - ocb + oab
    print(ans)


if __name__ == '__main__':
    main()
