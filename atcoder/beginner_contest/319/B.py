n = int(input())

for i in range(n + 1):
    has_divisors = False
    for j in range(1, 10):
        if (i * j) % n == 0:
            print(j, end='')
            has_divisors = True
            break

    if not has_divisors:
        print('-', end='')

print()
