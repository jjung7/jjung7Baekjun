# list = []
# for _ in range (9):
#     list.append(int(input()))
# list.sort()
# sum = 0
# for j in range(9):
#     sum += list[j]
# sum = sum - 100
# for k in range(0,8):
#     for p in range(k+1, 9):
#         if[list[k]+list[p] == sum]:
#             list.remove(list[p])
#             list.remove(list[k])
# print(list)    
heights = []
for _ in range(9):
    heights.append(int(input()))

total_height = sum(heights)
target_sum = total_height - 100

for i in range(9):
    for j in range(i + 1, 9):
        if heights[i] + heights[j] == target_sum:
            del heights[j]
            del heights[i]
            break
    if len(heights) == 7:
        break

heights.sort()
for _ in range(0,7):
    print(heights[_])