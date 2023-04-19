import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
T = int(input())
result = [0] * T
list1 = list(map(int,input().split()))
for j in range(len(list1)):
    while queue:
        if list1[queue[-1][0]] < list1[j]:
            queue.pop()
        else:
            result[j] = queue[-1][0] +1
            break
    queue.append((j,list1[j]))
print(*result)        
# while True:
#     for i in range(T-1):
#         for j in range(i+1,T):
#             if queue[i] <queue[j]:
#                 queue.popleft()
#                 print(queue[j].index())