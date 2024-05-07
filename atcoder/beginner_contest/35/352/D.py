from atcoder.segtree import SegTree


def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, k = read_tuple_int()
    p = read_list_int()
    p_i_list = [(p_i, i + 1) for i, p_i in enumerate(p)]
    p_i_list.sort()
    indices = [i for p_i, i in p_i_list]

    min_segtree = SegTree(min, 2 * 10 ** 5 + 1, indices)
    max_segtree = SegTree(max, 0, indices)

    ans = 2 * 10 ** 5 + 1
    for j in range(n - k + 1):
        i1 = min_segtree.prod(j, j + k)
        ik = max_segtree.prod(j, j + k)

        ans = min(ans, ik - i1)

    print(ans)


if __name__ == '__main__':
    main()
