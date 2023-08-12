from collections import defaultdict

ans = defaultdict(list)
n = int(input())
for b in range(1, n + 1):
    c_i = int(input())
    a = list(map(int, input().split()))

    for a_i in a:
        ans[a_i].append((c_i, b))

x = int(input())
if x in ans:
    ans[x].sort(key=lambda item: item[1])
    ans[x].sort(key=lambda item: item[0])
    min_bet = ans[x][0][0]
    c_n = list(filter(lambda item: item[0] == min_bet, ans[x]))
    b = list(map(lambda item: str(item[1]), c_n))
    k = len(b)
    print(k)
    print(' '.join(b))
else:
    print('0')
