import sys
from collections import deque
queue = deque()
input = sys.stdin.readline
T = int(input())
sum = 0
for i in range(T):
    num = int(input())
    if num == 0:
        queue.pop()
    else:
        queue.append(num)
for q in range(len(queue)):
    sum += queue[q]
print(sum)