n,k = map(int, input().split())
s = input()
def maxunique(s,k):
    if not s:
        return ''
    unum = 0
    for i in range(k-1, -1, -1):
        if s[i].isupper():
            unum += 1
        else:
            break
    if unum&1==1:
        return s[k-1:k+1]
    elif s[k].isupper():
        return s[k:k+2]
    else:
        return s[k]
print(maxunique(s,k))