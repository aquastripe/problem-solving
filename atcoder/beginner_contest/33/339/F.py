import random
from collections import defaultdict


def main():
    n = int(input())
    a = [input() for _ in range(n)]

    n_mods = 3
    mods = [random.randint(2 ** 15, 2 ** 16) for _ in range(n_mods)]
    vecs = []
    for a_i in a:
        vec = []
        for mod in mods:
            num = 0
            for c in a_i:
                num *= 10
                num += ord(c) - ord('0')
                num %= mod
            vec.append(num)
        vecs.append(vec)

    counter = defaultdict(int)
    for i in range(n):
        for j in range(n):
            counter[tuple(vecs[i][k] * vecs[j][k] % mods[k] for k in range(n_mods))] += 1

    ans = 0
    for i in range(n):
        ans += counter[tuple(vecs[i][k] % mods[k] for k in range(n_mods))]
    print(ans)


if __name__ == '__main__':
    main()
