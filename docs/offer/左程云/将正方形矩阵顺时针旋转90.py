class Solution():
    def rotate(self, matrix):
        tr, tc = 0,0
        dr, dc = len(matrix)-1, len(matrix[0])-1
        while tr<dr:
            self.rotateEdge(matrix, tr, tc, dr, dc)
            tr+=1
            tc+=1
            dr-=1
            dc-=1
    def rotateEdge(self, matrix, tr, tc, dr, dc):
        times = dc-tc
        temp= 0
        for i in range(times):
            temp = matrix[tr][tc+i]
            matrix[tr][tc+i]=matrix[dr-i][tc]
            matrix[dr-i][tc]= matrix[dr][dc-i]
            matrix[dr][dc-i]=matrix[tr+i][dc]
            matrix[tr+i][dc]=temp
if __name__ == "__main__":
    S = Solution()
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    S.rotate(matrix)
    for i in range(n):
        print(' '.join(map(str,matrix[i])))
        

