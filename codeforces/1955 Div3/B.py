from collections import Counter


def solve(a, n, c, d):
    a00 = min(a)
    a_set = Counter(a)
    a_set[a00] -= 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = a00
    if check(matrix, a_set, n, c, d):
        return 'YES'

    return 'NO'


def check(a, a_set, n, c, d):
    for i in range(n):
        for j in range(n):
            if i + 1 < n and a[i + 1][j] == 0:
                if a_set[a[i][j] + c] > 0:
                    a[i + 1][j] = a[i][j] + c
                    a_set[a[i][j] + c] -= 1
                else:
                    return False

            if j + 1 < n and a[i][j + 1] == 0:
                if a_set[a[i][j] + d] > 0:
                    a[i][j + 1] = a[i][j] + d
                    a_set[a[i][j] + d] -= 1
                else:
                    return False

    return True


def main():
    t = int(input())
    for _ in range(t):
        n, c, d = map(int, input().split())
        a = list(map(int, input().split()))
        ans = solve(a, n, c, d)
        print(ans)


if __name__ == '__main__':
    main()
