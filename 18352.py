import sys
from collections import deque

input = sys.stdin.readline

N,M,K,X = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)]
distance = [0] * (N+1)
visited = [False] *(N+1)
for i in range(M):
    x, y = map(int,input().split())
    graph[x].append(y)
def bfs(V):
    ans = []
    queue = deque()
    queue.append(V)
    visited[V] = True
    distance[V] = 0
    while queue:
        start = queue.popleft() 
        for i in graph[start]:
            if not visited[i]:
                visited[i] = True
                queue.append(i) 
                distance[i] = distance[start] +1
                if distance[i] == K:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)
bfs(X)

    

# print(bfs(X))
