x,y,n = map(int, input().split())
M =[[1 for i in range(1001)] for j in range(1001)]
for i in range(n):
    pos_x, pos_y = map(int, input().split())
    pos_x += 500
    pos_y += 500
    M[pos_x][pos_y] = 0

def getminmatrixlen(matrix):
    rowlen = len(matrix)
    collen = len(matrix[0])
    # dp[i][j]表示从(0,0)到(i,j)的最短路径值
    dp = [[0 for i in range(collen)] for j in range(rowlen)]
    rowq = []
    colq = []
    dp[500][500] = 1
    rowq.append(500)
    colq.append(500)
    # 广度优先遍历
    while rowq:
        i = rowq.pop(0)
        j = colq.pop(0)
        # 遍历到最后一个位置
        if i == x+500 and j == y+500:
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
    if tor < 0 or tor == len(matrix) or toc <0 or toc == len(matrix[0]) or matrix[tor][toc] != 1 or dp[tor][toc] != 0:
        return
    dp[tor][toc] = pre + 1
    # 将位置坐标加入两个队列
    rowq.append(tor)
    colq.append(toc)
ans = getminmatrixlen(M)-1
print(ans)
