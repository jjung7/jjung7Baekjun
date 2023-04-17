import sys


def dfs(start, now, value, cnt):
    global ans
    if cnt == N: #마지막에서 다시 처음으로 돌아가야함
        if a[now][start]: #현재도시에서 처음 도시로
            value += a[now][start] #값을 더함
            if ans > value: #비교
                ans = value #미니멈이 순회비용보다 크면 순회비용이 미니멈이 됨
        return #리턴

    if value > ans: #방문을 다 하기전에 값이 미니멈보다 크면 리턴
        return

    for i in range(N):  
        if not visited[i]   and a[now][i]: #1-4, 이미 도시 0은 방문처리완료 현재 도시에서부터 i 도시
            visited[i] = True #방문처리 완료
            dfs(start, i, value + a[now][i], cnt + 1) #재귀를 이용해서 시작도시, 다음도시, 벨류라는 변수에 저장, 방문도시 체크
            visited[i] = False #도시 리셋


N = int(input()) #input 값을 받음
a = [list(map(int, input().split()))for _ in range(N)] #이차원적 리스트를 생성 [[0,1,1,2],[1,0,2,2]] 이런 느낌
ans = sys.maxsize #변수 미니멈을 최대값으로 생성
visited = [False] * N #도시의 수만큼 False라는 인덱스 생성
for i in range(N): #처음시작 도시 설정
    visited[i] = True #처음시작 도시 방문한 도시로 설정
    dfs(i, i, 0, 1) #시작 도시,현재도시,비용, 순회횟수
    visited[i] = False #전부 다 방문 안할걸로 처리
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

