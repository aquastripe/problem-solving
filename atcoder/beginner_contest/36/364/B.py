def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def is_valid(i, j, C, H, W):
    return 0 <= i < H and 0 <= j < W and C[i][j] == '.'


def main():
    H, W = read_tuple_int()
    S_i, S_j = read_tuple_int()
    S_i -= 1
    S_j -= 1
    C = [input() for _ in range(H)]
    X = input()
    for x in X:
        if x == 'U':
            next_i, next_j = S_i - 1, S_j
        elif x == 'D':
            next_i, next_j = S_i + 1, S_j
        elif x == 'L':
            next_i, next_j = S_i, S_j - 1
        else:
            next_i, next_j = S_i, S_j + 1

        if is_valid(next_i, next_j, C, H, W):
            S_i, S_j = next_i, next_j

    S_i += 1
    S_j += 1
    print(S_i, S_j)


if __name__ == '__main__':
    main()
