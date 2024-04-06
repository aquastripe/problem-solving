def main():
    N, W = map(int, input().split())
    w, v = [], []
    for _ in range(N):
        w_i, v_i = map(int, input().split())
        w.append(w_i)
        v.append(v_i)

    dp = [[0] * (W + 1) for _ in range(N)]
    # dp[N][W] = max(dp[N-1][W], dp[N-1][W-w[i]] + v[i])
    for i in range(N):
        for curr_w in range(W + 1):
            if curr_w - w[i] >= 0:
                dp[i][curr_w] = max(dp[i - 1][curr_w], dp[i - 1][curr_w - w[i]] + v[i])
            else:
                dp[i][curr_w] = dp[i - 1][curr_w]

    print(dp[N - 1][W])


if __name__ == '__main__':
    main()
