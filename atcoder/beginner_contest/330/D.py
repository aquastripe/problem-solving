def main():
    n = int(input())
    s = [input() for _ in range(n)]
    count_in_rows = [0] * n
    count_in_cols = [0] * n
    for i in range(n):
        for j in range(n):
            if s[i][j] == 'o':
                count_in_rows[i] += 1
                count_in_cols[j] += 1

    ans = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == 'o' and count_in_rows[i] >= 2 and count_in_cols[j] >= 2:
                ans += (count_in_rows[i] - 1) * (count_in_cols[j] - 1)

    print(ans)


if __name__ == '__main__':
    main()
