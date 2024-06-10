import numpy as np


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def solve_by_geometric_series(n, k, p):
    a = (pow(10, n * k, p) - 1) % p
    b = pow(pow(10, k, p) - 1, -1, p) % p
    ans = n * a * b % p
    return ans


def solve_by_exp_by_squaring(n, k, p):
    # t^k
    t = np.identity(2, dtype=np.int64)
    base = np.array(
        [[pow(10, k, p), n % p],
         [0, 1]],
        dtype=np.int64
    )
    power = n - 1
    while power > 0:
        if power & 1:
            t = t @ base
            t %= p

        base = base @ base
        base %= p
        power >>= 1

    v_1 = np.array([n % p, 1], dtype=np.int64)
    v_n = t @ v_1
    v_n %= p
    return v_n[0]


def main():
    n = read_int()
    k = len(str(n))
    p = 998244353

    # ans = solve_by_geometric_series(n, k, p)
    ans = solve_by_exp_by_squaring(n, k, p)
    print(ans)


if __name__ == '__main__':
    main()
