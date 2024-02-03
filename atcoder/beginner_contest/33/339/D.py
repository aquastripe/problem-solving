from collections import deque


def is_in_same_pos(players):
    return all(players[0][i] == players[1][i] for i in range(2))


def is_obstacle(grid, h, w, n):
    return not (0 <= h < n and 0 <= w < n) or grid[h][w] == '#'


def encode_pos(players):
    return players[0][0] + (players[0][1] << 6) + (players[1][0] << 12) + (players[1][1] << 18)


def main():
    n = int(input())
    grid = [input() for _ in range(n)]

    players = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 'P']
    d_rc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    is_visited = [0] * (1 << 24)
    q = deque()
    pos = encode_pos(players)
    is_visited[pos] = True
    q.append(players + [0])

    ans = -1
    while len(q) > 0:
        *players, n_moves = q.popleft()
        if is_in_same_pos(players):
            ans = n_moves
            break

        for dr, dc in d_rc:
            players_new = []
            for r, c in players:
                next_r = r + dr
                next_c = c + dc
                if is_obstacle(grid, next_r, next_c, n):
                    next_r, next_c = r, c

                players_new.append((next_r, next_c))

            pos = encode_pos(players_new)
            if not is_visited[pos]:
                is_visited[pos] = True
                q.append(players_new + [n_moves + 1])

    print(ans)


if __name__ == '__main__':
    main()
