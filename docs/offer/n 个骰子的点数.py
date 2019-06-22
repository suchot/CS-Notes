class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        # countMap = {}
        # self.dfs(n, countMap, 0, 1)
        # ans = []
        # for key in countMap.keys():
        #     ans.append((key, countMap[key]))
        # return ans
        if n <= 0:
            return []
        return self.solution1(n)


    def dfs(self, n, res, val, pro):
        if n == 0:
            if val not in res:
                res[val] = 0
            res[val] += pro
            return
        for i in range(1,7):
            self.dfs(n-1, res, val + i, pro * 1/6)
    
    def solution1(self, n):

        f = [[0 for j in range(6 * n + 1)] for i in range(n + 1)]

        for i in range(1, 7):
            f[1][i] = 1.0 / 6.0

        for i in range(2, n + 1):
            for j in range(i, 6 * n + 1):
                for k in range(1, 7):
                    if j > k:
                        f[i][j] += f[i - 1][j - k]
                f[i][j] /= 6.0
        ans = []
        for i in range(n, 6 * n + 1):
            ans.append((i, f[n][i]))
        return ans
