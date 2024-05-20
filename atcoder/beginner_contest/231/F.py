from operator import add

from atcoder.segtree import SegTree


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    a = read_list_int()
    b = read_list_int()

    b_unique = sorted(set(b))
    compress_b = {b_i: i for i, b_i in enumerate(b_unique)}
    ab = [(a_i, -compress_b[b_i]) for a_i, b_i in zip(a, b)]
    ab.sort()

    segtree = SegTree(add, 0, len(b_unique))
    ans = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and ab[i] == ab[j]:
            j += 1

        count = j - i
        a_i, n_b_i = ab[i]
        b_i = -n_b_i
        segtree.set(b_i, segtree.get(b_i) + count)

        ans += segtree.prod(b_i, len(b_unique)) * count
        i = j

    print(ans)


if __name__ == '__main__':
    main()
