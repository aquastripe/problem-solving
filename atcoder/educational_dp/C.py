def main():
    n = int(input())
    activities = []
    for _ in range(n):
        activities.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n)]
    dp[0] = activities[0]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = activities[i][j] + max(dp[i - 1][k] for k in range(3) if k != j)

    print(max(dp[n - 1][j] for j in range(3)))


if __name__ == '__main__':
    main()
