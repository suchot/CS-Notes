shudu = []
for i in range(9):
    l = list(input())
    shudu.append(l)
def isvalid(shudu):
    row,col,cell = [[{},{},{},{},{},{},{},{},{}],[{},{},{},{},{},{},{},{},{}],[{},{},{},{},{},{},{},{},{}]]
    for x in range(9):
        for y in range(9):
            num =3*(x//3)+y//3
            temp = shudu[x][y]
            if temp != 'X':
                temp = int(temp)
                if temp not in row[x] and temp not in col[y] and temp not in cell[num]:
                    row[x][temp] = 1
                    col[y][temp] = 1
                    cell[num][temp]=1
                else:
                    return False
    return True
if isvalid(shudu):
    print('true')
else:
    print('false')