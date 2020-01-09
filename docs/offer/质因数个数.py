def countgcd(n):
    res = 0
    flag = True
    while flag:
        t = int(pow(n, 0.5))+1
        for i in range(2,t):
            if n % i == 0:
                n /= i
                res += 1
                break
        else:
            flag = False
            break
    return res+1
if __name__ == "__main__":
    n = int(input())
    s = 0
    for i in range(2,n+1):
        s += countgcd(i)
    print(s)