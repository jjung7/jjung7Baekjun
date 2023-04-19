import sys
input = sys.stdin.readline
T = int(input())
list1 = []
for _ in range(T):
    list1.append(list(map(int,input().split())))
print(list1)