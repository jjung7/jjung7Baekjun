import sys
input = sys.stdin.readline
T = int(input())
a= list(map(int,input().split())) #10 20 10 30 20 50 4
dp = [1 for _ in range(T)]        # 2  3  1  3  1  4 1
print(dp)
for i in range(1,T): #1,2,3,4,5
    for j in range(i): #0
        if(a[j] < a[i]):# 10 < 20
            dp[i] = max(dp[i], dp[j]+1) #max(20, 1) replace
print(f'{max(dp)}')