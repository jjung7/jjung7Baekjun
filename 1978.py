# T = int(input())
# result = [2,3,5,7,11,13,17,19,23,27,29,31]
# list = []
# list = input().split()
# count = 0
# for i in range(0,T):
#     list[i] = int(list[i])
# list.sort()
# for j in range(0,T):
#     for k in range(0,len(result)):
#         if(list[j] == result[k]):
#             count+=1
                
# print(count)

T = int(input())
list = []
result = []
list = input().split()
count = 0
for i in range(0,T): #[10,9,8,7]
    list[i] = int(list[i])
    for j in range(2, list[i]+1): #10
        if(list[i] == 2):
            count += 1
        elif (list[i] == j + 1):
            count +=1
        elif (list[i] % j == 0):
            break
          
print(count)

# su = int(input())
# a = list(map(int, input().split()))

# a = a[0:su]
# count = 0
# cnt = 0
# for i in a : #[10,9,8,7]
#     for j in range(1, i + 1):
#         if i % j == 0:
#             cnt += 1

#     if cnt == 2:
#         count += 1
#     cnt = 0

# print(count)