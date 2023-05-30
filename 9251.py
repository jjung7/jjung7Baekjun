import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()
dp = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            dp[i+1][j+1] = dp[i][j] +1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[len(string1)][len(string2)])

# import sys
# read = sys.stdin.readline

# word1, word2 = read().strip(), read().strip()
# l1, l2 = len(word1), len(word2)
# cache = [0] * l2

# for i in range1):
#     cnt = 0(l
#     for j in range(l2):
#         if cnt < cache[j]:
#             cnt = cache[j]
#         elif word1[i] == word2[j]:
#             cache[j] = cnt + 1
# print(max(cache)) n