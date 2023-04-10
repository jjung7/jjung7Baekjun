import math
up,down, goal = input().split()
up = int(up) #4
down = int(down) #3
goal = int(goal) #20
D = 0
goal = goal - down
x = up - down
D = goal/x
print(math.ceil(D))





# for i in range(D, goal -1):
#     if (D <= goal):
#         count += 1 
#         D += up 
#     if (D <= goal):
#         D = D - down 