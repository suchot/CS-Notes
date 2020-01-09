N = int(input())
arr = list(map(int, input().split()))
matrix = []
for i in range(N):
    l = arr[i:N*N:N]
    matrix.append([_ for _ in l])
def maxsum(matrix, N)
    res = float('-inf')
    matrix=[[0]*N]+ matrix
    for i in range(1,N+1):
        matrix[i]=[matrix[i][index]+matrix[i-1][index] for index in range(N)]
    for r in range(1,N+1):
        for i in range(N-r+1):
            temps=[matrix[i+r][index]-matrix[i][index] for index in range(N)]
            temp=0
            for n in temps:
                temp = temp+n if temp>0 else n
                res = max(res,temp)
    return res
print(maxsum(matrix,N))