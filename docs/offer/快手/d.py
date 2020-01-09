n = int(input())
def gcdcount(n):
    count = 0
    while n>2:
        sprt= int(n**0.5)+1
        for i in range(2, sprt):
            if n%i==0:
                count +=1
                n //= i
                break
        else:
            count+=1
            break
    return count
res = 0
for i in range(1,n+1):
    res += gcdcount(i)
    print(res)
