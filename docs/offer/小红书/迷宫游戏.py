# 题目描述：
# 薯队长最近在玩一个迷宫探索类游戏，迷宫是一个N*N的矩阵形状，其中会有一些障碍物禁止通过。这个迷宫还有一个特殊的设计，它的左右边界以及上下边界是连通的，比如在(2,n)的位置继续往右走一格可以到(2,1)， 在(1,2)的位置继续往上走一格可以到(n,2)。请问薯队长从起点位置S，最少走多少格才能到达迷宫的出口位置E。

# 输入
# 第一行正整数 N。 接下来 N 行 字符串。 

# ’.’表示可以通过，’#’表示障碍物, ’S’表示起点（有且仅有一个），’E’表示出口（有且仅有一个）。

# 对于50%的数据

# 0 < N < 10

# 对于100%的数据

# 0 < N < 10^3

# 输出
# 输出一个整数。表示从S到E最短路径的长度, 无法到达则输出 -1


# 样例输入
# 5
# .#…
# ..#S.
# .E###
# …..
# …..
# 样例输出
# 4

# 提示
# 向右来到(2,5)
# 向右来到(2,1)
# 向下来到(3,1)
# 向右来到(3,2)
n = int(input())
matrix = []
for i in range(n):
    matrix.append()
    matrix.append(list(input()))
N = 3*n
def migong(n, matrix):
    
    bigmatrix = [['#' for i in range(3*n)] for j in range(3*n)]
    for i in range(3*n):
        for j in range(3*n):
            bigmatrix[i][j] = matrix[i%n][j%n]
            if bigmatrix[i][j]=='S' and i//n== 1:
                si, sj = i, j
    return bigmatrix, si, sj
bigmatrix, si, sj = migong(n, matrix)
def minpath(matirx, si, sj, N):
    rowlen = N
    collen = N
    # dp[i][j]表示从(0,0)到(i,j)的最短路径值
    dp = [[0 for i in range(collen)] for j in range(rowlen)]
    rowq = []
    colq = []
    dp[si][sj] = 1
    rowq.append(si)
    colq.append(sj)
    # 广度优先遍历
    while rowq:
        i = rowq.pop(0)
        j = colq.pop(0)
        # 遍历到最后一个位置
        if matrix[i][j]=='E':
            return dp[i][j]
        # 上
        walkto(dp[i][j], i - 1, j, matrix, dp, rowq, colq)
        # 下
        walkto(dp[i][j], i + 1, j, matrix, dp, rowq, colq)
        # 左
        walkto(dp[i][j], i, j - 1, matrix, dp, rowq, colq)
        # 右
        walkto(dp[i][j], i, j + 1, matrix, dp, rowq, colq)
    return -1
# 走向某个位置，pre 到(tor,toc)之前的最短路径
def walkto(pre, tor, toc, matrix, dp, rowq, colq):
    # 越界，位置为0,已经走过，直接返回
    if tor < 0 or tor == len(matrix) or toc <0 or toc == len(matrix[0]) or matrix[tor][toc] == '#' or dp[tor][toc] != 0:
        return
    dp[tor][toc] = pre + 1
    # 将位置坐标加入两个队列
    rowq.append(tor)
    colq.append(toc)
ans = getminmatrixlen(bigmatrix ,si, sj, N)
print(ans)