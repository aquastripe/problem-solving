def main():
    n = int(input())
    p = list(map(int, list(input().split(' '))))
    if n > 1:
        ans = max(max(p[1:]) - p[0] + 1, 0)
    else:
        ans = 0
    print(ans)


if __name__ == '__main__':
    main()
