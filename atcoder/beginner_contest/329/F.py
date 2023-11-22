from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, q = tuple(map(int, input().split()))
    c = list(map(int, input().split()))
    s = [{c_i} for c_i in c]

    for _ in range(q):
        a, b = tuple(map(int, input().split()))
        a -= 1
        b -= 1
        if len(s[a]) < len(s[b]):
            s[b] |= s[a]
            s[a].clear()
        else:
            s[a] |= s[b]
            s[b].clear()
            s[a], s[b] = s[b], s[a]
        print(len(s[b]))


if __name__ == '__main__':
    main()
