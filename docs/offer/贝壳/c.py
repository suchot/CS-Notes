# 题目描述：
# 桌面上有n颗糖果，第i颗糖果的美味度为2wi。彼得每次能吃掉任意多颗糖果，但是他每次吃掉糖果的美味度的和必须为2k(k为非负整数)，问彼得最少需要多少次才能吃完桌面上所有的糖果。

# 输入
# 第一行一个整数n，表示桌面上的糖果数。(1 <= n <= 10^6) 第二行n个整数，中间用空格隔开，表示w1，w2，...，wn。(0 <= wi <= 10^6）

                               

# 输出
# 一个整数，表示吃掉桌面上所有糖果需要的最少次数。


# 样例输入
# 5
# 1 1 2 3 3
# 样例输出
# 2

class Solution():
    def eatsuger2(self, w):
        n = sum(map(lambda x: 2**x, w))
        count = 0
        if n < 0:
            n &= (1<<32)-1
        while n > 0:
            n &=(n-1)
            count += 1
        return count
    def eatsuger(self, w):
        dp = [0]*(10**6+1)
        for index in w:
            if dp[index]==0:
                dp[index]+=1
            elif dp[index]==1:
                dp[index]=0
                while dp[index+1]==1:
                    dp[index]=0
                    index+=1
                dp[index]=1
                

        res = sum(dp)
        return res
if __name__ == "__main__":
    
    n = input()
    w = list(map(int, input().split()))
    S = Solution()
    print(S.eatsuger(w))