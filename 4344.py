T = input()
T = int(T)
for i in range(0,T):
    a = []
    a = input().split()
    count = 0
    sum = 0
    avg = 0
    avg_above = 0
    real_avg = 0
    for j in range(1, len(a)):
        a[j] = int(a[j])
        sum = sum + a[j]
        count = count+ 1
        avg = sum/count
        avg = int(avg)
    for k in range(1,len(a)):
        if (a[k] > avg):
            avg_above += 1        
    real_avg = (avg_above/(len(a)-1)*100)
    print(f'{real_avg:.3f}%')