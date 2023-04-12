
import sys
sys.setrecursionlimit(10000) # 재귀 함수 깊이 한계 설정

def dfs(x, y, h):
    # 현재 위치 (x, y)가 범위를 벗어난 경우
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 현재 위치 (x, y)가 물에 잠긴 경우
    if board[x][y] <= h:
        return False
    # 이미 방문한 경우
    if visited[x][y]:
        return False

    # 현재 위치 (x, y)를 방문 처리
    visited[x][y] = True

    # 상하좌우로 DFS 탐색
    dfs(x-1, y, h)
    dfs(x+1, y, h)
    dfs(x, y-1, h)
    dfs(x, y+1, h)

    # DFS 탐색이 끝난 후, 안전한 영역의 크기를 반환
    return True

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

max_height = max(map(max, board)) # 지형의 최대 높이
max_count = 0 # 가장 큰 안전한 영역의 크기

# 높이가 0부터 최대 높이까지 모든 경우를 탐색
for h in range(max_height+1):
    visited = [[False]*n for _ in range(n)]
    count = 0 # 현재 높이에서의 안전한 영역의 개수
    for i in range(n):
        for j in range(n):
            if dfs(i, j, h):
                count += 1
    max_count = max(max_count, count)

print(max_count)
# # from itertools import permutations
# T = int(input())
# board = []
# board1 = [[False]*T for _ in range(T)]
# max_count = 0
# print(board1)
# start = 100
# for _ in range(T):
#     board.append(list(map(int, input().split())))

# def board_check(start, T):
#     global board1
#     for j in range(T):
#         for u in range(T):
#             if(j == T-1 and u == T-1):
#                 if(board[j][u] > start):
#                     board1[j][u] = True
#                     return board1
#                 else:
#                     return board1
#             elif(board[j][u] > start):
#                 board1[j][u] = True

# def checking(start , T):
#     count = 0
#     if start == 0:
#         return max_count
#     else:
#         board_check(start, T)
#         start - 1
#         for row in range(T):
#             for col in range(T):
#                 if(board1[row][col] == True):
#                     count += 1
#     max(count, max_count)
# checking(3,T)
# print(max_count)    

    

# print(board1)
# # #x = 100            
