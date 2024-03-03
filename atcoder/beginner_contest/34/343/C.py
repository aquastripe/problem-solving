n = int(input())
ans = 0
max_x = 10 ** 6
for x in range(max_x + 1):
    k = x ** 3
    if k > n:
        break

    k_str = str(k)
    if k_str == k_str[::-1]:
        ans = max(ans, k)

print(ans)
