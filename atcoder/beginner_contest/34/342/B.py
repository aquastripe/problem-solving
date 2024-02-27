n = int(input())
p = list(map(int, input().split()))
pos = {p_i: i for i, p_i in enumerate(p)}

q = int(input())

for _ in range(q):
    a, b = map(int, input().split())
    if pos[a] < pos[b]:
        print(a)
    else:
        print(b)
