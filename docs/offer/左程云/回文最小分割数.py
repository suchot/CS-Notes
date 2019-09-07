s = input()
def mindiv(s):
    if not s:
        return 0
    lens = len(s)
    dp = [0 for i in range(lens+1)]
    dp[-1] = -1
    p  = [[False for i in range(lens)] for j in range(lens)]
    for i in range(lens-1, -1 ,-1):
        dp[i] = float('inf')
        for j in range(i, lens):
            if s[i]==s[j] and (j-i<=1 or p[i+1][j-1]):
                p[i][j]=True
                dp[i] = min(dp[i], dp[j+1]+1)
    return dp[0]
print(mindiv(s))