def solve(n, s):
    for m in range(1, n):
        if n % m == 0:
            for t in [s[:m], s[-m:]]:
                count_diff = 0

                for j in range(n):
                    if s[j] != t[j % m]:
                        count_diff += 1

                    if count_diff > 1:
                        break

                if count_diff <= 1:
                    return m

    return n


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()

        m = solve(n, s)

        print(m)


if __name__ == '__main__':
    main()
