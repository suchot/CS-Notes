class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for i in range(0, len(nums)-1):
            start, end = i+1, len(nums)-1
            while start < end:
                res = nums[i] + nums[start] +nums[end]
                if  abs(res-target) < diff:
                    diff = abs(res-target)
                    result = res
                if res > target:
                    end -= 1
                elif res <target:
                    start += 1
                else:
                    return result
        return result
                    