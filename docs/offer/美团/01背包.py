N,V = map(int, input().split())
v, w = [0 for i in range(N+1)],[0 for j in range(N+1)]
B = [[0 for i in range(V+1)] for j in range(N+1)]

# for i in range(1,N+1):
#     v[i],w[i]= map(int, input().split())
# for i in range(1, N+1):
#     for j in range(1, V+1):
#         if v[i]<j:
#             B[i][j]=B[i-1][j]
#         else:
#             B[i][j]=max(B[i-1][j], B[i-1][j-v[i]]+w[i])
            
# print(B[-1][-1])

for i in range(1,N+1):
    v[i],w[i]= map(int, input().split())
for i in range(1, N+1):
    for j in range(V, -1,-1):
            B[i][j]=max(B[i-1][j], B[i-1][j-v[i]]+w[i])
            
print(B[-1][-1])