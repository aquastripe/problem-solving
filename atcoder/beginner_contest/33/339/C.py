n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = a[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

min_prefix_sum = min(prefix_sum)
ans = prefix_sum[-1] + (0 if min_prefix_sum >= 0 else -min_prefix_sum)
print(ans)
