# import sys

# input = sys.stdin.readline

# n, m, r = map(int, input().split())

# animals = []
# for i in range(n):
#     x, y = map(int, input().split())
#     animals.append((x, y))
# animals.sort(key=lambda x: x[1])

# stands = list(map(int, input().split()))
# stands.sort()

# catch = set()
# for x, y in animals:
#     left, right = 0, len(stands) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if stands[mid] < x:
#             left = mid + 1
#         elif stands[mid] > x:
#             right = mid - 1
#         else:
#             if y <= r:
#                 catch.add(mid)
#             break

# print(len(catch))

import sys
input = sys.stdin.readline
sh,an,r, = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
catch = 0
for i in range(an):
    pl = 0
    pr = len(num)-1
    x,y = map(int,input().split())
    while pl <= pr:
        mid = (pr+pl)//2
        if(num[mid] < x):   
            pl = mid + 1
        else:
            pr = mid - 1
        if abs(num[mid] - x) + y <= r: #|xi-aj| + bj
            catch += 1
            break
print(catch)

# 1 4 6 9
# 2