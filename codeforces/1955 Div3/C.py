from collections import deque


def solve(n, k, a):
    a = deque(a)
    while k > 0 and len(a) > 0:
        if k // 2 == 0:
            a[0] -= 1
            if a[0] == 0:
                a.popleft()
            k -= 1
        elif len(a) > 1:
            m = min(a[0], a[-1], k // 2)
            a[0] -= m
            a[-1] -= m

            if a[0] == 0:
                a.popleft()

            if a[-1] == 0:
                a.pop()

            k -= 2 * m
        else:
            m = min(a[0], k)
            a[0] -= m
            if a[0] == 0:
                a.popleft()

            k -= m

    return n - len(a)


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ans = solve(n, k, a)
        print(ans)


if __name__ == '__main__':
    main()
