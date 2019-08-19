n = int(input())
length = list(map(int, input().split()))
person = int(input())
count = 0
def canfind(left, right, length):
    if right-left+1>47:
        return True
    elif right-left+1<3:
        return False
    else:
        arrs = sorted(length)
        for i in range(0,len(arrs)-2):
            if arrs[i]+arr[i+1]>arrs[i+2]:
                return True
            else:
                return False
for i in range(person):
    left, right = map(int, input().split())
    arr = length[left:right+1]
    if canfind(left, right, arr):
        count +=1
print(count)

# 链接：https://www.nowcoder.com/questionTerminal/9363dcb83ca44c61a2c1a8f65aa722b8
# 来源：牛客网
# 
# 思想 为什么47个以上必然有
# https://www.cnblogs.com/dogenya/p/11184311.html

n=int(input())
f=[int(x) for x in input().split()]
m=int(input())
sum=0
for _ in range(m):
    lr=input().split()
    l=int(lr[0])-1
    r=int(lr[1])-1
    if(r-l+1>=47):
        sum+=1
    else:
        num=f[l:r+1]
        num.sort()
        for i in range(0,len(num)-2):
            if num[i]+num[i+1]>num[i+2]:
                sum+=1
                break
print(sum)


