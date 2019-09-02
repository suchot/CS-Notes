n = int(input())
T = input()
m = int(input())
res = 0 
def check(n, t, s):
    lens = len(s)
    if lens>n:
        return False
    times = n//lens + 1
    s = s*times
    if s.find(t) != -1:
        return True
    else:
        return False
for i in range(m):
    S = input()
    if check(n, T, S):
        res+=1
print(res)