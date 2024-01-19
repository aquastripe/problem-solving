def main():
    n, l = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = sum(1 for a_i in a if a_i >= l)
    print(ans)


if __name__ == '__main__':
    main()
