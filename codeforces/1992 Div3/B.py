def solve(n, k, a):
    a.sort()
    count = 0
    for i in range(k - 1):
        count += 2 * a[i] - 1

    return count


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ans = solve(n, k, a)
        print(ans)


if __name__ == '__main__':
    main()
