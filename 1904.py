import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


T = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3,T+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[T])
# dp = [0] *(T+1)

# def zerone(n): 
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif dp[n] != 0:
#         return dp[n]
#     else:
#         dp[n] = (zerone(n-1) + (zerone(n-2))) % 15746 
#         return dp[n]

# zerone(T)
# print(dp[T])