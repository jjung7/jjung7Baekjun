import sys
input = sys.stdin.readline
A,B,C = map(int,input().split()) #10 11 12
def pows(n, p):        #10 11
    if p == 0:          
        return 1
    else:
        x = pows(n, p // 2)  #10, 5 10, 2 10,1 10,0  
        x *= x                
        x %= C #100%12  x=4               
        if p % 2:             
            return (x * n) % C  
        else:
            return x

print(pows(A, B))      