import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
N = int(input())
for _ in range(N):    
    list1 = input().split()
    if list1[0] == "push":
        queue.append(list1[1])
    elif list1[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif list1[0] == "size":
        print(len(queue))
    elif list1[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif list1[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif list1[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

