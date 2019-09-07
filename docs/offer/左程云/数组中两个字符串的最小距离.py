n = int(input())
str1, str2 =map(str, input().split())

def mindistance(str1, str2, s):
    if not str1 or not str2:
        return -1
    if str1==str2:
        return 0
    last1 = -1
    last2 = -1
    Min = float('inf')
    for i in range(len(s)):
        if s[i]==str1:
            Min = min(Min, Min if last2 == -1 else i-last2)
            last1 = i
        if s[i]==str2:
            Min = min(Min, Min if last1 == -1 else i-last1)
            last2 = i
    return -1 if float('inf') == Min else Min
s = []
for i in range(n):
    s.append(input())
print(mindistance(str1, str2, s))




