n = int(input())
arr = list(map(int, input().split()))

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def oddeven(arr):
    end = len(arr)-1
    even,odd = 0,1
    while even<=end and odd<=end:
        if (arr[end]&1)==0:
            swap(arr, end, even)
            even += 2
        else:
            swap(arr, end, odd)
            odd += 2
    return arr
print(oddeven(arr))