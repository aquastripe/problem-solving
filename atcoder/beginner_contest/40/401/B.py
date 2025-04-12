def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


STATE_LOGGED_IN = 0
STATE_LOGGED_OUT = 1


def main():
    n = read_int()
    state = STATE_LOGGED_OUT
    ans = 0
    for _ in range(n):
        s = input()
        if s == 'login':
            state = STATE_LOGGED_IN
        elif s == 'logout':
            state = STATE_LOGGED_OUT
        elif s == 'private' and state == STATE_LOGGED_OUT:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
