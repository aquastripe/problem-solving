def in_matrix(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


"""
1
2 2
1 2
3 4
"""


def solve(a, n, m):
    for i in range(n):
        for j in range(m):
            neighbors = [
                a[i + d_i][j + d_j]
                for d_i, d_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if in_matrix(i + d_i, j + d_j, n, m)
            ]
            if a[i][j] > max(neighbors):
                a[i][j] = max(neighbors)

    return a


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))

        ans = solve(a, n, m)
        for i in range(n):
            for j in range(m):
                print(a[i][j], end=' ')
            print()


if __name__ == '__main__':
    main()
