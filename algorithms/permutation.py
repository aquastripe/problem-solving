def permutation(a, i, n):
    if i == n:
        print(' '.join(map(str, a)))
        return

    for j in range(i, n):
        a[i], a[j] = a[j], a[i]
        permutation(a, i + 1, n)
        a[i], a[j] = a[j], a[i]


def main():
    n = 3
    permutation(list(range(1, n + 1)), 0, n)


if __name__ == '__main__':
    main()
