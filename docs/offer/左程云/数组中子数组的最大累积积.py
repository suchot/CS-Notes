
n = int(input())
arr = list(map(float, input().split()))

def maxproduct(arr):
    mx,mn, res= arr[0],arr[0], arr[0]
    maxend, minend = 0, 0
    for i in range(1, len(arr)):
        maxend = mx*arr[i]
        minend = mn*arr[i]
        mx=max(maxend, minend, arr[i])
        mn = min(minend,maxend,arr[i]) 
        res = max(res, mx)
    return res
print('%.2f' % (maxproduct(arr)))