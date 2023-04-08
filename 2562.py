max = 0
max_num = 0
for i in range(0,9):
    x = input()
    x = int(x)
    if(max < x):
        max = x
        max_num = i + 1
print(max)
print(max_num)
