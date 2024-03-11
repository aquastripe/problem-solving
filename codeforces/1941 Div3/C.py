def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ans = 0
        i = 0
        while i < n - 2:
            if s[i:i + 3] in ['map', 'pie']:
                ans += 1
                i += 3
            else:
                i += 1

        print(ans)


if __name__ == '__main__':
    main()
