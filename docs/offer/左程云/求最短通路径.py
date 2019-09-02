class Solution():
    def min_steps(self,matrix, N_end, M_end):
        res = 0
        cols = len(matrix[0])
        rows = len(matrix)
        visited = [[0 for i in range(cols)] for j in range(rows)]
        visited[0][0]=1
        queue = [(0,0)]
        while queue:
            r,c = queue.pop(0)
            if r==rows-1 and c == cols-1:
                return visited[r][c]
            self.backtracking(visited[r][c], r-1, c, matrix, visited, queue)
            self.backtracking(visited[r][c], r+1, c, matrix, visited, queue)
            self.backtracking(visited[r][c], r, c-1, matrix, visited, queue)
            self.backtracking(visited[r][c], r, c+1, matrix, visited, queue)
        return res
    def backtracking(self, prev, r, c, matrix, visited, queue):
        if r<0 or r==len(matrix)  or c<0 or c==len(matrix[0]) or visited[r][c] !=0 or matrix[r][c]!=1:
            return 
        visited[r][c]=prev+1
        queue.append((r, c))

if __name__=='__main__':
    N,M = map(int,input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input())))
    S = Solution()
    print(S.min_steps(matrix,N-1,M-1))

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

