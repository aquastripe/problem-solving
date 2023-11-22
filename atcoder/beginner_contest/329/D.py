from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = tuple(input().split())
    a = list(map(int, input().split()))

    max_a = None
    max_value = 0
    count = defaultdict(int)
    for a_i in a:
        count[a_i] += 1
        if count[a_i] > max_value:
            max_a = a_i
            max_value = count[a_i]

        if count[a_i] == max_value and a_i < max_a:
            max_a = a_i

        print(max_a)


if __name__ == '__main__':
    main()
