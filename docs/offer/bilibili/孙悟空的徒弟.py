
nk = list(map(int,input().split()))
n = nk[0]
k = nk[1]
fight = sorted(list(map(int,input().split())))
res = []
for i in range(0, n):
    for j in range(1, i):
        num = fight[i] * fight[j]
        res.append(num)
res = sorted(res, reverse = True)
print(res[k - 1])