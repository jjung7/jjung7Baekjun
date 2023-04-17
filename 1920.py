# import sys
# input = sys.stdin.readline
# T = int(input())
# listA = list(map(int,input().split()))
# X = int(input())
# listB = list(map(int,input().split()))
# b = True
# for i in range(T):
#     for j in range(X):
#         if(listB[i] == listA[j]):
#             b = True
#             break
#         else:
#             b = False
#     if (b == True):
#         print(1)
#     else:
#         print(0)

import sys                  
input = sys.stdin.readline
def bin_search(arr,key,start,end):
    if start > end:
        return None
    pc = (start + end)//2
    if arr[pc] == key:
        return key
    elif arr[pc] < key:
        return bin_search(arr,key,pc+1,end)
    else:
        return bin_search(arr,key,start,pc-1)

T = int(input())
listA = list(map(int,input().split()))            
Q = int(input())
listA.sort()
listB = list(map(int,input().split()))
for i in range(Q):
    if bin_search(listA, listB[i],0, T-1):
        print(1)
    else:
        print(0)

