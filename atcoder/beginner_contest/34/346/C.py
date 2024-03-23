def main():
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(a_i for a_i in a if a_i <= k)
    ans = (1 + k) * k // 2 - sum(b_i for b_i in b)
    print(ans)


if __name__ == '__main__':
    main()
