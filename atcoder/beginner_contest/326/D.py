from itertools import permutations


def is_possibly_satisfied_rc(grid, r, c, n_i, n):
    for i in range(n_i + 1):
        for j in range(n):
            if grid[i][j] in 'ABC':
                if grid[i][j] == r[i]:
                    break
                else:
                    return False

    for j in range(n):
        for i in range(n_i + 1):
            if grid[i][j] in 'ABC':
                if grid[i][j] == c[j]:
                    break
                else:
                    return False

    return True


def is_satisfied_exactly_one_abc_by_columns(grid, n_i, n):
    for j in range(n):
        abc_exists = set()
        for i in range(n_i + 1):
            if grid[i][j] in ['A', 'B', 'C']:
                if grid[i][j] not in abc_exists:
                    abc_exists.add(grid[i][j])
                else:
                    return False
    return True


def dfs(grid, n_i, r, c, n, possibles):
    if n_i == n:
        return True

    for row in permutations(possibles):
        grid[n_i] = row

        if is_satisfied_exactly_one_abc_by_columns(grid, n_i, n):
            if is_possibly_satisfied_rc(grid, r, c, n_i, n):
                if dfs(grid, n_i + 1, r, c, n, possibles):
                    return True
    return False


def main():
    n = int(input())
    r = input()
    c = input()
    grid = [list('.' * n) for _ in range(n)]
    possibles = 'ABC..'[:n]

    is_satisfied = dfs(grid, 0, r, c, n, possibles)

    if is_satisfied:
        print('Yes')
        for row in grid:
            print(''.join(row))
    else:
        print('No')


if __name__ == '__main__':
    main()
