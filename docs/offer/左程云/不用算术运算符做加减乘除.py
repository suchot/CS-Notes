a, fun, b = input().split()
a = int(a)
b = int(b)
def add(a,b):
    res = a
    while b != 0:
        res = a^b
        b = (a&b)<<1
        a = res
    return res
def minus(a, b):
    negb = add(~b,1)
    res = add(a, negb)
    return res
def multi(a, b):
    res = 0
    while b != 0:
        if b&1==1:
            res = add(res, a)
        a = a<<1
        b = b>>1
    return res
def div(a, b):
    
def divide(a, b):

    res = 1
    if b==0:
        return 'Error'
    min_value = -2147483648
    if a<=min_value and b<=min_value:
        return 1
    elif b<=min_value:
        return 0
    elif a<=min_value:
        temp = div(add(a,1),b)
        res = add(temp, div(minus(a, multi(temp,b)), b))
        return res
    else:
        return div(a,b)


if fun=='+':
    print(add(a,b))
elif fun == '-':
    print(minus(a,b))
elif fun== '*':
    print(multi(a,b))
elif fun == '/':
    print(div(a,b))