import numpy as np


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    grid_size = 1
    grid_curr = np.array([['#']], dtype=str)
    for i in range(1, n + 1):
        grid_size_next = 3 ** i
        grid_next = np.empty((grid_size_next, grid_size_next), dtype=str)
        for j in range(3):
            for k in range(3):
                if j == 1 and k == 1:
                    grid_next[j * grid_size:(j + 1) * grid_size, k * grid_size:(k + 1) * grid_size] = \
                        np.array(['.'] * grid_size).repeat(grid_size).reshape(grid_size, grid_size)
                else:
                    grid_next[j * grid_size:(j + 1) * grid_size, k * grid_size:(k + 1) * grid_size] = grid_curr
        grid_size = grid_size_next
        grid_curr = grid_next

    for i in range(grid_curr.shape[0]):
        for j in range(grid_curr.shape[1]):
            print(grid_curr[i, j], end='')
        print()


if __name__ == '__main__':
    main()
