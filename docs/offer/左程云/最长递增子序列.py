n = int(input())
arr = list(map(int, input().split()))
def lis(n, arr):
    dp = [1 for i in range(n)]
    ends = [0 for i in range(n)]
    ends[0] = arr[0]
    right = 0
    l, r, m = 0, 0, 0
    for i in range(n):
        l = 0
        r = right
        while l<=r:
            m =l+((r-l)>>1)
            if arr[i]>ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right , l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return dp
def generatelis(dp, arr):
    len = max(dp)
    index = dp.index(len)
    lis = [0 for i in range(len)]
    lis[-1] = arr[index]
    for  i in range(index, -1, -1):
        if (arr[i]<arr[index] and dp[i]== dp[index]-1):
            index = i
            len -= 1
            lis[len-1]=arr[i]
    return lis
dp = lis(n,arr)
print(generatelis(dp, arr))