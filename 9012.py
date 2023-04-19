import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
for i in range(n):
    queue1 = deque()
    command = list(input().strip())
    for j in range(len(command)):
        if(len(command) == j+1):
            if(command[j] == "("):
                queue1.append("(")
            elif command[j] == ")":
                if queue1:
                    queue1.pop()
                else:
                    print("NO")
                    break
            if(len(queue1) == 0):
                print("YES")
            else:
                print("NO")
        elif command[j] =="(":
            queue1.append("(")
        elif(command[j] == ")"):
            if(len(queue1) == 0):
                print("NO")
                break
            else:
                queue1.pop()
            


    # if len(queue1) == len(queue2):
    #     print("YES")
    # else:
    #     print("NO")  