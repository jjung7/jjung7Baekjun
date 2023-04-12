a, b = map(int,input().split())
list1 = []
list1 = list(map(int,input().split()))
for i in range(a):
    if(list1[i] < b):
        print(list1[i], end=" ")
                    
    