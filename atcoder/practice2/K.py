import sys
from collections import namedtuple

from atcoder.lazysegtree import LazySegTree

input = sys.stdin.readline
MOD = 998244353

F = namedtuple('F', ['b', 'c'])
S = namedtuple('S', ['value', 'size'])


def affine(data_1: S, data_2: S) -> S:
    return (data_1[0] + data_2[0]) % MOD, data_1[1] + data_2[1]


def mapping(lazy: F, data: S) -> S:
    value, size = data
    b, c = lazy
    return (value * b + size * c) % MOD, size


def composition(parent: F, child: F) -> F:
    # (data * b1 + c1) * b2 + c2
    # = data * b1 * b2 + c1 * b2 + c2
    # = data * (b1 * b2) + (c1 * b2 + c2)
    b2, c2 = parent
    b1, c1 = child
    return (b1 * b2) % MOD, (c1 * b2 + c2) % MOD


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(map(lambda a_i: (a_i, 1), a))
    segtree = LazySegTree(affine, (0, 0), mapping, composition, (1, 0), a)

    for _ in range(q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 0:
            l, r, b, c = cmd[1:]
            segtree.apply(l, r, (b, c))
        else:
            l, r = cmd[1:]
            print(segtree.prod(l, r)[0])


if __name__ == '__main__':
    main()
