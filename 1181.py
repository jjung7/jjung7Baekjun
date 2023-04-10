import sys

T = int(sys.stdin.readline())
words = set()
for i in range(T):
    word = sys.stdin.readline().strip()
    words.add(word)

word_list = [(len(word), word) for word in words]

word_list.sort()
for length, word in word_list:
    print(word)
# for p in range(len(list2)-1):
#     if(list2[p] == list2[p+1]):
#         del(list2[p])
# print(list2)


    # for j in range(len(list)):

    # print(list1)
    # print(list1[i])
    # list[num] = list[num + 1]
# for j in range(0, 122):
#     if(list[j] != 0):
#         for k in range(list[j]):
#             print(j)
