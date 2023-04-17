import sys
from collections import deque
queue = deque()
N = int(input())
for _ in range(1,N+1):
    queue.append(_)
while len(queue)-1 > 0:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])

