def main():
    n, s, m, l = map(int, input().split())
    ans = int(1e6)
    for n_12 in range(n // 12 + 2):
        for n_8 in range(n // 8 + 2):
            for n_6 in range(n // 6 + 2):
                if n_12 * 12 + n_8 * 8 + n_6 * 6 >= n:
                    ans = min(ans, n_6 * s + n_8 * m + n_12 * l)
    print(ans)


if __name__ == '__main__':
    main()
