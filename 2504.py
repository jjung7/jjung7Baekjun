import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
command = list(input().strip())
sum = 1
ans = 0
for i in range(len(command)):
    if command[i] == "(":
        queue.append(command[i])
        sum *= 2
    elif command[i] == "[":
        queue.append(command[i])
        sum *= 3
    elif command[i] == ")":
        if len(queue) == 0 or queue[-1] == '[':
            ans = 0
            break
        if(command[i-1] == '('):
            ans += sum
        queue.pop()
        sum //=2
    elif command[i] == "]":
        if len(queue) == 0 or queue[-1] == '(':
            ans = 0
            break
        if command[i-1] == '[':
            ans += sum
        queue.pop()
        sum //= 3
if (queue):
    print(0)
else:
    print(ans)  