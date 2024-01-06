import sys

from collections import defaultdict

input = sys.stdin.readline


class DisjointSet:
    def __init__(self, N):
        self.N = N
        self.par = [-1] * N
        self.sz = [1] * N

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return None, None
        if self.sz[a] > self.sz[b]:
            a, b = b, a
        self.par[a] = b
        self.sz[b] += self.sz[a]
        return a, b  # tree a merges into tree b

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, x):
        return self.sz[self.root(x)]

    def __str__(self):
        clusters = defaultdict(list)
        for x in range(self.N):
            clusters[self.root(x)].append(x)
        return str(list(clusters.values()))


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    edges_on_num = defaultdict(list)
    dsu = DisjointSet(n)
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1

        if a[u] > a[v]:
            edges_on_num[a[u]].append((u, v))
        elif a[v] > a[u]:
            edges_on_num[a[v]].append((v, u))
        else:
            dsu.unite(u, v)

    dp = [0] * n
    dp[dsu.root(n - 1)] = 1
    nums = list(edges_on_num.keys())
    nums.sort(reverse=True)
    for num in nums:
        edges = edges_on_num[num]
        for u, v in edges:
            u, v = dsu.root(u), dsu.root(v)
            if dp[u] > 0:
                dp[v] = max(dp[v], dp[u] + 1)

    print(dp[dsu.root(0)])


if __name__ == '__main__':
    main()
