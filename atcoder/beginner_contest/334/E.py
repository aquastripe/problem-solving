from collections import defaultdict
from itertools import product


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


def is_valid(i, j, h, w):
    return 0 <= i < h and 0 <= j < w


def main():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    dsu = DisjointSet(h * w)
    n_red = 0
    for i, j in product(range(h), range(w)):
        if grid[i][j] == '#':
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if is_valid(ni, nj, h, w) and grid[ni][nj] == '#':
                    dsu.unite(i * w + j, ni * w + nj)
        else:
            n_red += 1

    clusters = set()
    for i, j in product(range(h), range(w)):
        if grid[i][j] == '#':
            clusters.add(dsu.root(i * w + j))

    n_connected_green = len(clusters)
    sum_n_connected_green = 0
    prime = 998244353
    for i, j in product(range(h), range(w)):
        if grid[i][j] == '.':
            n_connected_components_neighbors = set()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if is_valid(ni, nj, h, w) and grid[ni][nj] == '#':
                    n_connected_components_neighbors.add(dsu.root(ni * w + nj))

            sum_n_connected_green += (n_connected_green - len(n_connected_components_neighbors) + 1) % prime
            sum_n_connected_green %= prime

    n_red_inv = pow(n_red, -1, prime)
    ans = sum_n_connected_green * n_red_inv % prime
    print(ans)


if __name__ == '__main__':
    main()
