import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)] 
parent = [0 for _ in range(N+1)]
visited = [False] * (N+1) 
for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]: 
            if parent[i] == 0:
                parent[i] = start 
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(parent[i])
# import sys
# input = sys.stdin.readline
# N = int(input())
# graph = [[]*(N+1) for _ in range(N+1)]
# parent = [0 for _ in range(N+1)]
# print(parent)
# visited = [False] *(N+1)
# for _ in range(N-1):
#     a, b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# def dfs(start):
#     visited[start] = True
#     for i in graph[start]:
#         if not visited:
#             if parent[i] == 0:
#                 parent[i] = graph[start]
#             dfs(i)
# dfs(1)
# print(parent)


# def dfx(start):
    