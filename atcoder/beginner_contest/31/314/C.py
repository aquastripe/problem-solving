from collections import defaultdict

n, m = list(map(int, input().split()))
s = list(input())
c = list(map(lambda item: int(item) - 1, input().split()))

index = defaultdict(list)
c_index = defaultdict(list)

for i, c_i in enumerate(c):
    index[c_i].append(i)
    c_index[c_i].append(s[i])

for i in range(m):
    # rotate
    pos = index[i]
    c = c_index[i]
    rc = [c[j - 1] for j in range(len(c))]

    for j, c_j in zip(pos, rc):
        s[j] = c_j

print(''.join(s))
