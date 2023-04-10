import sys
read = sys.stdin.readline()
read = int(read)
list = []
result = []
for i in range(0,read):
    list.append(sys.stdin.readline())
    list[i] = int(list[i])
list.sort()
for k in range(0,read):
    print(list[k])
    # list[i] = int(list[i])
# list.sort()
# print(list)


# print(type(read))
# list = [0] * read
# ABC = []
# save = 0
# for k in range(0,read):
#     ABC = sys.stdin.readline()
#     ABC[k] = int(ABC[k])
# def sorting(read):
#     for i in range(0,read):
#         for j in range(0,len(list)):
#             if (list[j] == 0):
#                 list[j] = ABC[i]
#                 break
#             elif (list[j] > ABC[i]):
#                 read = list[j]
#                 list[j] = ABC[i]
#                 return sorting(read)
#     print(list[i]) 
            

