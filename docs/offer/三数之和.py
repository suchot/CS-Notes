class Solution:
    def threeSum(self, nums):
        nums.sort()
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start< end:
                sum = nums[i]+nums[start]+nums[end]
                if sum == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif sum>0:
                    end -= 1
                else:
                    start += 1
        return res
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    S = Solution()
    print(S.threeSum(nums))