import sys
read = int(sys.stdin.readline())
list = [0] * 10001
for i in range(0,read):
    num = int(sys.stdin.readline()) 
    list[num] = list[num] + 1  
for k in range(0,10001):
    if list[k] != 0:
        for _ in range(list[k]):
            print(k)