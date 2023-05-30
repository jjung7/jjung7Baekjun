import sys,heapq
from collections import deque

input = sys.stdin.readline

n, value = map(int,input().split())
coins = list(set(int(input()) for _ in range(n)))
# list1 = []
# num, target = map(int,input().split())
# for _ in range(num):
#     list1.append(list(map(int,input().split())))

# def bfs(ct , cur):
#     count = 0 
check = [0 for _ in range(value + 1)]
def bfs(coins,value):
    queue = deque()
    for coin in coins:
        if coin < value:
            queue.append([coin,1])
            check[coin] = 1
    
    while queue:
        cum, cnt = queue.popleft()
        if value == cum:
            print(cnt)
            break
        for coin in coins:
            cum1 = cum+coin
            cnt1 = cnt + 1
            if cum1 > value:
                continue
            elif cum1 <= value and check[cum1] == 0:
                check[cum1] = 1
                queue.append([cum1,cnt1])
    if cum != value:
        print('-1')
bfs(coins,value)