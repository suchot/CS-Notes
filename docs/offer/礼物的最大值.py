# -*- coding:utf-8 -*-

class Bonus:
    def getMost(self, board):
        # write code here
        row, col = 6, 6
        if not board:
            return 0
        
        dp = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                up, left = 0, 0
                if i>0 :
                    up  = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
                
                dp[i][j]= max(left, up) + board[i][j]
        maxvalue = dp[-1][-1]
        return maxvalue
    def getMost2(self, board):
        # write code here
        row, col = 6, 6
        if not board:
            return 0
        
        dp = [0 for i in range(col)]
        for i in range(row):
            for j in range(col):
                up, left = 0, 0
                if i>0 :
                    up  = dp[j]
                if j>0:
                    left = dp[j-1]
                
                dp[j]= max(left, up) + board[i][j]
        maxvalue = dp[-1]
        return maxvalue
