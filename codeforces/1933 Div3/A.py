def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = sum(map(abs, a))
        print(ans)


if __name__ == '__main__':
    main()
