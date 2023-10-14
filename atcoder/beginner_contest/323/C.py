from collections import defaultdict

n, m = tuple(map(int, input().split()))
a_list = list(map(int, input().split()))
a_i = sorted(list(enumerate(a_list)), key=lambda item: item[1], reverse=True)

s_list = []
scores = defaultdict(int)
for i in range(n):
    s = input()
    s_list.append(s)

    scores[i] = i + 1
    for j, c in enumerate(s):
        if c == 'o':
            scores[i] += a_list[j]

top_player, top_score = max(scores.items(), key=lambda item: item[1])
n_top_players = sum([score == top_score for score in scores.values()])

for i in range(n):
    if i == top_player:
        if n_top_players == 1:
            print(0)
        else:
            print(1)
    else:
        current_score = scores[i]
        n_problems_to_solve = 0
        for j, a in a_i:
            if s_list[i][j] == 'x':
                current_score += a
                n_problems_to_solve += 1

            if current_score > top_score:
                break

        print(n_problems_to_solve)
