class Solution:
    def threeSum(self, nums):
        nums.sort()
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, len(nums)-1
            while start< end:
                sum = nums[i]+nums[start]+nums[end]
                if sum == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
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