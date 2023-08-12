n = int(input())
s = list(input())
q = int(input())

s_stat = [(0, c) for c in s]
fill = None

for i in range(q):
    t, x, c = list(input().split())
    x = int(x)

    if t == '1':
        s_stat[x - 1] = (i, c)
    else:
        fill = (i, t)

for last_updated_time, c in s_stat:
    if fill is None:
        print(c, end='')
        continue

    if last_updated_time > fill[0]:
        print(c, end='')
    else:
        if fill[1] == '2':
            print(c.lower(), end='')
        else:
            print(c.upper(), end='')

print()
