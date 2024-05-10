def solve(s):
    ans = 1
    count_zeros_to_ones = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            ans += 1

            if s[i - 1] == '0':
                count_zeros_to_ones += 1

    if count_zeros_to_ones > 0:
        ans -= 1

    return ans


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        ans = solve(s)
        print(ans)


if __name__ == '__main__':
    main()
