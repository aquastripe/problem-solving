from collections import deque

"""
k = 3
L W W W L
  3 2 1
"""


def solve_2(n, m, k, a):
    n += 2
    a = 'L' + a + 'L'
    visited = [False] * n
    q = deque()
    visited[0] = True
    q.append((0, k))

    while len(q) > 0:
        u, k = q.popleft()
        if u == n - 1:
            return 'YES'

        if a[u] == 'W':
            v = u + 1
            if v < n and not visited[v] and a[v] != 'C':
                visited[v] = True
                if a[v] == 'L':
                    q.append((v, k))
                else:
                    if k - 1 >= 0:
                        q.append((v, k - 1))
        elif a[u] == 'L':
            for i in range(m):
                v = u + 1 + i
                if v < n and not visited[v] and a[v] != 'C':
                    visited[v] = True
                    if a[v] == 'L':
                        q.appendleft((v, k))
                    else:
                        if k - 1 >= 0:
                            q.append((v, k - 1))

    return 'NO'


def solve(n, m, k, a):
    dp = [0] * (n + 1)
    dist_jump = min(n + 1, m)
    reachable = [True] * dist_jump + [False] * (n + 1 - dist_jump)
    for i in range(dist_jump):
        dp[i] = k

    for i in range(n):
        if not reachable[i]:
            continue

        if a[i] == 'W':
            if dp[i] > 0:
                dp[i + 1] = max(dp[i + 1], dp[i] - 1)
                reachable[i + 1] = True
        elif a[i] == 'C':
            ...
        else:
            for j in range(m):
                if i + 1 + j <= n:
                    reachable[i + 1 + j] = True
                    dp[i + 1 + j] = max(dp[i + 1 + j], dp[i])

    if reachable[n]:
        return 'YES'

    return 'NO'


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = input()
        ans = solve_2(n, m, k, a)
        print(ans)


if __name__ == '__main__':
    main()
