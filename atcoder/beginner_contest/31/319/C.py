from itertools import permutations

c = []
for _ in range(3):
    c += list(map(int, input().split()))
c = [(c_i, i) for i, c_i in enumerate(c)]

indices_in_line = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
indices_to_in_line_sets = {}
for i in range(9):
    indices_to_in_line_sets[i] = []
    for j in range(len(indices_in_line)):
        if i in indices_in_line[j]:
            indices_to_in_line_sets[i].append(j)

count_disappointed = 0
count_all = 0

for c_perm in permutations(c):
    count_all += 1

    is_disappointed = False
    in_line_sets = [[] for _ in range(len(indices_in_line))]
    for c_i, i in c_perm:
        for j in indices_to_in_line_sets[i]:
            in_line_sets[j].append(c_i)

            if len(in_line_sets[j]) == 2 and in_line_sets[j][0] == in_line_sets[j][1]:
                count_disappointed += 1
                is_disappointed = True
                break

        if is_disappointed:
            break

print(f'{(count_all - count_disappointed) / count_all}')
