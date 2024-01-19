from operator import itemgetter


def main():
    n, m, l = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [(i + 1, e) for i, e in enumerate(a)]
    b = [(i + 1, e) for i, e in enumerate(b)]
    b.sort(key=itemgetter(1), reverse=True)

    not_offered_set = set()
    for _ in range(l):
        c, d = map(int, input().split())
        not_offered_set.add((c, d))

    ans = 0
    for i, a_i in a:
        for j, b_j in b:
            if (i, j) in not_offered_set:
                continue
            else:
                ans = max(ans, a_i + b_j)
                break

    print(ans)


if __name__ == '__main__':
    main()
