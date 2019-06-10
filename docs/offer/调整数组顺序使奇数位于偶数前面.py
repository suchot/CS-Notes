class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in array:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        odd.extend(even)
        return odd