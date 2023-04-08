import math
up,down, goal = input().split()
up = int(up)
down = int(down)
goal = int(goal)
D = 0
count = 0
x = (up + down)/2
count = goal / x
print(count)





# for i in range(D, goal -1):
#     if (D <= goal):
#         count += 1 
#         D += up 
#     if (D <= goal):
#         D = D - down 