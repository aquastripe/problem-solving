from collections import defaultdict

from atcoder.dsu import DSU


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


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    graph = defaultdict(list)
    for _ in range(m):
        u, v = read_tuple_int()
        u, v = u - 1, v - 1
        graph[u].append(v)
        graph[v].append(u)

    to_be_deleted = set()
    dsu = DSU(n)

    for u in range(n):
        if u in to_be_deleted:
            to_be_deleted.remove(u)

        for v in graph[u]:
            if v < u:
                dsu.merge(u, v)
            else:  # v > u
                to_be_deleted.add(v)

        if dsu.same(u, 0) and dsu.size(0) == (u + 1):
            print(len(to_be_deleted))
        else:
            print(-1)


if __name__ == '__main__':
    main()
