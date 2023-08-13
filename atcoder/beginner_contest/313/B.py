from collections import defaultdict


def main():
    N, M = list(map(int, input().split(' ')))
    num_stronger_than = defaultdict(int)

    for _ in range(M):
        a, b = list(map(int, input().split(' ')))
        num_stronger_than[b] += 1

    count = 0
    the_strongest = ...
    for p_i in range(1, N + 1):
        if num_stronger_than[p_i] == 0:
            count += 1

            if count > 1:
                the_strongest = -1
                break
            else:
                the_strongest = p_i

    print(the_strongest)


if __name__ == '__main__':
    main()
