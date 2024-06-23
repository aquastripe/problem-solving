def solve(s, idx, c):
    idx = list(set(idx))
    idx.sort()
    c.sort()
    for i, c_i in zip(idx, c):
        s[i] = c_i

    s = ''.join(s)
    return s


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = list(input())
        idx = list(map(lambda x: int(x) - 1, input().split()))
        c = list(input())
        ans = solve(s, idx, c)
        print(ans)


if __name__ == '__main__':
    main()
