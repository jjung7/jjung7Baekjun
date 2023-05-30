import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
count = 0
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)] 
Visited = [False] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start):
    Visited[start] = True
    for i in graph[start]: 
        if not Visited[i]:
            dfs(i)

for i in range(1,N+1):
    if not Visited[i]:
        dfs(i)
        count+=1
print(count)
# import sys
# input = sys.stdin.readline
# count = 0
# N, M = map(int,input().split())
# graph = [[0]*(N+1) for _ in range(N+1)]
# Visited = [False] * (N+1)
# for _ in range(M):
#     a,b = map(int,input().split())
#     graph[a][b] = graph [b][a] = 1
# # graph.sort(key = lambda x: x[0])
# # print(graph)
# def dfs(start):
#     Visited[start] = True
#     for i in range(1,M+1):
#         if graph[start]==1 and Visited[i] == False:
#             Visited[i] = True
#             dfs(i)
# for i in range(1,N+1):
#     if Visited[i] == False:
#         dfs(i)
#         count+=1
# print(count)