def solve(a, b, c):
    n_tents_a = a
    n_tents_b = (b + 2) // 3
    b_rest = (3 - b % 3) % 3
    c_rest = c - b_rest
    if c_rest < 0:
        return -1

    n_tents_c = (c_rest + 2) // 3
    return n_tents_a + n_tents_b + n_tents_c


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        ans = solve(a, b, c)
        print(ans)


if __name__ == '__main__':
    main()
