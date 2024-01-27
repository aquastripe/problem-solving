s = input()
mapping = ['A', 'B', 'C']
state = 0

ans = 'Yes'

i = 0
while i < len(s):
    j = i + 1

    if state < 3:
        while state < 3 and s[i] != mapping[state]:
            state += 1

        if state == 3:
            ans = 'No'
            break

        while j < len(s) and s[i] == s[j]:
            j += 1

        state += 1
    else:
        ans = 'No'
        break

    i = j

print(ans)
