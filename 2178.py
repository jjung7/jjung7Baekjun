import sys
from collections import deque
input = sys.stdin.readline

row,col = map(int,input().split())
graph = []
for _ in range(row):
    graph.append(list(map(int,input().rstrip())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        q, p = queue.popleft()
        for i in range(4):
            new_x = q + dx[i]
            new_y = p + dy[i]
            if(0 <= new_x < row and 0 <= new_y < col and graph[new_x][new_y] == 1):
                queue.append((new_x,new_y))
                graph[new_x][new_y] = graph[q][p] + 1
    return graph[row-1][col-1]
print(bfs(0,0))