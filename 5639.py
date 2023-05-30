import sys
sys.setrecursionlimit(10**9) #increase recursion depth to avoide maximum recursion depth in case of a large input
nums = []
while True:                            
    try:
        nums.append(int(sys.stdin.readline())) #50,30,24,5,28,45,98,52,60
    except:
        break
        
def postorder(s, e): #0,8
    if s > e:
        return
    mid = e + 1    #mid = 9,6
                   # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1): #1, 9| 2,6
        if nums[s] < nums[i]: #50, 30, 24,45,30,60
            mid = i #mid = 5
            break

    postorder(s+1, mid-1)   #1,5 ->            # 왼쪽 확인
    postorder(mid, e)       #5,8 ->           # 오른쪽 확인
    print(nums[s])          #50                

postorder(0, len(nums)-1)    