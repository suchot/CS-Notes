# 题目描述：
# 有一个非常经典的概率问题，是一个袋子里面有若干个红球和若干个蓝球，两个人轮流取出一个球，谁先取到红球谁就赢了，当人的先后顺序和球的数量确定时，双方的胜率都可以由计算得到，这个问题显然是很简单的。
#
## 现在有一个进阶版的问题，同样是一个袋子里面有n个红球和m个蓝球，共有A，B，C三人参与游戏，三人按照A，B，C的顺序轮流操作，
# 在每一##回合中，
# A，B，C都会随机从袋子里面拿走一个球，然而真正分出胜负的只有A，B两个人，没错，C就是来捣乱的，他除了可以使得袋子里面减##少一#个
# 球，没有其他任何意义，而A，B谁 先拿到红球就可以获得胜利，但是由于C的存在，两人可能都拿不到红球，此时B获得胜利。
#
# 输入
# 输入仅包含两个整数n和m,表示红球和蓝球的数量，中间用空格隔开。(0<=n,m<=1000)

# 输出
# 请你输出A获胜的概率，结果保留5位小数。（四舍五入）


# 样例输入
# 1 1
# 样例输出
# 0.50000

# 提示
# 输入样例2
# 3 4
# 输出样例2
# 0.62857
# class Solution():
#     def redblue(self,n,m):
#         dp[i][j] = dp[i][j]
        


# if __name__ == "__main__":
#     S = Solution()
#     n,m = input()
#     res = S.redblue(n.m)
#     print(%res)



rb = input().strip().split()
r = int(rb[0])+1
b = int(rb[1])+1

rr = max(r, 2)
bb = max(b, 3)
dp = [bb*[0] for i in range(rr)]

for i in range(r):
    dp[i][1] = i / (i+1)
dp[1][2] = 1/3
for i in range(2, r):
    dp[i][2] = i/(2+i) + (2/((2+i) * (1+i)))

for i in range(r):
    for j in range(3, b):
        dp[i][j] = i / (i+j) + (j/(i+j)) * ((j-1)/(i+j-1)) * ((i/(i+j-2)) * dp[i-1][j-2] + ((j-2)/(i+j-2))*dp[i][j-3])

print("%.5f" % dp[r-1][b-1])