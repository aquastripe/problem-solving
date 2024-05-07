def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    s = input()
    t = input()
    i = 0
    ans = []
    for j in range(len(t)):
        if s[i] == t[j]:
            ans.append(j + 1)
            i += 1

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
