def solve(a, b):
    min_length = 201
    for k in range(len(b)):
        length = k
        i, j = 0, 0
        while i < len(a) and (j + k) < len(b):
            if a[i] == b[j + k]:
                i += 1
                j += 1
            else:
                i += 1

            length += 1

        length += len(a) - i
        length += len(b) - (j + k)
        min_length = min(min_length, length)

    return min_length


def main():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        ans = solve(a, b)
        print(ans)


if __name__ == '__main__':
    main()
