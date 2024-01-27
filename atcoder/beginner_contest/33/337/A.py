n = int(input())
x_sum = 0
y_sum = 0

for _ in range(n):
    x_i, y_i = map(int, input().split())
    x_sum += x_i
    y_sum += y_i

if x_sum == y_sum:
    print('Draw')
elif x_sum > y_sum:
    print('Takahashi')
else:
    print('Aoki')
