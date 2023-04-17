import sys
input = sys.stdin.readline
T = int(input()) #5
list1 = list(map(int,input().split())) # -2,4,-99,-1,98
list1.sort() # -99 -2 -1 4 8
ans = float("inf")
pl = 0
pr = T-1 #4
left =0
right =0

while (pl < pr):
    sum = list1[pl] + list1[pr]
    if(abs(sum) < ans):
        ans = abs(sum)
        left = pl
        right = pr
        if(ans == 0):
            break
    if sum < 0:
        pl +=1
    else:
        pr -=1
print(list1[left],list1[right])
