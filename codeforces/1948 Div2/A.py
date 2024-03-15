def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        if n % 2 == 1:
            print('NO')
            continue

        print('YES')
        for i in range(n // 2):
            print('AAB', end='')

        print()


if __name__ == '__main__':
    main()
