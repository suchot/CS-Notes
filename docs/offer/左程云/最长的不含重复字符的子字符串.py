n = int(input())
arr =list(map(int, input().split()))
def larges(arr):
    if not arr:
        return 0
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = d.get(arr[i], -1)
    maxlen = 0
    pre = -1
    for i in range(len(arr)):
        if d[arr[i]] != -1 and d[arr[i]]>=pre:
            maxlen = max(maxlen, i-pre)
            pre = d[arr[i]]+1
        d[arr[i]] = i
 #   maxlen = max(maxlen,len(arr)-pre)
    return maxlen
print(larges(arr))