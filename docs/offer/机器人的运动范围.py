class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows == 0 or cols == 0 or threshold <= 0:
            return 0
        visited = [0]*(rows*cols)
        count_all = self.movingcountcore(threshold, rows, cols, 0, 0, visited)
        return count_all
    def movingcountcore(self, threshold, rows, cols, r, c, visited):
        count = 0 # 先定义很关键
        if self.check(threshold,rows, cols, r, c, visited):
            visited[r*cols+c] = 1
            count = (1 + self.movingcountcore(threshold, rows, cols, r+1, c, visited) +
                    self.movingcountcore(threshold, rows, cols, r-1, c, visited) + 
                    self.movingcountcore(threshold, rows, cols, r, c+1, visited) + 
                    self.movingcountcore(threshold, rows, cols, r, c-1, visited))

        return count
                 
    def check(self, threshold, rows, cols, r, c, visited):
        if r>=0 and r<rows and c>=0 and c<cols and visited[r*cols+c]==0:

            if (self.getdigitsum(r)+self.getdigitsum(c))<=threshold:
                return True
        
        return False
                
            
    def getdigitsum(self, num):
        sum_num = 0
        while num > 0:
            sum_num += num%10
            num //= 10
        return sum_num


if __name__ == "__main__":
    pass