# 题目描述：
# 给定一个长度为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？

# 输入
# 第一行包含一个整数N，1<N≤1000。

# 第二行包含N-1个空格隔开的整数A1到AN-1，0≤Ai≤1

# 输出
# 输出符合要求的排列个数对109+7取模后的结果。


# 样例输入
# 4
# 1 1 0
# 样例输出
# 3
from itertools import permutations 
class Solution():
    def sortcount1(self, n,arr):
        se  = list(permutations([i for i in range(1,n+1)]))
        count = 0
        for p in se:
            i = 0
            while i < n-1:
                if arr[i] == 0 and p[i]<p[i+1]:
                    i += 1
                    continue
                elif arr[i] == 1 and p[i]>p[i+1]:
                    i+=1
                    continue
                else:
                    break
            if i==n-1:
                count += 1 
        return count
    def sortcount(self, n,arr):
        Mod = 10**9 +7
        n = len(arr)
        def dp(i,j):
            if i==0:
                return 1
            elif arr[i-1] ==0:
                return sum(dp(i-1,k) for k in range(j,i))% Mod
            else:
                return sum(dp(i-1,k) for k in range(j)) % Mod
        return sum(dp(n,j) for j in  range(n+1)) % Mod
if __name__ == "__main__":
    S = Solution()
    n = int(input())
    arr = list(map(int, input().split()))
    print(S.sortcount(n,arr))