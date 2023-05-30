import sys
input = sys.stdin.readline
T = int(input())
list1 = list(map(int,input().split()))
op = list(map(int,input().split()))
maximum = -10**9
minimum = 10**9
def dfs(depth,total,plus,minus,multiply,divide):
    global maximum, minimum
    if T == depth:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
    if plus > 0:
        dfs(depth+1, total + list1[depth],plus - 1,minus,multiply,divide)
    if minus > 0:
        dfs(depth+1, total - list1[depth],plus,minus-1,multiply,divide)
    if multiply >0:
        dfs(depth+1, total * list1[depth],plus,minus,multiply-1,divide)
    if divide > 0:
        dfs(depth+1, int(total / list1[depth]),plus,minus,multiply,divide-1)
dfs(1,list1[0],op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)        
