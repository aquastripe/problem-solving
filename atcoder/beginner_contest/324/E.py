def compute_max_prefix_length_subsequence(s, t):
    max_prefix_length = 0
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            max_prefix_length += 1
            i += 1
            j += 1
        else:
            i += 1

    return max_prefix_length


def compute_max_suffix_length_subsequence(s, t):
    max_suffix_length = 0
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[-i - 1] == t[-j - 1]:
            max_suffix_length += 1
            i += 1
            j += 1
        else:
            i += 1

    return max_suffix_length


def main():
    n, t = input().split()
    n = int(n)
    a, b = [], []
    for _ in range(n):
        s = input()
        a.append(compute_max_prefix_length_subsequence(s, t))
        b.append(compute_max_suffix_length_subsequence(s, t))

    c = [0] * (len(t) + 1)
    for b_i in b:
        c[b_i] += 1

    ans = 0
    for i in range(n):
        l_i = max(len(t) - a[i], 0)
        for k in range(l_i, len(t) + 1):
            ans += c[k]

    print(ans)


if __name__ == '__main__':
    main()
