"""
Case 1:

101011
011011: 2
001111: 3

Case 2:

01101001
00111001: 3
00011101: 4
00001111: 4
"""


def solve(s):
    ans = 0
    count_1s = 0
    for c in s:
        if c == 1:
            count_1s += 1
        else:
            if count_1s > 0:
                ans += count_1s + 1

    return ans


def main():
    t = int(input())
    for _ in range(t):
        s = list(map(int, input()))
        ans = solve(s)
        print(ans)


if __name__ == '__main__':
    main()
