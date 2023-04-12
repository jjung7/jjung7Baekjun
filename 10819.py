import sys
from itertools import permutations
 
 
n = int(input())
a = list(map(int,input().split()))
 
all = permutations(a)
ans = 0
 
for i in all:
    s = 0
    for j in range(1,n):
        s+=abs(i[j]-i[j-1])
    if ans<s:
        ans =s
print(ans)
# import sys
# from itertools import permutations
# T = int(input())
# a = list(map(int, input().split()))
# all = permutations(a)
# for i in range (all):
#     t = 0  
#     for k in range(i[k-1], i[k]):
#         t += abs(a[i])
#     if (t > add):
#         add = t
    
# print(add)
#20 1 15 4 10 8
# (15 - 1) + (1 - 13)
#19 14 11 6 2
#1 20 4 15 8 10
#19 16 11 7 2
# 19 14 11 6 2   