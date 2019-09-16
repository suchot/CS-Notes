def p(x):
    y = reduce(lambda x,y: x*y, map(int, str(x)))
    return y and x % y
def q(x):
    return p(x) and p(x+1)
print sum(q(x) for x in xrange(2019))