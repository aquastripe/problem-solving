def main():
    n, l, r = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = []
    for a_i in a:
        if a_i <= l:
            ans.append(f'{l}')
        elif a_i >= r:
            ans.append(f'{r}')
        else:
            ans.append(f'{a_i}')
    print(' '.join(ans))


if __name__ == '__main__':
    main()
