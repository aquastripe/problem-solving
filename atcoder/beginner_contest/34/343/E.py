from itertools import product


def volume_intersect_2(cube1, cube2):
    volume = 1
    for x1, x2 in zip(cube1, cube2):
        volume *= max(0, min(x1, x2) + 7 - max(x1, x2))
    return volume


def volume_intersect_3(cube1, cube2, cube3):
    volume = 1
    for x1, x2, x3 in zip(cube1, cube2, cube3):
        volume *= max(0, min(x1, x2, x3) + 7 - max(x1, x2, x3))
    return volume


def solve(v1, v2, v3):
    a1, b1, c1 = 0, 0, 0
    for a2, b2, c2 in product(range(8), range(8), range(8)):
        for a3, b3, c3 in product(range(-7, 8), range(-7, 8), range(-7, 8)):
            w3 = volume_intersect_3((a1, b1, c1), (a2, b2, c2), (a3, b3, c3))

            w2_12 = volume_intersect_2((a1, b1, c1), (a2, b2, c2)) - w3
            w2_23 = volume_intersect_2((a2, b2, c2), (a3, b3, c3)) - w3
            w2_13 = volume_intersect_2((a1, b1, c1), (a3, b3, c3)) - w3
            w2 = w2_12 + w2_23 + w2_13

            w1_1 = 7 * 7 * 7 - w2_12 - w2_13 - w3
            w1_2 = 7 * 7 * 7 - w2_12 - w2_23 - w3
            w1_3 = 7 * 7 * 7 - w2_13 - w2_23 - w3
            w1 = w1_1 + w1_2 + w1_3

            if v1 == w1 and v2 == w2 and v3 == w3:
                return True, (a1, b1, c1, a2, b2, c2, a3, b3, c3)

    return False, None


def main():
    v1, v2, v3 = map(int, input().split())
    ans = solve(v1, v2, v3)
    if ans[0]:
        print('Yes')
        print(' '.join(map(str, ans[1])))
    else:
        print('No')


if __name__ == '__main__':
    main()
