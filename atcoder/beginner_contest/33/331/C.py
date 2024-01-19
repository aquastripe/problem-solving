from operator import itemgetter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_i = [(i, e) for i, e in enumerate(a)]
    a_i.sort(key=itemgetter(1), reverse=True)
    ans = [0] * len(a_i)
    is_first = True
    suffix_sum = 0
    buffer = 0
    for i, (j, e) in enumerate(a_i):
        if is_first:
            ans[j] = 0
            buffer = e
            is_first = False
        else:
            if a_i[i][1] < a_i[i - 1][1]:
                suffix_sum += buffer
                ans[j] = suffix_sum
                buffer = e
            else:
                buffer += a_i[i - 1][1]
                ans[j] = suffix_sum

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
