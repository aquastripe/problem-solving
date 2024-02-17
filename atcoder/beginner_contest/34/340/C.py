TABLE = {
    1: 0
}


def solve(n):
    if n not in TABLE:
        if n % 2 == 0:
            TABLE[n] = 2 * solve(n // 2) + n
        else:
            TABLE[n] = solve(n // 2) + solve(n // 2 + 1) + n
    return TABLE[n]


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()
