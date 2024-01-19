from itertools import permutations

import numpy as np


def main():
    h, w = map(int, input().split())
    a = np.array([list(map(int, input().split())) for _ in range(h)])
    b = np.array([list(map(int, input().split())) for _ in range(h)])
    count = count_swap(a, b, h, w)
    print(count)


def compute_inversion_number(perm, size):
    count = 0
    for i in range(size):
        for j in range(size):
            if i < j and perm[i] > perm[j]:
                count += 1
    return count


def count_swap(a, b, h, w):
    ans = 10 ** 9
    for perm_row in permutations(range(h)):
        for perm_col in permutations(range(w)):
            perm_row, perm_col = list(perm_row), list(perm_col)
            if np.all(a[perm_row][:, perm_col] == b):
                row_inv = compute_inversion_number(perm_row, h)
                col_inv = compute_inversion_number(perm_col, w)
                ans = min(ans, row_inv + col_inv)

    return ans if ans != 10 ** 9 else -1


if __name__ == '__main__':
    main()
