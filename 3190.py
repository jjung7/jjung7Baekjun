import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n = int(input())
board = [[0]*n for _ in range(n)]
num = int(input())
count = 0
for _ in range(num):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
second = int(input())

# 초기 상태
head = (0, 0)  # 머리 위치
tail = (0, 0)  # 꼬리 위치
direction = 0  # 이동 방향 (0: right, 1: down, 2: left, 3: up)
queue.append(head)

while True:
    # 이동할 위치 계산
    dx = [0, 1, 0, -1]  # x 이동량
    dy = [1, 0, -1, 0]  # y 이동량
    nx = head[0] + dx[direction]
    ny = head[1] + dy[direction]

    # 벽 또는 뱀의 몸과 부딪히는지 체크
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        print(count+1)
        break

    # 머리 이동
    head = (nx, ny)
    queue.append(head)

    # 사과가 있는 경우
    if board[nx][ny] == 1:
        board[nx][ny] = 2

    # 사과가 없는 경우
    else:
        tail = queue.popleft()
        board[tail[0]][tail[1]] = 0

    # 방향 전환
    if second > 0 and count+1 == int(second):
        second_list = input().split()
        if second_list[1] == "D":
            direction = (direction+1) % 4
        else:
            direction = (direction-1) % 4
        if len(second_list) > 0:
            second = int(second_list[0])
    count += 1
# import sys
# from collections import deque
# input = sys.stdin.readline
# queue = deque()
# n = int(input())
# board = [[0]*n for _ in range(n)]
# num = int(input())
# count = 0
# for _ in range(num):
#     x, y = map(int, input().split())
#     board[x-1][y-1] = 1
# second = int(input())
# while True:

#     for _ in range(second):
#         time, turn = input().split()
#         time = int(time)
#         if(count == time):
#             if(turn == "D"):
#                 #turn right
#             elif(turn == "L"):
#                 #turn left
                
