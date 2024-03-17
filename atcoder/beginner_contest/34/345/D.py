import sys

from itertools import product

sys.setrecursionlimit(10000000)


def is_satisfied(grid, h, w, curr_r, curr_c, a, b):
    if curr_r + a > h or curr_c + b > w:
        return False

    for r, c in product(range(curr_r, curr_r + a), range(curr_c, curr_c + b)):
        if grid[r][c]:
            return False

    return True


def dfs_backtracking(grid, is_used, n, h, w, tiles):
    curr_r, curr_c = None, None
    for r, c in product(range(h), range(w)):
        if not grid[r][c]:
            curr_r, curr_c = r, c
            break

    if curr_r is None and curr_c is None:
        return True

    for i in range(n):
        if is_used[i]:
            continue

        is_used[i] = True
        ta, tb = tiles[i]
        rotated_tiles = [(ta, tb), (tb, ta)]
        for a, b in rotated_tiles:
            if is_satisfied(grid, h, w, curr_r, curr_c, a, b):
                for r, c in product(range(curr_r, curr_r + a), range(curr_c, curr_c + b)):
                    grid[r][c] = True

                if dfs_backtracking(grid, is_used, n, h, w, tiles):
                    return True

                for r, c in product(range(curr_r, curr_r + a), range(curr_c, curr_c + b)):
                    grid[r][c] = False

        is_used[i] = False

    return False


def solve(grid, is_used, n, h, w, tiles):
    if dfs_backtracking(grid, is_used, n, h, w, tiles):
        return True

    return False


def main():
    n, h, w = map(int, input().split())
    tiles = []
    for _ in range(n):
        a, b = map(int, input().split())
        tiles.append((a, b))

    grid = [[False for _ in range(w)] for _ in range(h)]
    is_used = [False] * n
    if solve(grid, is_used, n, h, w, tiles):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
