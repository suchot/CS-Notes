n = int(input())
m = int(input())
g = [[float('inf') for i in range(n)] for j in range(n)]
ans = float('inf')
for i in range(m):
    a,b,c = map(int,input().split())
    if g[a][b]>c:
        g[a][b]=c
        g[b][a]=c
Map = [[g[i][j] for i in range(n)] for j in range(n)]
for k in range(n):
    for i in range(k):
        for j in range(1)
        ans = min(ans, Map[i][j]+g[i][k]+g[k][j])

    for i in range(n):
        for j in range(n):
            Map[i][j] = min(Map[i][j], Map[i][k]+Map[k][j])
if ans >= (10**9):
    print(-1)
else:
    print(2*ans+1)


