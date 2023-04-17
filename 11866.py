import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n, order = map(int,input().split())
count = 1
for i in range(1,n+1):
    queue.append(i)
list1 = []
while len(queue) > 0:
    if count == order:
        list1.append(queue.popleft())
        count = 1
    else:
        queue.append(queue.popleft())
        count += 1
print("<", end = '')
print(*list1, sep=', ', end = '')
print(">")
