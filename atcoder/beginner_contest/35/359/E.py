def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    h = read_list_int()
    x = [(1, 2, 3, 4)]
    a, b, c, d = x[-1]
    h_max = 10 ** 9 + 1
    stack = [(-1, h_max, 0)]
    for w_i, h_i in enumerate(h):
        w_prev, h_prev, capacity_prev = stack[-1]
        while h_i > h_prev:
            stack.pop()
            w_prev, h_prev, capacity_prev = stack[-1]

        capacity_i = h_i * (w_i - w_prev)
        stack.append((w_i, h_i, capacity_prev + capacity_i))
        print(capacity_prev + capacity_i + 1, end=' ')
    print()


if __name__ == '__main__':
    main()
