s = input()
def maxLength(s):
    if len(s) == 0:
        return 0
    dp = [0] * len(s)
    res = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            pre = i - dp[i - 1] - 1
            if pre >= 0 and s[pre] == '(':
                dp[i] = dp[i - 1] + 2
                if pre > 0:
                    dp[i] += dp[pre - 1]
        res = max(res,dp[i])
    return res
 

print(maxLength(s))