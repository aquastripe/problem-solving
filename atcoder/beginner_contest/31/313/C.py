import math


def solve(A):
    mean = sum(A) / len(A)
    mean_floor = math.floor(mean)
    mean_ceil = mean_floor + 1

    n = sum(A) - mean_floor * len(A)
    m = len(A) - n

    A.sort()
    count = 0
    i, j = 0, len(A) - 1
    while i < j:
        target_i = mean_floor if i < m else mean_ceil
        target_j = mean_floor if j < m else mean_ceil

        diff_i = target_i - A[i]
        diff_j = A[j] - target_j

        if diff_i < diff_j:
            diff = diff_i
            A[i] += diff
            A[j] -= diff
            i += 1
            count += diff
        else:
            diff = diff_j
            A[i] += diff
            A[j] -= diff
            j -= 1
            count += diff
    return count


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    count = solve(A)
    print(count)


if __name__ == '__main__':
    main()
