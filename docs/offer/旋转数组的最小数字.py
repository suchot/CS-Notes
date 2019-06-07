# -*- coding:utf-8 -*-
class Solution:
#这道题用的测试用例太少了　，两个逻辑相反的代码都能通过。
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left, right = 0, len(rotateArray) - 1
        mid = left
        while rotateArray[left] >= rotateArray[right]:
            if right-left==1:
                mid = right
                break
            mid = left + ((right-left)>>1)
            if (rotateArray[mid] == rotateArray[right]) and \
            (rotateArray[mid] == rotateArray[left]):
                return self.MinInOrder(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
                
        return rotateArray[mid]
    def MinInOrder(self, array, l, r):
        res = array[l]
        for i in array:
            if res > i:
                res = i
        return res


if __name__ == "__main__":
    rotateArray = [6,7,1,2,3,4,5]
    S = Solution()  
    print(S.minNumberInRotateArray(rotateArray))