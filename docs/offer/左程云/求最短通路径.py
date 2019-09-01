
class Solution():
    def min_steps(self,matrix, N_end, M_end):
        visited = [[0 for i in range(M_end+1)] for j in range(N_end+1)]
        self.backtracking(matrix, 0, 0, visited, N_end, M_end, 0)
        return visited[-1][-1]
    def backtracking(self, matrix, r, c, visited, rows, cols, prev):
        if r<0 or r>rows or c>cols or c<0 or visited[r][c] !=0 or matrix[r][c]==0 or visited[-1][-1] !=0:
            return 
        visited[r][c] = prev+1    
        self.backtracking(matrix, r+1,c, visited, rows, cols,visited[r][c])
        self.backtracking(matrix, r-1,c, visited, rows, cols,visited[r][c])
        self.backtracking(matrix, r,c+1, visited, rows, cols,visited[r][c])
        self.backtracking(matrix, r,c-1, visited, rows, cols,visited[r][c])

if __name__=='__main__':
    N,M = map(int,input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,list(input()))))
    S = Solution()
    print(S.min_steps(matrix,N-1,M-1))
    pass