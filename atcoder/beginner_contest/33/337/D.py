import sys
from collections import Counter

import numpy as np

input = sys.stdin.readline


def count_operations(h, w, k, s):
    min_operations = k + 1
    for h_i in range(h):
        count = Counter(s[h_i, :k])
        if count['x'] == 0:
            min_operations = min(min_operations, count['.'])

        for w_i in range(k, w):
            count[s[h_i, w_i]] += 1
            count[s[h_i, w_i - k]] -= 1

            if count['x'] == 0:
                min_operations = min(min_operations, count['.'])
    return min_operations


def main():
    h, w, k = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    s = np.array(s)

    min_operations = (max_operations := k + 1)
    if w >= k:
        min_operations = min(min_operations, count_operations(h, w, k, s))
    if h >= k:
        min_operations = min(min_operations, count_operations(w, h, k, s.T))

    min_operations = min_operations if min_operations != max_operations else -1
    print(min_operations)


if __name__ == '__main__':
    main()
