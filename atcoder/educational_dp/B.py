def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [10 ** 9 + 1] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(k):
            if i - j - 1 < 0:
                break

            dp[i] = min(dp[i], dp[i - j - 1] + abs(h[i] - h[i - j - 1]))

    print(dp[n - 1])


if __name__ == '__main__':
    main()
