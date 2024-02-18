from atcoder.segtree import SegTree
from operator import add


def main():
    n, q = map(int, input().split())
    s = list(map(int, input()))
    a = [1] + [int(s[i] != s[i + 1]) for i in range(n - 1)]
    # modifying
    #
    # i: 0123456789
    # s:  101010101
    # a: 111111111
    # flip s[2, 5]
    # s:  110100101
    # a: 101110111
    # flip s[1, 3]
    # s:  010010101
    # a: 111011111
    # flip s[8, 9]
    # s:  101010110
    # a: 111111101
    # = flip a[l-1] and a[r]
    #
    # query s[1:3]
    # s:  010010101
    # a: 111011111
    # = sum(11) = 2 = sum(a[1, 2])
    #
    # i: 0123
    # s:  101
    # a: 111
    segtree = SegTree(add, 0, a)

    for _ in range(q):
        cmd, l, r = list(map(int, input().split()))
        if cmd == 1:
            if l - 1 != 0:
                l_bit = segtree.get(l - 1)
                segtree.set(l - 1, 1 - l_bit)

            if r != n:
                r_bit = segtree.get(r)
                segtree.set(r, 1 - r_bit)
        else:
            d = segtree.prod(l, r)
            ans = 'Yes' if d == (r - l) else 'No'
            print(ans)


if __name__ == '__main__':
    main()
