from operator import add
from atcoder.lazysegtree import LazySegTree


def _apply_lazy(lazy, data):
    return data + lazy


def _merge_lazy(parent, child):
    return parent + child


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    segtree = LazySegTree(add, 0, _apply_lazy, _merge_lazy, 0, a)

    for b_i in b:
        total = segtree.get(b_i)
        segtree.set(b_i, 0)

        # .....oooo: first round
        # ooooooooo: loops
        # ooooooooo
        # ooo......: last round

        begin = b_i + 1
        end = begin + total
        if begin == n:
            begin = 0
            end -= n

        if end > n:
            segtree.apply(begin, n, 1)
            total -= n - begin
            x, y = divmod(total, n)
            segtree.apply(0, n, x)
            segtree.apply(0, y, 1)
        else:
            segtree.apply(begin, end, 1)

    print(' '.join(map(str, list(map(segtree.get, range(n))))))


if __name__ == '__main__':
    main()
