import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    num = int(input())
    heapq.heappush(card, num)
print(card)
# result = 0
# while len(card)>1:
#     n1 = heapq.heappop(card)
#     n2 = heapq.heappop(card)
#     result += n1 + n2
#     heapq.heappush(card, n1+n2)

# print(result)

# import sys, heapq
# input = sys.stdin.readline
# n = int(input())
# min1,temp1 = [],[]
# sum1 = 0
# for i in range(n):
#     x = int(input())
#     if (len(min1) == len(temp1)):

#         heapq.heappush(min1, -x)
#     else:
#         heapq.heappush(temp1,x)
#     if temp1 and min1:
#         sum1 += heapq.heappush(temp1, -heapq.heappop(min1) + heapq.heappop(temp1))
# print(sum1)  