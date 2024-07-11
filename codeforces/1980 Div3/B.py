import bisect


def main():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        a = list(map(int, input().split()))
        a_f = a[f - 1]
        count_a_f = sum(a_i == a_f for a_i in a)
        a.sort(reverse=True)
        if a[k - 1] == a_f:
            if k == n or k < n and a[k] != a_f:
                print('YES')
            else:
                print('MAYBE')
        elif a[k - 1] < a_f:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
