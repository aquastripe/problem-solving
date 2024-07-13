def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n = read_int()
    l_r = []
    for _ in range(n):
        l, r = read_tuple_int()
        l_r.append((l, r))

    sum_ans = 0
    ans = []
    for i in range(n):
        l, r = l_r[i]
        sum_ans += l
        ans.append(l)

    for i in range(n):
        if sum_ans == 0:
            break

        l, r = l_r[i]
        if sum_ans < 0:
            d = min(r - ans[i], -sum_ans)
            sum_ans += d
            ans[i] += d

    if sum_ans == 0:
        print('Yes')
        print(*ans)
    else:
        print('No')


if __name__ == '__main__':
    main()
