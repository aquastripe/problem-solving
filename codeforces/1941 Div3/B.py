def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = True
        for i in range(len(a) - 2):
            if a[i] < 0:
                ans = False
                break

            a_i = a[i]
            a[i] -= a_i
            a[i + 1] -= a_i * 2
            a[i + 2] -= a_i

        ans = (ans and a[-1] == 0 and a[-2] == 0)
        print('Yes' if ans else 'No')


if __name__ == '__main__':
    main()
