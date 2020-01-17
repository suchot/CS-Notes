T = int(input())
def fuxi(n,m):
    c,v = [0 for i in range(n)], [0 for i in range(n)]
    for i in range(n):
        c[i],v[i] = map(int, input().split())
    F = [0 for i in range(m+1)]
    def ZeroOneBackPack(cost,value):
        for i in reversed(range(cost,m+1)):
            F[i] = max(F[i],F[i-cost]+value)
    for i in range(0,n):
        ZeroOneBackPack(c[i],v[i])
    return F[m]


for i in range(T):
    n,m = map(int, input().split())
    res =
    r = fuxi(n,m)
    print(r)