import sys


def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N): 
        if not visited[i] and a[now][i]:
            visited[i] = True
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = False


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(ans)
# import sys
# from itertools import permutations

# N = int(sys.stdin.readline())
# W = []
# for i in range(N):
#     W.append(list(map(int, sys.stdin.readline().split())))

# cities = [i for i in range(N)]  # List of cities from 0 to N-1
# min_cost = float('inf')  # Set minimum cost to positive infinity

# # Iterate over all permutations of cities, i.e., all possible travel paths
# for path in permutations(cities):
#     cost = 0  # Initialize the cost for the current path
#     for i in range(N - 1):
#         # Add the cost of traveling from the current city to the next city
#         cost += W[path[i]][path[i + 1]]
#     # Add the cost of traveling from the last city to the first city
#     cost += W[path[N - 1]][path[0]]
#     # Update the minimum cost if the cost of the current path is lower
#     min_cost = min(min_cost, cost)

# print(min_cost)

