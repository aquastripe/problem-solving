from collections import defaultdict
import bisect


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    max_num_gifts = solve_2(a, m)

    print(max_num_gifts)


def solve_1(a, m):
    num_gifts_in = defaultdict(int)
    for a_i in a:
        num_gifts_in[a_i] += 1

    x = sorted(num_gifts_in.keys())
    n = len(num_gifts_in.keys())
    lower_bound, upper_bound = x[0], x[0] + m
    j = 1
    num_gifts = num_gifts_in[lower_bound]
    while j < n and x[j] < upper_bound:
        num_gifts += num_gifts_in[x[j]]
        j += 1

    max_num_gifts = num_gifts
    for i in range(1, n):
        num_gifts -= num_gifts_in[x[i - 1]]
        upper_bound = x[i] + m
        while j < n and x[j] < upper_bound:
            num_gifts += num_gifts_in[x[j]]
            j += 1

        max_num_gifts = max(max_num_gifts, num_gifts)
    return max_num_gifts


def solve_2(a, m):
    a.sort()
    max_gifts = 0
    for i in range(len(a)):
        j = bisect.bisect_left(a, a[i] + m)
        max_gifts = max(max_gifts, j - i)
    return max_gifts


if __name__ == '__main__':
    main()
