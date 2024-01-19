def main():
    n, x = list(map(int, input().split()))
    ans = sum(filter(lambda s_i: s_i <= x, map(int, input().split())))
    print(ans)


if __name__ == '__main__':
    main()
