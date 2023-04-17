import sys
from collections import deque
queue = deque()
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] =="top":
        if queue:
            print(queue[-1])
        else:
            print(-1)