from operator import mod
from collections import Counter


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a_sum_mod_3 = sum(a) % 3
        a_mod_3 = list(map(lambda x: mod(x, 3), a))
        counter = Counter(a_mod_3)

        # a_i mod 3 = 0, 1, 2
        count = 0
        while a_sum_mod_3 != 0:
            if counter[a_sum_mod_3]:
                counter[a_sum_mod_3] -= 1
                a_sum_mod_3 -= a_sum_mod_3
            else:
                a_sum_mod_3 += 1
                a_sum_mod_3 %= 3

            count += 1

        print(count)


if __name__ == '__main__':
    main()
