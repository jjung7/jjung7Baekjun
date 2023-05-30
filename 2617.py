import sys
input = sys.stdin.readline

def dfs(start,arr):
    global visited, check
    visited[start] = True
    for i in arr[start]:
        if(visited[i] == False):
            check += 1
            dfs(i, arr)

N,M = map(int,input().split())
list1 = []
heavier = [[] * (N+1) for _ in range(N+1)]
minimum = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    # list1.append(list(map(int,input().split())))
    x,y = map(int,input().split())
    heavier[x].append(y)
    minimum[y].append(x)
ans = (N+1) //2
count = 0
for i in range(1,N+1):
    visited = [False] * (N+1)
    check = 0
    dfs(i, heavier)
    if (check >= ans):
        count += 1
    check = 0
    dfs(i, minimum)
    if (check >= ans):
        count +=1
print(count)    
    #     dfs(i)

    # if minimum[i]:
    #     dfs(i)
    # if(len(heavier[i]) >= ans):
    #     count+=1
    # if(len(minimum[i]) >= ans):
    #     count+=1


