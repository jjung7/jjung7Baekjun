import sys
from collections import deque

R, C = map(int, input().rstrip().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 문자열 한 줄 이런식으로 하면 됨
arr = [list(map(str, input())) for _ in range(R)]
ch = [[0] * C for _ in range(R)]
gsdc = deque()  # 고슴도치
water = deque()  # 물
cnt = 0

for i in range(R):
    for j in range(len(arr[i])):
        if arr[i][j] == 'S':
            gsdc.append((i, j))
            ch[i][j] = 1
        elif arr[i][j] == '*':
            water.append((i, j))


while len(gsdc) != 0:
    cur_loop = len(water)
    for i in range(cur_loop):
        tmp = water.popleft()
        for j in range(4):
            yy = tmp[0]+dy[j]
            xx = tmp[1]+dx[j]
            if yy < 0 or xx < 0 or yy >= R or xx >= C or arr[yy][xx] == 'X' or arr[yy][xx] == 'D' or arr[yy][xx] == '*':
                continue
            if arr[yy][xx] == '.':
                water.append((yy, xx))
                arr[yy][xx] = '*'

    cnt += 1  # 시간 증가

    # 고슴도치 움직이는 로직
    cur_loop = len(gsdc)
    # 큐에 있는 모든 경우를 다 돌아 봐야함
    for _ in range(cur_loop):
        cur = gsdc.popleft()
        for i in range(4):
            yy = cur[0]+dy[i]
            xx = cur[1]+dx[i]
            if yy < 0 or xx < 0 or yy >= R or xx >= C or arr[yy][xx] == 'X' or arr[yy][xx] == '*':
                continue
            if arr[yy][xx] == '.' and ch[yy][xx] == 0:
                gsdc.append((yy, xx))
                ch[yy][xx] = 1
            elif arr[yy][xx] == 'D':
                print(cnt)
                exit()

print("KAKTUS")
# import sys
# import heapq
# from collections import deque

# row, col = map(int, input().split())
# count = 0
# graph = []
# for _ in range(row):
#     graph.append(list(input()))
# visited = [[False]*col for _ in range(row)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def water():
#     over_flow = []
#     for i in range(row):
#         for j in range(col):
#             if graph[i][j] == "*" and not visited[i][j]:
#                 over_flow.append((i,j))
#                 visited[i][j] = True
#     for x, y in over_flow:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx < row and 0 <= ny < col and not visited[nx][ny]:
#                 if(graph[nx][ny] == "."):
#                     graph[nx][ny] = "*"

# def bfs(row2, col2):
#     # heap = []
   
    # visited[row2][col2] = True
    # heapq.heappush(heap, (row2, col2))
    # while heap:
    #     x, y = heapq.heappop(heap)
    #     for i in range(4):
    #         new_x = x + dx[i]
    #         new_y = y + dy[i]
    #         if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
    #             heapq.heappush(heap, (new_x, new_y))
    #             visited[new_x][new_y] = True

# def move(row1, col1):
#     heap1 = []
#     global count
#     visited[row1][col1] = True
#     heapq.heappush(heap1, (row1, col1))
#     while heap1:
#         count += 1
#         x, y = heapq.heappop(heap1)
#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
#                 if graph[new_x][new_y] == "D":
#                     return count
#                 elif graph[new_x][new_y] == ".":
#                     heapq.heappush(heap1, (new_x, new_y))
                
#     return "KAKTUS"
# starting_x,starting_y = 0, 0
# for x in range(row):
#     for y in range(col):
#         if graph[x][y] == "S":
#             starting_x,starting_y = x,y
#             graph[x][y] = "."        

# print(move(starting_x,starting_y))