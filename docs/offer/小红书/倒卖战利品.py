# 题目描述：
# 在游戏中，击败魔物后，薯队长获得了N件宝物，接下来得把这些宝物卖给宝物回收员来赚点小钱。这个回收员有个坏毛病，每次卖给他一件宝物后，之后他就看不上比这件宝物差的宝物了。在这个世界中，衡量宝物的好坏有两个维度，稀有度X和实用度H，回收员在回收一个宝物A后，下一个宝物的稀有度和实用度都不能低于宝物A。那么薯队长如何制定售卖顺序，才能卖给回收员宝物总个数最多。

# 输入
# 第一行一个正整数N。

# 接下来N行。每行两个整数分别表示X 和 H

# X1 H1

# X2 H2

# …

# XN HN

# 输入限制：

# 对于70%的数据：

# 0 < N < 10^4

# 0 < Xi < 10^6

# 0 < Hi < 10^6

# 对于100%的数据：

# 0 < N < 10^6

# 0 < Xi < 10^6

# 0 < Hi < 10^6

# 输出
# 一个整数，表示最多可以卖出的宝物数


# 样例输入
# 4
# 3 2
# 1 1
# 1 3
# 2 2
# 样例输出
# 3
n = int(input())
arr = []
dict_s = dict()
for i in range(n):
    
    arr.append(list(map(int, input().split())))
def numsort(arr, n):
    arrs = sorted(arr, key = lambda x:(x[0],x[1]))
    res = arrs[0][0]+arr[0][1]
    lastx = arrs[0][0]
    num =  1
    for i in range(n):
        if i > lastx:
            temp = arrs[i][0]+arrs[i][1]
            if temp > res:
                lastx = arrs[i][0]
                res += temp
                num+=1
    return num
print(numsort(arr,n))
