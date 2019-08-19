rows,cols = map(int, input().split())
matrix = []
for i in range(rows):
    c =  list(map(int, input().split()))
    matrix.append(c)
def sortmatrix(matrix):
    r, c = 0, 0
    r1, c1 = len(matrix)-1, len(matrix[0])-1
    res = []
    while r<=r1 and c<=c1:
        for j in range(c, c1+1):
            res.append(matrix[r][j])
        for i in range(r+1, r1+1):
            res.append(matrix[i][c1])
        if r != r1:
            for j in range(c1-1, c-1, -1):
                res.append(matrix[r1][j])
        if c != c1:
            for i in range(r1-1, r, -1):
                res.append(matrix[i][c])
        r += 1
        c += 1
        r1 -= 1
        c1 -= 1
    return res
print(sortmatrix(matrix))