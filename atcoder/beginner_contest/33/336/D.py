def main():
    n = int(input())
    a = list(map(int, input().split()))

    # left_slope[i]: Returns k, where k is the maximum size of Pyramid
    #                   that satisfies the pattern 1, 2, ..., k in left slope.
    # right_slope[i]: ... k, k-1, ..., 1 in right slope.
    left_slope = [0] * n
    right_slope = [0] * n

    k = 1
    for i, a_i in enumerate(a):
        left_slope[i] = min(a_i, k)
        k = min(k, a_i)
        k += 1

    k = 1
    for i, a_i in enumerate(reversed(a)):
        right_slope[-i - 1] = min(a_i, k)
        k = min(k, a_i)
        k += 1

    k = 1
    for i in range(n):
        k = max(k, min(left_slope[i], right_slope[i]))

    print(k)


if __name__ == '__main__':
    main()
