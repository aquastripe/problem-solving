def main():
    b = int(input())
    ans = -1
    n = 1
    while (m := pow(n, n)) < b:
        n += 1

    if m == b:
        ans = n

    print(ans)


if __name__ == '__main__':
    main()
