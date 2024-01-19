from collections import defaultdict
from itertools import permutations

MAX_INT = 1_000_000


def main():
    m = int(input())
    s = defaultdict(lambda: defaultdict(list))
    for i in range(3):
        s_i = list(map(int, input()))
        for second, digit in enumerate(s_i):
            s[digit][i].append(second)
            s[digit][i].append(second + m)
            s[digit][i].append(second + 2 * m)

    minimum_seconds = MAX_INT
    indices_set = list(permutations(range(3)))
    for digit in s.keys():
        if len(s[digit]) != 3:
            continue

        for i in range(3):
            s[digit][i].sort()

        for indices in indices_set:
            non_repeated_seconds = set()
            for i in indices:
                for second in s[digit][i]:
                    if second not in non_repeated_seconds:
                        non_repeated_seconds.add(second)
                        break

            minimum_seconds = min(max(non_repeated_seconds), minimum_seconds)

    ans = minimum_seconds if minimum_seconds != MAX_INT else -1
    print(ans)


if __name__ == '__main__':
    main()
