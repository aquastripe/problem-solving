s = input()
ans = 'Yes' if all([s[i] == '0' for i in range(1, len(s), 2)]) else 'No'

print(ans)
