a = []
while True:
    a_i = input()
    a.append(a_i)

    if a_i == '0':
        break

a = a[::-1]
print('\n'.join(a))
