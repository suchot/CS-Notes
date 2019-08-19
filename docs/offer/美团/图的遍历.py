N = int(input())
l1 = [[] for _ in range(2*N)]
for _ in range(N-1):
    i,x = map(int, input().split())
    l1[i].append(x)
    print(l1)
def dfs(x, depth):
    temp = depth
    for i in l1[x]:
        temp = max(temp,dfs(i,depth+1))
    return temp
depth = dfs(1,0)
print(2*N-2-depth)
if __name__ == "__main__":
    N = 4
    