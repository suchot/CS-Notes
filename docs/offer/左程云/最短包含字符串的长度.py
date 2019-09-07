str1, str2 = input(), input()
tgt = {}
left = 0
right = 0
found = len(str2)
minlen = len(str1) + 1
for x in str2:
    tgt[x] = tgt.get(x, 0) + 1
while right < len(str1):
    if str1[right] not in tgt:
        right += 1
        continue
    tgt[str1[right]] -= 1
    if tgt[str1[right]]>=0:
        found -= 1
    if found==0:
        while tgt[str1[left]]<0:
            tgt[str1[left]] += 1
            left += 1
        minlen = min(minlen, right-left+1)
        found += 1
        tgt[str1[left]] += 1
        left += 1
    right += 1

if minlen <= len(str1):
    print(minlen)
else:
    print('0')