def solve(n, s):
    ans = 99 * 9 ** 18
    for i in range(n - 1):
        t = []
        for j in range(n):
            if j == i:
                t.append(int(s[i] + s[i + 1]))
            elif j != (i + 1):
                t.append(int(s[j]))
            else:
                continue

        result = 0
        has_zero = False
        has_one = False
        for j in range(n - 1):
            if t[j] == 0:
                has_zero = True
                break
            elif t[j] == 1:
                has_one = True
            else:
                result += t[j]

        if has_zero:
            return 0

        if has_one and result == 0:
            result = 1

        ans = min(ans, result)

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(input())
        ans = solve(n, s)
        print(ans)


if __name__ == '__main__':
    main()
