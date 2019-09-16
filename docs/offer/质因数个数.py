n = int(input())
def countgcd(n):
    res = 0
    while n > 1:
        flag = 1
        t = int(n**0.5)
        for i in range(2,t+1):
            if n % i == 0:
                n /= i
                res += 1
                flag = 0
                break
        if flag:
            res += 1
            break
    return res
s = 0
for i in range(2,n+1):
    s += countgcd(i)
print(s)