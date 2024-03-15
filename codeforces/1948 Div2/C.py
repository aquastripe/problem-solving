from collections import deque


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = [input(), input()]

        q = deque([(0, 0)])
        is_reachable = [[False for _ in range(n)] for _ in range(2)]
        is_reachable[0][0] = True
        while len(q) > 0:
            r, c = q.pop()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 and 0 <= nc < n:
                    if grid[nr][nc] == '<':
                        nc -= 1
                    else:
                        nc += 1

                    if 0 <= nc < n and not is_reachable[nr][nc]:
                        q.append((nr, nc))
                        is_reachable[nr][nc] = True

        if is_reachable[1][n - 1]:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
