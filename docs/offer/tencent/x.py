from itertools import combinations
red = 1
white = 0
l = ['r' for i in range(red)]
l.extend(['w' for j in range(white)])
print(list(combinations(l,len(l))))
print(l)