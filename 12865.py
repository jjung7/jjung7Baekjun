n, k = [int(x) for x in input().split()]
table = [0] * (k+1)
for _ in range(n):
    w, v = [int(x) for x in input().split()]
    if w > k:
      continue
    for j in range(k, 0, -1):
      if j + w <= k and table[j] != 0:
        table[j+w] = max(table[j+w], table[j] + v)
    table[w] = max(table[w], v)
print(max(table))
# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())
# dp = [0] * (K+1)
# weights = []
# for _ in range(1,N+1):
#     W,V = map(int,input().split())
#     dp[W] = V
#     weights.append(W)
# for weight in weights: #4, 3, 4, 6, 7
#     for j in range(0, K+1):
#         if weight + j <= K:
#             adsf       
# print(dp[K])

      
# import sys
# input = sys.stdin.readline

# N,K = map(int,input().split())
# dp = [[0]*(K+1) for _ in range(K+1)]
# for _ in range(N):
#     W,V = map(int,input().split())
#     dp[0][W] = V
#     dp[W][0] = V
# for i in range(1,K+1):
#     for j in range(i,K+1):
#         if i + j > K or dp[i][0] == 0 or dp[0][j] == 0:
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#         else:
#             dp[i][j] = dp[i][j-1] + dp[i-1][j]
# print(dp)