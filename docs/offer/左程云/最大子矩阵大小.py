# 通过75%，然后超时
class Solution():
    def maxrecsize(self, Map):
        rows, cols = len(Map), len(Map[0])
        if not Map or not rows or not cols :
            return 0
        maxarea = 0
        height = [0 for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                height[j] = 0 if Map[i][j]==0 else height[j]+1
            maxarea = max(maxarea, self.maxrecfrombottom(height))
        return maxarea
    def maxrecfrombottom(self, height):
        if not height:
            return 0
        lenh = len(height)
        maxarea = 0
        stack = []
        for i in range(lenh):
            while stack and height[i]<=height[stack[-1]]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                curarea = (i-k-1)*height[j]
                maxarea = max(maxarea,curarea)
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            curarea = (lenh-k-1)*height[j]
            maxarea = max(maxarea,curarea)
        return maxarea


if  __name__ == "__main__":
    rows, cols = map(int, input().split())
    Map = []
    for i in range(rows):
        l =  list(map(int,input().split()))
        Map.append(l)
    S = Solution()
    print(S.maxrecsize(Map))