N = int(input())
ls = list(map(int, input().split()))
def local_Minimum(ls):
    if len(ls) == 1:
        return 0
    elif ls[0] < ls[1]:
        return 0
    elif ls[-1] < ls[-2]:
        return len(ls)-1
    else:
        left,right = 1, len(ls)-2
        mid = 0
        while left<right:
            mid = left +((right-left)>>1)
            if ls[mid]>ls[mid-1]:
                right = mid-1
            elif ls[mid]>ls[mid+1]:
                left = mid+1
            else:
                return mid
        return left
print(local_Minimum(ls))