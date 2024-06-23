from collections import defaultdict


def solve(n, k, a):
    d = defaultdict(list)
    a.sort()
    for a_i in a:
        d[a_i % k].append(a_i // k)

    ans = 0
    count_no_pairs = 0
    for b in d.values():
        if (len(b) % 2) == 1:
            if (n % 2) == 0:
                return -1
            else:
                count_no_pairs += 1

        if count_no_pairs > 1:
            return -1

        if (len(b) % 2) == 1:
            """
            1 2 3 4 5

            s_0 = -1 +2 -3 +4
            s_1 = -1 +2 -3    +5 = s_0 - b[3] + b[4]
            s_2 = -1 +2    -4 +5 = s_1 + b[2] - b[3]
            s_3 = -1    +3 -4 +5 = s_2 - b[1] + b[2]
            s_4 =    -2 +3 -4 +5 = s_3 + b[0] - b[1]
            """
            s = 0
            for i in range(0, len(b) - 1, 2):
                s += b[i + 1] - b[i]

            state = 1
            s_i = s
            for i in range(len(b) - 1, 0, -1):
                s_i = s_i + (b[i] - b[i - 1]) * state
                state *= -1
                s = min(s, s_i)

            ans += s
        else:
            for i in range(0, len(b) - 1, 2):
                ans += b[i + 1] - b[i]

    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ans = solve(n, k, a)
        print(ans)


if __name__ == '__main__':
    main()
