n = int(input())
matirx = []
for i in range(n):
    matirx.append(list(map(int, input().split())))
def (matirx, N):
    rows_1 = [[0]*N for i in range(N)]
    cols_1 = [[0]*N for i in range(N)]
    res = 0
    for row in range(N):
        for col in range(N):
            if col==0:
                rows_1[row][col] = matrix[row][col]
                cols_1[col][row] = matrix[col][row]
            else:
                if matrix[row][col]==1:
                    rows_1[row][col] = rows_1[row][col-1]+1
                if matrix[col][row]==1:
                    cols_1[col][row] = cols_1[col-1][row]+1
    for row in range(N):
        for col in range(N):
            for lens in range(N-max(row,col)):
                if matrix[row][col]==1 and rows_1[row][col+lens]-rows_1[row][col]==lens and rows_1[row+lens][col+lens]-rows_1[row+lens][col]==lens and cols_1[row+lens][col]-cols_1[row][col]==lens and cols_1[row+lens][col+lens]-cols_1[row][col+lens]==lens:
                    res = max(res,lens+1)
    print(res)