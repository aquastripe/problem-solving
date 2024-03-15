def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        # dp[i,j]: bool
        # dp[i,0/1] = a[0:i+1] is sorted and a[i] is split/not split
        # dp[i,0] = (dp[i-1,0] and a[i-1] <= a[i]) or (dp[i-1,1] and a[i-1]%10 <= a[i])
        # dp[i,1] = (dp[i-1,0] and b<=c and a[i-1] <= b) or (dp[i-1,1] and a[i-1] <= a[i]//10)
        dp = [[False for _ in range(2)] for _ in range(n)]
        dp[0][0] = True
        b, c = divmod(a[0], 10)
        dp[0][1] = b <= c
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] and a[i - 1] <= a[i] or dp[i - 1][1] and a[i - 1] % 10 <= a[i]
            is_splittable = a[i] >= 10
            b, c = divmod(a[i], 10)
            dp[i][1] = is_splittable and \
                       (dp[i - 1][0] and a[i - 1] <= b <= c or dp[i - 1][1] and a[i - 1] % 10 <= b <= c)

        if dp[n - 1][0] or dp[n - 1][1]:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
