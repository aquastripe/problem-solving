def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        curr_sum = 0
        n_odds = 0
        for a_i in a:
            curr_sum += a_i
            n_odds += a_i % 2
            factor_3 = n_odds // 3
            rest = n_odds % 3
            ans = curr_sum - factor_3 - (rest == 1 and curr_sum != a_i)
            print(ans, end=' ')
        print()


if __name__ == '__main__':
    main()
