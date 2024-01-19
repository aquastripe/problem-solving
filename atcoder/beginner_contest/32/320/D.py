from collections import defaultdict, deque


def main():
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        a, b, dx, dy = list(map(int, input().split()))
        g[a].append((b, dx, dy))
        g[b].append((a, -dx, -dy))

    x = defaultdict(int)
    y = defaultdict(int)
    is_visited = defaultdict(bool)

    q = deque()
    q.append(1)
    is_visited[1] = True
    while len(q) > 0:
        a = q.popleft()
        for b, dx, dy in g[a]:
            if is_visited[b]:
                continue

            x[b] = x[a] + dx
            y[b] = y[a] + dy

            q.append(b)
            is_visited[b] = True

    is_decidable = is_visited
    for i in range(n):
        if not is_decidable[i + 1]:
            print('undecidable')
        else:
            print(f'{x[i + 1]} {y[i + 1]}')


if __name__ == '__main__':
    main()
