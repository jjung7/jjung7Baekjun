import sys
input = sys.stdin.readline
comp = int(input())
count = 0
M = int(input())
graph = [[] * (comp+1) for _ in range(comp+1)]
visited = [False] *(comp+1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if(not visited[i]):
            dfs(i)
dfs(1)
for j in range(2,len(visited)):
    if(visited[j] == True):
        count += 1

print(count)    