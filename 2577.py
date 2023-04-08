a = int(input())
b = int(input())
c = int(input())
result = []
sum = (a*b*c) #321 ['3','2','1']
list = [0,0,0,0,0,0,0,0,0,0]
result = [int(i) for i in str(sum)]

for k in range(0,len(result)): #0-3
    for j in range(0,10):
        if(result[k] == j):
            list[j] += + 1
            break
for x in range(0,10):
    print(list[x])
