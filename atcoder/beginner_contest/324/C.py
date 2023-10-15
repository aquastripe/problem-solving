def is_diff_by_1_insertion(a, b):
    i, j = 0, 0
    n_diff = 0
    while i < len(a) and j < len(b) and n_diff < 2:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1
            n_diff += 1

    n_diff += (len(a) - i) + (len(b) - j)
    return n_diff == 1


def is_diff_by_1_change(a, b):
    i, j = 0, 0
    n_diff = 0
    while i < len(a) and j < len(b) and n_diff < 2:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            i += 1
            j += 1
            n_diff += 1

    n_diff += (len(a) - i) + (len(b) - j)
    return n_diff == 1


def solve_1(n, t):
    ans = []
    for i in range(1, n + 1):
        s = input()

        if s == t or is_diff_by_1_insertion(s, t) or is_diff_by_1_insertion(t, s) or is_diff_by_1_change(s, t):
            ans.append(f'{i}')
    return ans


def compute_prefix_length(a, b):
    min_len = min(len(a), len(b))
    prefix_length = 0
    for i in range(min_len):
        if a[i] == b[i]:
            prefix_length += 1
        else:
            break
    return prefix_length


def compute_suffix_length(a, b):
    min_len = min(len(a), len(b))
    suffix_length = 0
    for i in range(min_len):
        if a[-i - 1] == b[-i - 1]:
            suffix_length += 1
        else:
            break
    return suffix_length


def solve_2(n, t_prime):
    ans = []
    for i in range(1, n + 1):
        s = input()
        prefix_length = compute_prefix_length(s, t_prime)
        suffix_length = compute_suffix_length(s, t_prime)
        case_1 = prefix_length == suffix_length == len(t_prime) == len(s)
        case_2 = prefix_length + suffix_length >= len(s) == len(t_prime) - 1
        case_3 = prefix_length + suffix_length >= len(s) - 1 == len(t_prime)
        case_4 = prefix_length + suffix_length >= len(s) - 1 == len(t_prime) - 1

        if case_1 or case_2 or case_3 or case_4:
            ans.append(f'{i}')

    return ans


def main():
    n, t_prime = input().split()
    n = int(n)
    ans = solve_2(n, t_prime)

    print(len(ans))
    print(' '.join(ans))


if __name__ == '__main__':
    main()
