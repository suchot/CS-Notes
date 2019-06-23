class Solution(object):
    def search(self, nums, target):
        if not nums or  target == None:
            return -1
        min_index = self.search_min(nums)
        if min_index ==0:
            index = self.search_core(nums,target, 0, len(nums)-1)

        elif target >=nums[0]:
            index = self.search_core(nums, target, 0, min_index-1)
        else:
            index = self.search_core(nums, target, min_index, len(nums)-1)
        return index
        #二分查找旋转数组的最小值
    def search_min(self, nums):
        left, right = 0, len(nums)-1
        mid = left
        if not nums:
            return 0
        while nums[left]>=nums[right]:
            if right-left==1:
                mid = right
                break
            mid = left +((right- left)>>1)
            if nums[mid]>= nums[left]:
                left = mid
            else:
                right = mid 
        return mid
        #二分查找
    def search_core(self, nums, target, left, right):
        while left<=right:
            mid = left +((right- left)>>1)
            if nums[mid] == target:
                return mid
                break
            elif nums[mid]< target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    S = Solution()
    print(S.search(nums, target))