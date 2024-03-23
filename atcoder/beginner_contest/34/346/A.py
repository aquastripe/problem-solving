def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - 1):
        b.append(a[i] * a[i + 1])

    print(' '.join(list(map(str, b))))


if __name__ == '__main__':
    main()
