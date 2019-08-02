class Solution:
    def findDuplicate(self, nums):
        n = len(nums)-1
        left, right =1 , n
        while left<right:
            mid = left+((right-left)>>1)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return right
if __name__ == "__main__":
    nums = [1,3,4,2,1]
    S = Solution()
    print(S.findDuplicate(nums))