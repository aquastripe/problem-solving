def manachers_odd(s):
    s = '^' + s + '$'
    n = len(s)
    d_odd = [0] * n
    l, r = 1, 1
    for i in range(1, n - 1):
        d_odd[i] = max(0, min(r - i, d_odd[l + (r - i)]))

        # trivial
        while s[i - d_odd[i]] == s[i + d_odd[i]]:
            d_odd[i] += 1

        if i + d_odd[i] > r:
            l, r = i - d_odd[i], i + d_odd[i]

    return d_odd[1:-1]


def manachers_algorithm(s):
    s = '#' + '#'.join(s) + '#'
    d = manachers_odd(s)
    d_odd = [d[2 * i + 1] // 2 for i in range(len(d) // 2)]
    d_even = [d[2 * i] - 1 for i in range(len(d) // 2)]
    return d, d_odd, d_even


def main():
    s = 'abcbcba'
    print(manachers_algorithm(s))


if __name__ == '__main__':
    main()
