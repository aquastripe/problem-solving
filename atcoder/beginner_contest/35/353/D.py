def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = read_list_int()
    m = 998244353

    d = [0] * n
    for i, a_i in enumerate(a):
        while a_i > 0:
            d[i] += 1
            a_i //= 10

    a_suffix_sum = [0] * (n + 1)
    d_suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        a_suffix_sum[i] = a_suffix_sum[i + 1] + a[i]
        d_suffix_sum[i] = d_suffix_sum[i + 1] + 10 ** d[i]

    ans = 0
    for i in range(n - 1):
        ans += a[i] * d_suffix_sum[i + 1] + a_suffix_sum[i + 1]

    print(ans % m)


if __name__ == '__main__':
    main()
