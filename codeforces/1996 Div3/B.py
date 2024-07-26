def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        grid = [input() for _ in range(n)]

        for i in range(0, n, k):
            for j in range(0, n, k):
                print(grid[i][j], end='')
            print()


if __name__ == '__main__':
    main()
