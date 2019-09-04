n = int(input())
arr = list(map(int, input().split()))
def minsortlengh(arr, n):
    if n<2:
        return arr
    Min = arr[-1]
    noMinindex = -1
    for i in range(n-2, -1, -1):
        if arr[i]>Min:
            noMinindex = i
        else:
            Min = min(Min, arr[i])
    if noMinindex == -1:
        return 0
    Max = arr[0]
    nomaxindex = -1
    for j in range(1, n):
        if arr[j]<Max:
            nomaxindex = j
        else:
            Max = max(Max, arr[j])
    return nomaxindex-noMinindex+1

print(minsortlengh(arr, n))