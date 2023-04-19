# import heapq
# import sys
# input = sys.stdin.readline
# n = int(input())
# list1= []
# answer = []
# for i in range(n):
#     list1.append(list(map(int,input().split())))
# list1.sort(key=lambda x: x[0])
# target = int(input())
# start = list1[0][0] 
# end = start + target
# for i in range(n):
#     if(   )
import sys
import heapq

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)
print(road_info)
# d = int(sys.stdin.readline())
# roads = []
# for road in road_info:
#     house, office = road
#     if abs(house - office) <= d:
#         road = sorted(road)
#         roads.append(road)
# roads.sort(key=lambda x:x[1])

# answer = 0
# heap = []
# for road in roads:
#     if not heap:
#         heapq.heappush(heap, road)
#     else:
#         while heap[0][0] < road[1] - d:
#             heapq.heappop(heap)
#             if not heap:
#                 break
#         heapq.heappush(heap, road)
#     answer = max(answer, len(heap))

# print(answer)