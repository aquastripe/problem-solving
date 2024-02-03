H, W, N = map(int, input().split())
grid = [['.' for _ in range(W)] for _ in range(H)]
dh_dw = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direct = 0
h, w = 0, 0
for _ in range(N):
    if grid[h][w] == '.':
        grid[h][w] = '#'
        direct += 1
    else:
        grid[h][w] = '.'
        direct -= 1

    dh, dw = dh_dw[direct % 4]
    h, w = (h + dh) % H, (w + dw) % W

for h in range(H):
    print(''.join(grid[h]))
