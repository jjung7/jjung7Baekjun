N,X= input().split()
list = []
list = input().split()
list1 = []
N = int(N)
X = int(X)
for i in range(0,N):
    list[i] = int(list[i])
    if(list[i] < X):
        list1.append(list[i])
for j in range(0,len(list1)):
    print(list1[j], end= " ")



