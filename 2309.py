list = []
for i in range (9):
    list.append(int(input()))
list.sort()
sum = 0
for j in range(9):
    sum += list[j]
sum = sum - 100
    
print(list)
