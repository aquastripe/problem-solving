def main():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        ans = min(n * a, n // 2 * b + n % 2 * a)
        print(ans)


if __name__ == '__main__':
    main()
