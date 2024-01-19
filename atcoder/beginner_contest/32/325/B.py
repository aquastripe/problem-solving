# 10/21/2023
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    n_employees = [0] * 32
    for _ in range(n):
        w, x = list(map(int, input().split()))
        n_employees[x] += w
        if x < 8:
            n_employees[x + 24] += w

    sliding_window = [0] * 32
    sliding_window[0] = sum(n_employees[:9])
    for i in range(1, 24):
        sliding_window[i] = sliding_window[i - 1] + n_employees[i + 8] - n_employees[i - 1]

    print(max(sliding_window))


if __name__ == "__main__":
    main()
