class Solution():
    def commonpart(self, num1, num2):
        res = []
        if not num1 or not num2:
            return []
        start1, start2 = 0,0
        end1, end2 = len(num1), len(num2)
        while start1<end1 and start2<end2:
            if num1[start1]<num2[start2]:
                start1 +=1
            elif num1[start1]>num2[start2]:
                start2 += 1
            else:
                res.append(num1[start1])
                start1+=1
                start2+=1
        return res
 
if __name__ == "__main__":
    S = Solution()
    n = int(input())
    num1 = list(map(int, input().split()))
    m = int(input())
    num2 = list(map(int, input().split()))
    res = S.commonpart(num1, num2)
    print(' '.join(map(str, res)))