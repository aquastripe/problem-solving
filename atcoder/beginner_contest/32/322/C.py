def main():
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    j = 0
    for i in range(1, n + 1):
        ans = a[j] - i
        print(ans)

        if a[j] == i:
            j += 1


if __name__ == '__main__':
    main()
