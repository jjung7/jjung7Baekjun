import sys
import heapq
input = sys.stdin.readline

T = int(input())
graph = [] * T
for _ in range(T):
    graph.append(list(map(int,input().rstrip())))
visited = [[False] * (T) for _ in range (T)]

def bfs():
    visited[0][0] = True
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    heap = []
    heapq.heappush(heap,[0,0,0])
    while heap:
        a, x, y = heapq.heappop(heap)
        if x == T-1 and y == T-1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < T and 0 <= ny < T and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    heapq.heappush(heap,[a+1, nx, ny])
                else:
                    heapq.heappush(heap,[a,nx,ny])
bfs()