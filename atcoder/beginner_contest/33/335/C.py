def main():
    move = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }
    n, q = map(int, input().split())
    x, y, = 1, 0
    history = []
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            dx, dy = move[query[1]]
            x += dx
            y += dy
            history.append((x, y))
        else:
            p = int(query[1]) - 1
            i = len(history)
            if p < i:
                print(f'{history[-1 - p][0]} {history[-1 - p][1]}')
            else:
                print(f'{(p - i + 1) * 1} {0}')


if __name__ == '__main__':
    main()
