N = int(input())
nums = list(map(int, input().split()))

if not nums:
    print(0)
res=0
leftmax = [0 for i in range(N)]
rightmax = [0 for i in range(N)]
leftmax[0] = nums[0]
rightmax[N-1] = nums[N-1]
for i in range(1, N):
    leftmax[i] = max(leftmax[i-1], nums[i])
for i in range(N-2, -1, -1):
    rightmax[i] = max(rightmax[i+1], nums[i])
for i in range(1, N-1):
    res += max(min(leftmax[i], rightmax[i])-nums[i],0)
print (res)