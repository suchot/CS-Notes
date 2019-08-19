n = int(input())
Map = []
for i in range(n):
    l = list(map(int, input().split(',')))
    Map.append(l)

def findpath(Map):
    rows,cols = len(Map), len(Map[0])
    path = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0:
                path[i][j] = Map[i][j]
            elif i==0:
                path[i][j]=path[i][j-1]+Map[i][j]
            elif j==0:
                path[i][j]= path[i-1][j]+Map[i][j]
            else:
                path[i][j] = min(path[i-1][j], path[i][j-1])+Map[i][j]
    return path[-1][-1]
print(findpath(Map))

