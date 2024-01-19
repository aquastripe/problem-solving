def main():
    n, q = list(map(int, input().split()))
    s = input()
    is_consecutive = [0] + [s[i - 1] == s[i] for i in range(1, n)]
    prefix_sum = [0] * n
    for i in range(n):
        prefix_sum[i] += prefix_sum[i - 1] + is_consecutive[i]

    ans = []
    for _ in range(q):
        l, r = tuple(map(int, input().split()))
        ans.append(f'{prefix_sum[r - 1] - prefix_sum[l - 1]}')
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
