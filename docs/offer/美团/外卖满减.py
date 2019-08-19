n,x = list(map(int, input().split()))
res = list(map(int, input().split()))
dp = [100000]*(x+1)
for i in range(n):
    for j in range(x,-1,-1):
        if j>res[i]:
            dp[j] = min(dp[j], dp[j-res[i]]+res[i])
        else:
            dp[j] = min(dp[j], res[i])
print(dp[-1])