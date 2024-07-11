from collections import Counter


def solve():
    return


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = input()
        counter = Counter(a)
        ans = 0
        for difficult in 'ABCDEFG':
            ans += max(m - counter[difficult], 0)

        print(ans)


if __name__ == '__main__':
    main()
