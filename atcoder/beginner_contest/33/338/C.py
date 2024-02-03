import numpy as np


def is_satisfied(q, a, b, x, y):
    c = a * x + b * y
    return np.all(c <= q)


def main():
    n = int(input())
    q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    is_unsatisfied = False
    for x in range(max(q) + 1):
        y_min = max(q) + 1

        for q_i, a_i, b_i in zip(q, a, b):
            if (q_i - a_i * x) < 0:
                is_unsatisfied = True
                break

            if b_i != 0:
                y = (q_i - a_i * x) // b_i
                y_min = min(y_min, y)

        if is_unsatisfied:
            break
        else:
            ans = max(ans, x + y_min)

    print(ans)


if __name__ == '__main__':
    main()
