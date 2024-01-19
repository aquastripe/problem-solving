import numpy as np

SET_1_to_9 = set(n for n in range(1, 10))


def condition_1(a):
    for row in a:
        row = set(row)
        if row != SET_1_to_9:
            return False
    return True


def condition_2(a):
    for j in range(9):
        col = set(a[:, j])
        if col != SET_1_to_9:
            return False
    return True


def condition_3(a):
    for i in range(3):
        for j in range(3):
            r = i * 3
            c = j * 3
            block = set(a[r:r + 3, c:c + 3].flatten())
            if block != SET_1_to_9:
                return False
    return True


def main():
    a = []
    for _ in range(9):
        row = list(map(int, input().split()))
        a.append(row)
    a = np.array(a)
    ans = 'Yes' if condition_1(a) and condition_2(a) and condition_3(a) else 'No'
    print(ans)


if __name__ == '__main__':
    main()
