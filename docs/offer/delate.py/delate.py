class Solution:
    def __init__(self):
        self.memo = {'':1, '1':1, '0':1} # 记忆化
    def sortcount(self,S):
        """
        :type S: str
        :rtype: int
        """
        # 分治 + 动态规划
        # time complexity: O(n^2)
        n = len(S)
        if S in self.memo:
            return self.memo[S]
        CONST = 10**9 + 7
        ans = 0
        if S[0] == "1": # 最大数出现在最左端
            ans += self.sortcount(S[1:])
        if S[-1] == "0": # 最大数出现在最右端
            ans += self.sortcount(S[:-1])
        comb = 1 # 组合数
        for i in range(n-1):
            comb = comb*(n-i)//(i+1)
            if S[i:i+2] == "ID": # 最大数出现在中间
                temp1, temp2 = S[:i], S[i+2:]
                ans += self.sortcount(temp1)*self.sortcount(temp2)*comb
                ans %= CONST
        self.memo[S] = ans
        return ans
if __name__ == "__main__":
    S = Solution()
    n = int(input())
    arr = ''.join((map(str, input().split())))
    print(S.sortcount(arr))