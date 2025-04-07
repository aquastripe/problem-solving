def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    ans = method_3(n)
    print(ans)


def method_2(n):
    ans_set = set()
    for b in range(1, 10 ** 9 + 1):
        good_integer = 2 ** 1 * b * b
        if good_integer > n:
            break

        for a in range(1, 64):
            good_integer = 2 ** a * b * b
            if good_integer <= n:
                ans_set.add(good_integer)
            else:
                break

    return len(ans_set)


def method_1(n):
    ans = 0
    pow_2 = [2 ** i for i in range(64)]
    for b in range(1, 10 ** 9 + 1):
        if b % 2 == 0:
            continue

        # 2**1 * b_square
        b_square = b * b
        good_integer = 2 * b_square
        if good_integer > n:
            break

        lb, ub = 1, 64
        while ub - lb > 1:
            mid = (lb + ub) // 2
            good_integer = pow_2[mid] * b_square
            if good_integer > n:
                ub = mid
            else:
                lb = mid

        ans += lb
    return ans


def method_3(n):
    ans = 0
    pow_2 = [2 ** i for i in range(64)]
    for a in range(1, 64):
        good_integer = pow_2[a] * 1
        if good_integer > n:
            break

        lb, ub = 1, 10 ** 9
        while ub - lb > 1:
            mid = (lb + ub) // 2
            good_integer = pow_2[a] * mid * mid
            if good_integer > n:
                ub = mid
            else:
                lb = mid

        ans += (lb + 1) // 2
    return ans


if __name__ == '__main__':
    main()
