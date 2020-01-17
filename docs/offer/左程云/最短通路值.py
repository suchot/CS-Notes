# class Solution():
#    def findPath(self, matrix, n, m):
#       res =0
#       visited = [[0 for i in range(m)] for j in range(n)]
#       visited[0][0]=1
#       deque = [(0,0)]
#       while deque:
#          row, col = deque.pop(0)
#          if row == n-1 and col == m-1:
#             return visited[row][col]
#          self.dfs(visited[row][col],row-1, col, matrix, visited, deque)
#          self.dfs(visited[row][col],row+1, col, matrix, visited, deque)
#          self.dfs(visited[row][col],row, col-1, matrix, visited, deque)
#          self.dfs(visited[row][col],row, col+1, matrix, visited, deque)
#       return res
#    def dfs(self, pre, r, c, matirx, visited, deque):
#       if r<0 or r>=n or c<0 or c>=m or matirx[r][c]!=1 or visited[r][c]!=0:
#          return 
#       visited[r][c] = pre + 1
#       deque.append((r,c))

# if __name__ == "__main__":
#    S = Solution()
#    n,m = map(int, input().split())
#    matrix = []
#    for i in range(n):
#       matrix.append(list(map(int, input())))
#    # matrix = [[0 for i in range(m)] for j in range(n)]
   
#    print(S.findPath(matrix, n, m))   
N, M = map(int, input().split())
matrix = []
for i in range(N):
    add = list(map(int, input()))
    matrix.append(add)
def getminmatrixlen(matrix):
    rowlen = len(matrix)
    collen = len(matrix[0])
    # dp[i][j]表示从(0,0)到(i,j)的最短路径值
    dp = [[0 for i in range(collen)] for j in range(rowlen)]
    rowq = []
    colq = []
    dp[0][0] = 1
    rowq.append(0)
    colq.append(0)
    # 广度优先遍历
    while rowq:
        i = rowq.pop(0)
        j = colq.pop(0)
        # 遍历到最后一个位置
        if i == (rowlen - 1) and j == (collen - 1):
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
ans = getminmatrixlen(matrix)
print(ans)

