from collections import defaultdict


def main():
    s = input()
    counter = defaultdict(int)
    distinctive_sum = [0] * len(s)
    for i in range(len(s) - 1, -1, -1):
        distinctive_sum[i] = len(s) - i - 1 - counter[s[i]]
        counter[s[i]] += 1

    ans = 0
    for i in range(len(s)):
        ans += distinctive_sum[i]

    ans += any(value > 1 for value in counter.values())

    print(ans)


if __name__ == '__main__':
    main()

"""
aabbc
baabc
babac
cabba
ababc
abbac
acbba
aacbb
aabcb

aabbc
  a a b b c
i 0 1 2 3 4
d 2 2 1 1 0

abbc
babc
bbac
cbbc
acbb
abcb

abcb
"""
