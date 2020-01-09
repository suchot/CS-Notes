n = int(input())
ai  = list(map(int, input().split()))
bi = list(map(int, input().split()))
def baowenxiang(n, a, b):
    d = [(a[i], b[i]) for  i in range(n)]
    all_a = sum(a)
    d.sort(key= lambda x: [-x[1],x[0]])
    minneed, need = 0,0
    for i in range(n):
        need += d[i][1]
        if need >= all_a:
            minneed = i+1
            break
    mintime = 0
    for i in range(minneed, n):
        mintime += d[i][0]
    
    return minneed, mintime

print('%d %d' %(baowenxiang(n,ai,bi)))