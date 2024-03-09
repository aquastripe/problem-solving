def main():
    t = input()
    n = int(input())
    bags = []
    a = []
    for i in range(n):
        s = input().split()
        bags.append(s[1:])
        a.append(int(s[0]))

    inf = 10 ** 12
    dp = [[inf for _ in range(len(t) + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i + 1] = dp[i].copy()

        for s in bags[i]:
            for j in range(len(s), len(t) + 1):
                if s == t[j - len(s):j]:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - len(s)] + 1)

    ans = dp[n][len(t)]
    print(ans if ans != inf else -1)


if __name__ == '__main__':
    main()
