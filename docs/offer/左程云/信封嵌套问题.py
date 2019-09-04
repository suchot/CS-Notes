n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
def numsort(arr, n):
    arr = sorted(arr, key = lambda x:(x[0],-x[1]))
    new_arr = [arr[i][1] for i in range(n)]
    return new_arr
def lis(arr, n):
    right = 0
    dp =[1 for i in range(n)]
    ends = [0 for i in range(n)]
    ends[0]=arr[0]
    l,r,m = 0,0,0
    for i in range(n):
        l = 0
        r = right
        while l<=r:
            m =l +((r-l)>>1)
            if arr[i] > ends[m]:
                l = m + 1
            elif arr[i]==ends[m]:
                flag 
            else:
                r = m - 1
        right = max(right, l)
        dp[i] = l + 1
        ends[l] = arr[i]
    return dp
newarr = numsort(arr,n)
dp = lis(newarr,n)
print(max(dp))