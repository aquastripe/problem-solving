def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def is_valid(keys, tests, k):
    for a, r in tests:
        test_keys = 0
        for a_i in a:
            test_keys |= 1 << a_i

        n_matched_keys = (keys & test_keys).bit_count()
        if r == 'o' and n_matched_keys < k or r == 'x' and n_matched_keys >= k:
            return False
    return True


def main():
    n, m, k = read_tuple_int()

    tests = []
    for _ in range(m):
        s = input().split()
        c, *a = list(map(lambda x: int(x) - 1, s[:-1]))
        r = s[-1]
        tests.append((a, r))

    ans = 0
    for keys in range(1 << n):
        if is_valid(keys, tests, k):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
