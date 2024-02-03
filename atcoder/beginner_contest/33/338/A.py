s = input()
if s[0].isupper() and (len(s) == 1 or len(s) > 1 and all(s[i].islower() for i in range(1, len(s)))):
    print('Yes')
else:
    print('No')
