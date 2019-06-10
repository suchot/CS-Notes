'''
从左到右不断交换相邻逆序的元素，在一轮的循环之后，可以让未排序的最大元素上浮到右侧。
每次上浮都会把最大的一位排在最后
在一轮循环中，如果没有发生交换，就说明数组已经是有序的，此时可以直接退出。
'''
class Solution(object):
    def bubble_sort(self, num):
        if not num:
            return []
        len_n = len(num)
        for i in range(len_n-1):
            for j in range(len_n-i-1):
                if num[j]> num[j+1]:
                    self.swap(num, j, j+1)
        return num
    def swap(self, num , i ,j):
        # num[i], num[j] = num[j], num[i]
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
if __name__ == "__main__":
    # num1 = [1,2,3,4,5]
    num1 = [5,4,3,4,3,2,1]

    S = Solution()
    print(S.bubble_sort(num1))