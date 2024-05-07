from collections import defaultdict
from itertools import pairwise


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


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    c_a = []
    for _ in range(m):
        k, c = read_tuple_int()
        edges = list(map(lambda x: x - 1, read_list_int()))
        c_a.append((c, edges))
    c_a.sort()

    dsu_for_mst = DisjointSet(n)
    ans = 0
    for i in range(m):
        c, edges = c_a[i]

        for u, v in pairwise(edges):
            if not dsu_for_mst.same(u, v):
                dsu_for_mst.unite(u, v)
                ans += c

    if dsu_for_mst.size(0) != n:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
