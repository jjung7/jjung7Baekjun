import sys
input = sys.stdin.readline

house, wifi = map(int, input().split())
houselist = []
for i in range(house):
    houselist.append(int(input()))
houselist.sort()
#1,2,4,8,9
count = 1
left = 1  # 가능한 최소 거리
right = houselist[-1] - houselist[0]  # 가능한 최대 거리 #8

while left <= right:
    mid = (left + right) // 2 #4
    installed = houselist[0]  # 첫 번째 집에는 무조건 공유기 설치
    count = 1
    
    for i in range(1,   house):
        if houselist[i] - installed >= mid: #4 -1 >= 4
            installed = houselist[i]
            count += 1
        
        if count == wifi:  # 공유기를 다 설치한 경우
            break
    
    if count == wifi:  # 공유기를 다 설치한 경우
        left = mid + 1  # 최소 거리 증가
        answer = mid   # 현재의 최대 거리 저장
    else:
        right = mid - 1  # 최대 거리 감소

print(answer)

# import sys
# input = sys.stdin.readline
# house, wifi = map(int,input().split())
# houselist = []
# for i in range(house):
#     houselist.append(int(input()))
# print(houselist)
# houselist.sort()
# count = 1
# min = 0
# pl = 0
# pr = len(houselist)-1
# while pl <= pr:
#     pc = (pl+pr)//2
#     installed = houselist[0]
#     count = 1
#     for i in range(1,house):
#     if houselist[i] - installed >= pc:
#     installed = houselist[i]
#     count += 1
        
#     elif(pl < pr):
#         break

    
    
    


