from collections import defaultdict

n = int(input())
s_list = []
for _ in range(n):
    s = input()
    s_list.append(s)

counter = defaultdict(int)
for i in range(n):
    player_i = i + 1
    for j in range(i, n):
        player_j = j + 1

        if s_list[i][j] == 'o':
            counter[player_i] += 1
        else:
            counter[player_j] += 1
results = [(player, wins) for player, wins in counter.items()]
results = sorted(results, key=lambda item: item[0], reverse=False)
results = sorted(results, key=lambda item: item[1], reverse=True)

print(' '.join([f'{item[0]}' for item in results]))
