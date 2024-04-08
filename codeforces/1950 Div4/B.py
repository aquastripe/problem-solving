def main():
    t = int(input())

    grid = []
    for i in range(21):
        if i % 2 == 0:
            grid.append('##..' * 11)
            grid.append('##..' * 11)
        else:
            grid.append('..##' * 11)
            grid.append('..##' * 11)

    for _ in range(t):
        n = int(input())
        for i in range(2 * n):
            for j in range(2 * n):
                print(grid[i][j], end='')
            print()


if __name__ == '__main__':
    main()
