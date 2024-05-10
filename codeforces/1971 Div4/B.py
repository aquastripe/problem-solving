def solve(s):
    ans = list(s)
    for i in range(1, len(s)):
        if s[i] != s[0]:
            ans[0] = s[i]
            ans[i] = s[0]
            return 'YES\n' + ''.join(ans)
    return 'NO'


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        ans = solve(s)
        print(ans)


if __name__ == '__main__':
    main()
