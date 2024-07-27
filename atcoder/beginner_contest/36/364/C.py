import bisect


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, x, y = read_tuple_int()
    a = read_list_int()
    a.sort(reverse=True)
    b = read_list_int()
    b.sort(reverse=True)

    prefix_sum_a = [0] * n
    prefix_sum_b = [0] * n
    for i in range(n):
        prefix_sum_a[i] = prefix_sum_a[i - 1] + a[i]
        prefix_sum_b[i] = prefix_sum_b[i - 1] + b[i]

    min_a = bisect.bisect_right(prefix_sum_a, x) + 1
    min_b = bisect.bisect_right(prefix_sum_b, y) + 1
    ans = min(min_a, min_b, n)
    print(ans)


if __name__ == '__main__':
    main()
