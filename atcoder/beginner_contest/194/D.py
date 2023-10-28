def main():
    # dp[i] := expected number of operations if i nodes are connected
    # dp[n] := 0
    # dp[1] := answer
    # dp[i] := dp[i+1]
    # group(connected) i/n, group(disconnected) (n-i)/n
    # dp[i] := (n-i)/n dp[i+1] + i/n dp[i] + 1
    # (n-i)/n dp[i] := (n-i)/n dp[i+1] + 1
    # dp[i] := dp[i+1] + n/(n-i)
    n = int(input())
    dp = [0.] * (n + 1)
    for i in range(n - 1, 0, -1):
        dp[i] = dp[i + 1] + n / (n - i)

    print(f'{dp[1]:.7f}')


if __name__ == '__main__':
    main()
