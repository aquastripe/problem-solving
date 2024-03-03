n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    buffer = []
    for j in range(n):
        if a[i][j]:
            buffer.append(j + 1)

    print(' '.join(map(str, buffer)))
