import math


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = read_list_int()

    prefix_gcd = [0] * n
    suffix_gcd = [0] * n

    prefix_gcd[0] = a[0]
    suffix_gcd[n - 1] = a[n - 1]

    for i in range(1, n):
        prefix_gcd[i] = math.gcd(prefix_gcd[i - 1], a[i])

    for i in range(n - 2, -1, -1):
        suffix_gcd[i] = math.gcd(suffix_gcd[i + 1], a[i])

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, suffix_gcd[i + 1])
        elif i == n - 1:
            ans = max(ans, prefix_gcd[i - 1])
        else:
            ans = max(ans, math.gcd(prefix_gcd[i - 1], suffix_gcd[i + 1]))

    print(ans)


if __name__ == '__main__':
    main()
