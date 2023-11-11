def main():
    n, x = list(map(int, input().split()))
    s = list(map(int, input().split()))
    s = list(filter(lambda s_i: s_i <= x, s))
    ans = sum(s)
    print(ans)


if __name__ == '__main__':
    main()
