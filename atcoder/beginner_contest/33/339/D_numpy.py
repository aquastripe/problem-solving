from collections import deque

import numpy as np

OBSTACLE = 1
PLAYER = 2


def is_in_same_pos(state):
    r1, c1, r2, c2 = state
    return r1 == r2 and c1 == c2


def is_obstacle(grid, r, c, n):
    return not (0 <= r < n and 0 <= c < n) or grid[r, c] == OBSTACLE


def encode(state, bases):
    return np.dot(state, bases)


def decode(code, masks):
    return np.array([(code & mask) >> (i * 6) for i, mask in enumerate(masks)])


def main():
    n = int(input())
    grid_raw = [input() for _ in range(n)]
    grid = np.zeros((n, n))
    state = []
    for r in range(n):
        for c in range(n):
            if grid_raw[r][c] == '#':
                grid[r, c] = OBSTACLE
            elif grid_raw[r][c] == 'P':
                grid[r, c] = PLAYER
                state += [r, c]
    state = np.array(state, dtype=int)

    d_rc = np.array([(-1, 0), (0, 1), (1, 0), (0, -1)])
    is_visited = np.zeros(1 << 24, dtype=bool)
    bases = np.array([1 << i * 6 for i in range(4)], dtype=int)
    masks = np.array([int('1' * (i + 1) * 6, 2) for i in range(4)], dtype=int)

    q = deque()
    code = encode(state, bases)
    is_visited[code] = True
    q.append((code, 0))

    ans = -1
    while len(q) > 0:
        code, n_moves = q.popleft()
        state = decode(code, masks)
        if is_in_same_pos(state):
            ans = n_moves
            break

        for dr, dc in d_rc:
            next_state = []

            for i in range(2):
                r, c = state[i * 2:(i + 1) * 2]
                next_r = r + dr
                next_c = c + dc
                if is_obstacle(grid, next_r, next_c, n):
                    next_r, next_c = r, c

                next_state += [next_r, next_c]

            code = encode(next_state, bases)
            if not is_visited[code]:
                is_visited[code] = True
                q.append((code, n_moves + 1))

    print(ans)


if __name__ == '__main__':
    main()
