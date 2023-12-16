k, g, m = map(int, input().split())
glass, mug = 0, 0
for _ in range(k):
    if glass == g:
        glass = 0
    elif mug == 0:
        mug = m
    else:
        transfer = min(g - glass, mug)
        glass += transfer
        mug -= transfer

print(glass, mug)
