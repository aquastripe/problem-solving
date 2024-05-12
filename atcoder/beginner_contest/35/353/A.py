def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = int(input())
    h = read_list_int()
    for i in range(n):
        if h[i] > h[0]:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
