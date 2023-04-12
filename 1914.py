n = int(input())
def Hanoi(n,start, end):
    if n > 1: # n = 3 start 1 end 3
        Hanoi(n-1, start,6-start-end)
    print(start,end)
    if n > 1:
        Hanoi(n-1,6-start-end, end)
    
Hanoi(n,1,3)  