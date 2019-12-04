n= int(input())
arr = list(map(int,input().split()))
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
def miss__pos(arr):
    l, r = 0, len(arr)
    while l<r:
        if arr[l] == l+1:
            l += 1
        elif arr[l]<=l or arr[l]>r or arr[arr[l]-1]==arr[l]:
            r-=1
            arr[l] = arr[r]
        else:
            swap(arr, l, arr[l]-1)
    return l+1
print(miss__pos(arr))
