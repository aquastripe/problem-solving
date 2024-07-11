def solve():
    return


def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        if y >= -1:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
