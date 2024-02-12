q = int(input())
a = []
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        a.append(x)
    else:
        print(a[-x])
