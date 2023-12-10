import bisect


def search_upper_bound(array, target, lower_bound, upper_bound):
    while lower_bound + 1 != upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if array[mid] <= target:
            lower_bound = mid
        else:
            upper_bound = mid

    return upper_bound


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + a_sorted[i]

    for i in range(n):
        j = search_upper_bound(a_sorted, a[i], 0, n)
        # j = bisect.bisect_right(a_sorted, a[i])
        print(suffix_sum[j], end=' ' if i != n - 1 else '\n')


if __name__ == '__main__':
    main()
