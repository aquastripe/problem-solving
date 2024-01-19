# i: 0, 1, 2, 3, 4
# a: 1, 2, 4, 7, 8
# i, a:
# 0, 1: (4-2)+(8-7) = (a[2]-a[1]) + (a[4]-a[3])
# 1, 2: (4-1)+(8-7) = (a[2]-a[0]) + (a[4]-a[3])
# 2, 4: (2-1)+(8-7) = (a[1]-a[0]) + (a[4]-a[3])
# 3, 7: (2-1)+(8-4) = (a[1]-a[0]) + (a[4]-a[2])
# 4, 8: (2-1)+(7-4) = (a[1]-a[0]) + (a[3]-a[2])

# prefix[0] = 0
# prefix[2] = (a[1]-a[0])
# prefix[4] = (a[1]-a[0]) + (a[3]-a[2])

# suffix[4] = suffix[k-1] = 0
# suffix[2] = (a[4]-a[3])
# suffix[0] = (a[4]-a[3]) + (a[2]-a[1])

# remove[0] = prefix[0] + suffix[0]
# remove[2] = prefix[2] + suffix[2]
# remove[4] = prefix[4] + suffix[4]

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k % 2 == 0:
        ans = 0
        for i in range(0, k, 2):
            ans += a[i + 1] - a[i]
    else:
        prefix_sum = [0] * k
        for i in range(2, k, 2):
            prefix_sum[i] = prefix_sum[i - 2] + (a[i - 1] - a[i - 2])

        suffix_sum = [0] * k
        for i in range(k - 3, -1, -2):
            suffix_sum[i] = suffix_sum[i + 2] + (a[i + 2] - a[i + 1])

        ans = 10 ** 9
        for i in range(0, k, 2):
            ans = min(ans, prefix_sum[i] + suffix_sum[i])

    print(ans)


if __name__ == '__main__':
    main()
