class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        timeof3, restofnum = n//3, n%3
        if restofnum == 1:
            timeof3 -= 1
        timeof2 = (n-(timeof3*3))//2
        return (3**timeof3) * (2**timeof2)

class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(dp[j],j) * max((i-j), dp[i-j]))
        return dp[n]
            
