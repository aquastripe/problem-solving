# TLE
def is_satisfied(q, a, b, x, y):
    return all(a_i * x + b_i * y <= q_i for a_i, b_i, q_i in zip(a, b, q))


def main():
    n = int(input())
    q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    max_q = max(q)
    for x in range(max_q + 1):
        # ax + by < q
        # max (x+y) = ?
        lb, ub = 0, max_q
        if not is_satisfied(q, a, b, x, lb):
            continue
        if is_satisfied(q, a, b, x, ub):
            y = ub
            ans = max(ans, x + y)
            continue

        while ub - lb > 1:
            y = (lb + ub) // 2

            if is_satisfied(q, a, b, x, y):
                lb = y
            else:
                ub = y
        y = lb
        ans = max(ans, x + y)

    print(ans)


if __name__ == '__main__':
    main()
