

n = int(input())
weight = []
value = []
for i in range(n):
    w1, v1, w2, v2 = map(int, input().split())
    weight.append([w1, w2])
    value.append([v1, v2])
 
dp = [0]*121
for i in range(n):
    for j in range(120,0, -1):
        if j >= weight[i][0] or j >= weight[i][1]:
            if j >= weight[i][0] and j >= weight[i][1]:
                dp[j] = max(dp[j-weight[i][0]]+value[i][0], dp[j-weight[i][1]]+value[i][1], dp[j])
            elif j >= weight[i][0]:
                dp[j] = max(dp[j-weight[i][0]]+value[i][0], dp[j])
            else:
                dp[j] = max(dp[j-weight[i][1]]+value[i][1], dp[j])
print(dp[120])