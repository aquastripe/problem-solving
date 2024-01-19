from collections import defaultdict
from itertools import combinations


class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self._size = [1] * n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return None, None
        if self._size[a] > self._size[b]:
            a, b = b, a
        self.parent[a] = b
        self._size[b] += self._size[a]
        return a, b  # tree a merges into tree b

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, x):
        return self._size[self.root(x)]

    def __str__(self):
        clusters = defaultdict(list)
        for x in range(self.n):
            clusters[self.root(x)].append(x)
        return str(list(clusters.values()))


def main():
    n, m, k = tuple(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = tuple(map(int, input().split()))
        edges.append((u, v, w))

    ans = int(1e15)
    for edge_set in combinations(edges, n - 1):
        disjoint_set = DisjointSet(n + 1)
        is_not_msp = False
        cost = 0
        for u, v, w in edge_set:
            if disjoint_set.same(u, v):
                is_not_msp = True
                break

            disjoint_set.unite(u, v)
            cost += w

        if is_not_msp:
            continue

        ans = min(ans, cost % k)

    print(ans)


if __name__ == '__main__':
    main()
