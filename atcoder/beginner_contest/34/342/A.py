from collections import defaultdict

s = input()

count = defaultdict(int)
last = defaultdict(int)
for i, s_i in enumerate(s):
    count[s_i] += 1
    last[s_i] = i + 1

for s_i, n in count.items():
    if n == 1:
        print(last[s_i])
