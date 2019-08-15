class Solution:
    def mergesort(self, array):
            if len(array) <=1 :
                return array
            mid = len(array)>>1
            left = self.mergesort(array[:mid])
            right = self.mergesort(array[mid:])
            return self.mergesortCore(left, right)
    def mergesortCore(self, left, right):
        l_start, l_end = 0, len(left) 
        r_start, r_end = 0, len(right)
        res = []
        while l_start< l_end and r_start <r_end:
            if left[l_start] < right[r_start]:
                res.append(left[l_start])
                l_start += 1
            else:
                res.append(right[r_start])
                r_start += 1
        if l_start == l_end:
            res.extend(right[r_start:])
        else:
            res.extend(left[l_start:])
        return res
    def mergesort(num,start, end):
        if start<end:
            mid = start+ ((end-start)>>1)
            left = self.mergesort(num, start, mid)
            right = self.mergesort(num, mid+1, end)
            self.merge(left, right)
    def merge(self, left, right):
        merged = []
        while left and right:
            if left[0]<right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        if left:
            merged.extend(left)
        if right:
            merged.extend(right)
        return merged
if __name__ == "__main__":
    array = [4,5,-7,1,2,3]
    S = Solution()
    print(S.mergesort(array))