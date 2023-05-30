import sys

input = sys.stdin.readline

T = int(input())
dp = [0,1]
def fibo(n):
    if n < len(dp):
        return dp[n]
    else:
        dp.append(fibo(n-1) + fibo(n-2))
        return(dp[n])
print(fibo(T))