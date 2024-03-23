from collections import defaultdict


def main():
    h, w, m = map(int, input().split())
    tax = []
    for _ in range(m):
        tax.append(map(int, input().split()))

    count = defaultdict(int)
    count[0] = h * w
    n_zeros_row = w
    n_zeros_col = h
    unset_row = set(range(h))
    unset_col = set(range(w))
    for i in range(m - 1, -1, -1):
        t, a, x = tax[i]

        if t == 1:
            if a - 1 not in unset_row:
                continue

            unset_row.remove(a - 1)
            count[x] += n_zeros_row
            count[0] -= n_zeros_row
            n_zeros_col -= 1
        else:
            if a - 1 not in unset_col:
                continue

            unset_col.remove(a - 1)
            count[x] += n_zeros_col
            count[0] -= n_zeros_col
            n_zeros_row -= 1

    keys = sorted(list(filter(lambda num: count[num] != 0, count.keys())))
    print(len(keys))
    for k in keys:
        print(f'{k} {count[k]}')


if __name__ == '__main__':
    main()
