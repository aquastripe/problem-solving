import numpy as np


def main():
    n = int(input())
    grid = np.zeros((n, n), dtype=int)
    grid[n // 2, n // 2] = -1
    x, y = n // 2 - 1, n // 2

    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    i = 0
    depth = 1
    m = 3
    for num in range(1, n * n):
        if num + 1 == m * m:
            m += 2
            depth += 1

        grid[x, y] = num
        dx, dy = move[i]
        nx, ny = x + dx, y + dy
        if abs(nx - n // 2) > depth or abs(ny - n // 2) > depth:
            i = (i + 1) % 4
            dx, dy = move[i]

        x += dx
        y += dy

    for i in range(n):
        for j in range(n):
            if grid[i, j] == -1:
                print(f'T ', end='')
            else:
                print(f'{grid[i, j]} ', end='')
        print()


if __name__ == '__main__':
    main()
