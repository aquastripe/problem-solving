def solve():
    return


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        count_1s = s.count('1')
        count_0s = n - count_1s

        print((count_1s - 1) * count_1s + (count_1s + 1) * count_0s)


if __name__ == '__main__':
    main()
