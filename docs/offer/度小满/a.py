# 题目描述：
# A和B正在博弈，他们的博弈道具是一张初始为 n*m纸片。

# 每次操作，都可以把一张x*y的纸片剪成x*t和x*(y-t)(t≥1,y-t≥1)的两张纸片，也可以切成t*y和(x-t)*y(t≥1,x-t≥1)的两张纸片，（x，y均为正整数）；纸片一分为二后，可以选取任意一个部分进行后续操作，最终先切出1*1纸片的人胜利

# 现在你是A，你想知道在自己先手的情况下，俩人都足够聪明的情况下谁会赢？

# 如果你会赢，输出WIN，否则输出LOSE 

# 输入
# 输入包含多组数据，数据组数不超过40000，

# 每组数据两个整数n,m，代表一开始的纸片n*m 

# 2≤n≤200  ,  2≤m≤200 


# 输出
# 对于每组数据，如果你有必胜策略，输出 WIN

# 否则输出 LOSE


# 样例输入
4 2
3 2
2 2
# 样例输出
# WIN
# LOSE
# LOSE

while x,y = map(int, input().split()):
    def wins(x,y):
        if x^y != 0 :
            return True
        else:
            return False
    if wins(x,y):
        print('WIN')
    else:
        print('LOSE')

