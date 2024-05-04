# 10
# 1 1 1 1 1 1 2 3 4 5
#  => 1 2 3 4 5 6 7 (+1)
#  => ans = 7


def solve_1(a, n):
    a.sort()
    # I don't know why it is WA.
    i = 0
    count_lt_i, count_eq_i, count_gt_i = 0, 0, n
    curr_volume = 1
    while i < n:
        if a[i] == curr_volume:
            count_eq_i += 1
            count_gt_i -= 1
            curr_volume += 1
            i += 1
        elif a[i] < curr_volume:
            count_lt_i += 1
            count_gt_i -= 1
            i += 1
        else:
            volumes_from_lt_i = min(2, count_lt_i)
            volumes_from_gt_i = 2 - volumes_from_lt_i
            if count_gt_i - volumes_from_gt_i < 0:
                break

            count_lt_i -= volumes_from_lt_i
            count_gt_i -= volumes_from_gt_i
            count_eq_i += 1
            n -= volumes_from_gt_i
            curr_volume += 1

    print(count_eq_i + (count_lt_i + count_gt_i) // 2)


def solve_2(a, n):
    a = set(a)
    count_volumes = 0
    curr_volume = 1

    while n > 0:
        if curr_volume in a:
            n -= 1
        elif n - 2 >= 0:
            n -= 2
        else:
            break

        count_volumes += 1
        curr_volume += 1

    print(count_volumes)


def solve_3(a, n):
    def check(x):
        # a = [1, 2, 4, 4, 4, 4, 4] = {1, 2, 4}, n = 7
        # x = 4
        # {1, 2, 3, 4} & {1, 2, 4} = {1, 2, 4}, size = 3
        # size + (n - size) // 2 >= x
        size = len(set(range(1, x + 1)) & a)
        return size + (n - size) // 2 >= x

    a = set(a)
    lb, ub = 0, n + 1

    while ub - lb > 1:
        mid = (ub + lb) // 2
        if check(mid):
            lb = mid
        else:
            ub = mid

    print(lb)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    solve_3(a, n)


if __name__ == '__main__':
    main()
