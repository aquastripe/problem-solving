"""
State definition:
  dp[i][j]: the maximum value achievable by considering the first items with a total weight not exceeding j.

Initialization:
  dp[0][j] = 0 for all j  # no items are taken, so the total value is 0 regardless of the weight limit.

State transition:
  for each item i from 1 to N
    dp[i][j] = max(dp[i-1][j],           # skip item i
                   dp[i-1][j-w_i] + v_i) # take item i (if the weight allows)

Final answer:
  dp[N][W]
"""

N, W = map(int, input().split())
items = []

for _ in range(N):
  w, v = map(int, input().split())
  items.append((w, v))

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, W+1):
    w, v = items[i-1]
    if j-w >= 0:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][W])
