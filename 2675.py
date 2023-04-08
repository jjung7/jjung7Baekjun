T = int(input())
result = []

for i in range(0,T):
    temp = ""
    list = []
    a, b = input().split()
    a = int(a)
    list = b
    for k in range(0, len(list)):
        result = list[k]
        temp += list[k] * a
    print(temp)