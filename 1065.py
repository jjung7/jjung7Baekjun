T = int(input())
if (T < 100):
    print(T)
elif ( 1000 == T):
    print(144)
else:
    n = 99
    for i in range(100, T+1):
        a = i // 100
        b = (i-a*100)//10
        c = i-a*100-b*10
        if(a == b and b == c):
            n += 1
        elif(a - b == b-c):
            n += 1

    print(n)