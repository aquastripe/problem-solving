def main():
    n = int(input())
    a = list(map(int, input().split()))
    prev = dict()
    next_ = dict()
    next_['head'] = a[0]
    prev['tail'] = a[n - 1]
    for i in range(n):
        if i == 0:
            prev[a[i]] = 'head'
        else:
            prev[a[i]] = a[i - 1]
        if i == n - 1:
            next_[a[i]] = 'tail'
        else:
            next_[a[i]] = a[i + 1]

    q = int(input())
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1:]
            z = next_[x]
            next_[y] = z
            next_[x] = y
            prev[y] = x
            prev[z] = y
        else:
            x = query[1]
            w = prev[x]
            y = next_[x]
            next_[w] = y
            prev[y] = w

    curr = 'head'
    while next_[curr] != 'tail':
        print(next_[curr], end=' ')
        curr = next_[curr]
    print()


if __name__ == '__main__':
    main()
