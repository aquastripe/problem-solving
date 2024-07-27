def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    s = [input() for _ in range(n)]
    ans = 'Yes'
    for i in range(n - 2):
        if s[i] == 'sweet' and s[i + 1] == 'sweet':
            ans = 'No'
    print(ans)


if __name__ == '__main__':
    main()
