def max_gap(arr):
    if not arr or len(arr)<2:
        return
    len_arr = len(arr)
    min_arr, max_arr = min(arr), max(arr)
    if max_arr==min_arr:
        return 0
    has_num = [False]*(len_arr+1)
    mins, maxs = [0]*(len_arr+1), [0]*(len_arr+1)
    temp = 0
    for i in range(len_arr):
        temp = bucket(arr[i], len_arr, min_arr, max_arr)
        mins[temp] = min(mins[temp],arr[i]) if has_num[temp] else arr[i]
        maxs[temp] = max(maxs[temp],arr[i]) if has_num[temp] else arr[i]
        has_num[temp]=True
    res = 0
    lastmax = maxs[0]
    i=1
    for i in range(len_arr+1):
        if has_num[i]:
            res = max(res, mins[i]-lastmax)
            lastmax = maxs[i]
    return res
def bucket(num, lens, Min, Max):
    return int((num-Min)*lens/(Max-Min))


if __name__ == "__main__":
    lens = int(input())
    arr = list(map(int,input().split()))
    print(max_gap(arr))

