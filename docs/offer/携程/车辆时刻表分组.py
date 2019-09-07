times = list(input())
def fenzu(times):
    res = []
    che = set(times)
    n = len(che)
    array = []
    def getindex(lst, item):
        return [index for (index, value) in enumerate(lst) if value==item]
    for i in range(n):
        chs = list(che)
        array.append([getindex(times, chs[i])[0],getindex(times, chs[i])[-1]])

    array = sorted(array, key=lambda x:(x[0],x[1]))
    return array
def merge(interval):
    lens = len(interval)
    res = []
    for inter in interval:
        if not res or res[-1][1]<inter[0]:
            res.append(inter)
        else:
            res[-1][1] = max(res[-1][1],inter[1])
    return res
    pass
array = fenzu(times)
arr = merge(array)
res = []
for a in arr:
    res.append(str(a[-1]-a[0]+1))
print(','.join(res))