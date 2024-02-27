import string


def main():
    n = int(input())
    s = input()
    q = int(input())

    table = {c: c for c in string.ascii_lowercase}  # type: dict[str, str]
    for _ in range(q):
        c, d = input().split()

        for a in string.ascii_lowercase:
            if table[a] == c:
                table[a] = d

    t = list(table[s_i] for s_i in s)
    print(''.join(t))


if __name__ == '__main__':
    main()
