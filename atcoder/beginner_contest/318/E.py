from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

indices = defaultdict(list)
for i, a in enumerate(A):
    indices[a].append(i)

indices_list = list(filter(lambda item: len(item) >= 2, indices.values()))

count = 0
for indices in indices_list:
    for i in range(len(indices) - 1):
        count_left = i + 1
        count_mid = indices[i + 1] - indices[i] - 1
        count_right = len(indices) - i - 1
        count += count_left * count_mid * count_right

print(count)
