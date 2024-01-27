import bisect
import operator

n = int(input())
a = list(map(int, input().split()))
i_a = [(i + 1, a[i]) for i in range(n)]
i_a.sort(key=operator.itemgetter(1))

nums = set(range(1, n + 1))
for a_i in a:
    if a_i != -1:
        nums.remove(a_i)

num = nums.pop()

# i: 1 2  3 4 5 6
# a: 4 1 -1 5 3 2

i = 0
while i < n and i != num or i > num and i - 1 < n:
    if i > num:
        j, _ = i_a[i - 1]
    else:
        j, _ = i_a[i]

    print(j, end=' ')
    i = j

# 1  2  3 4  5
# 3 25 20 6 18 12 26 1 29 -1 21 17 23 9 8 30 10 15 22 27 4 13 5 11 16 24 28 2 19 7
