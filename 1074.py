N = int(input())
board = [[0]*(2**N) for _ in range(2**N)]

r = int(input())
c = int(input())
board[c][r] = 1
print(board) 

count = 0
def move(x,y): #0 0, 0 1, 1 0, 1 1,  0 2, 0 3, 1 2, 1 3,2 0, 2 1
    global count
    if (board[x][y] == 1):
        return count
    board[x][y] = 1 # 현재 위치를 방문한 것으로 표시
    if(x == 0 or x % 2 == 0):
        if(y == 0):
            count += 1
            return move(x + 1, 0)
        elif(y == len(board)-1 or y % 2 == 1): 
            count+=1
            return move(x+1,y-1)
        elif(y % 2 == 0):
            count+=1
            return move(x,y+1)
    elif(x == 1 or x % 2 == 1):
        if(y == 0):
            count += 1
            return move(x + 1, 0)
        elif(y == len(board)-1 or y % 2 == 1): 
            count+=1
            return move(x-1,y+1)
        elif(y % 2 == 0):
            count+=1
            return move(x,y+1)
    
    return count # count 변수를 리턴해줌
   
move(0,0)
print(count)

