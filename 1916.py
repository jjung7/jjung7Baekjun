import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for i in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))

st, ed = map(int, input().split())

dist = [INF]*(n+1)
def dijkstra(start):
    dist[start] = 0
    q = [(0, st)]

    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w: #이미 처리되었다면 무시
            continue

        for dest, wei in g[cur]:
            cost = dist[cur] + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heapq.heappush(q, (cost, dest))

dijkstra(st)
print(dist[ed])
# import sys
# from collections import deque
# import heapq
# input = sys.stdin.readline

# N = int(input())
# M = int(input())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     s,e,cost = map(int,input().split())
#     graph[s].append((e,cost))
# start,end = map(int,input().split())
# min_cost = 1e9

# def bfs(start,end):
#     global min_cost
#     queue = deque([(start, 0)])  
#     heap = [(start, 0)]


#     visited = [False] * (N+1)
#     visited[start] = True
    
#     while heap:
#         q, total = heapq.heappop(heap)
#         for i, cost in graph[q]:
#             if not visited[i]:
#                 visited[i] = True
#                 heapq.heappush(heap, (total + cost, i)) 
#             if end == i:
#                 min_cost = min(min_cost, total + cost) 

# bfs(start, end)
# print(min_cost)

