class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a=[1]*len(nums)
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    a[i]=max(a[i],a[j]+1)
        return max(a)
        """
        a=[]
        if len(nums)==0:
            return 0
        a.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>a[-1]:
                a.append(nums[i])
            elif nums[i]<a[0]:
                a[0]=nums[i]
            else:
                position=self.binarySearch(a,nums[i],0,len(a)-1)
                a[position]=nums[i]
        return len(a)
            
    def binarySearch(self,a,number,left,right):
        if left==right:
            return left
        while left<right:
            mid=(left+right)//2
            if mid==left or mid==right:
                if number>a[left]:
                    return right
                else:
                    return left
            if number<a[mid]:
                return self.binarySearch(a,number,left,mid)
            else:
                return self.binarySearch(a,number,mid,right)


if __name__ == "__main__":
    S = Solution()
    num = [4,2,3,4,5]
    print(S.lengthOfLIS(num))
        