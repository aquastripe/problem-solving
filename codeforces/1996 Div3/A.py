def solve(n):
    count_4 = n // 4
    count_2 = (n - count_4 * 4) // 2
    return count_4 + count_2


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = solve(n)
        print(ans)


if __name__ == '__main__':
    main()
