from math import lcm


def main():
    n, m, k = map(int, input().split())
    lcm_nm = lcm(n, m)

    # n, m, k = 2, 3, 5
    # lcm_nm = lcm(n, m) = 6
    # test(11)
    # 11 // n = 5
    # 11 // m = 3
    # 11 // lcm_nm = 1
    # => There are 5 numbers that are divisible by 2, 3 numbers that are divisible by 3,
    # and 1  numbers that are divisible by 2 * 3.
    # 2, 4, 6, 8, 10
    # 3, 6, 9
    # 6 => 6 presents in multipliers of both 2 and 3.
    # How many numbers satisfy the problem statement? 5 + 3 - 2 * 1 = 6.
    # 2, 3, 4, 8, 9, 10, [11]
    # test(13)
    # 13 // n = 6
    # 13 // m = 4
    # 13 // lcm_nm = 2
    # 6 + 4 - 2 * 2 = 6
    # 2, 3, 4, 8, 9, 10
    # test(14)
    # 14 // n = 7
    # 14 // m = 4
    # 14 // lcm_nm = 2
    # 7 + 4 - 2 * 2 = 7
    # 2, 3, 4, 8, 9, 10, 14
    #
    # num:   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    # count: 0, 1, 2, 3, 3, 3, 3, 4, 5,  6,  6,  6,  6,  7

    lb, ub = 0, 2 * 10 ** 18
    while lb + 1 < ub:
        mid = (lb + ub) // 2
        count = mid // n + mid // m - 2 * (mid // lcm_nm)

        if count < k:
            lb = mid
        else:
            ub = mid

    ans = ub
    print(ans)


if __name__ == '__main__':
    main()
