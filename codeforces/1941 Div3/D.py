from collections import deque


def main():
    t = int(input())
    for _ in range(t):
        n, m, x = tuple(map(int, input().split()))

        p = {x}
        for i in range(m):
            r, c = input().split()
            r = int(r)

            q = set()
            for p_i in p:
                if c == '0':
                    q.add((p_i - 1 + r) % n + 1)
                elif c == '1':
                    q.add((p_i - 1 - r) % n + 1)
                else:
                    q.add((p_i - 1 + r) % n + 1)
                    q.add((p_i - 1 - r) % n + 1)
            p = q

        p = list(p)
        p.sort()
        print(len(p))
        print(' '.join(map(str, p)))


if __name__ == '__main__':
    main()
