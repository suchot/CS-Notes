'''
每次都将当前元素插入到左侧已经排序的数组中，使得插入之后左侧数组依然有序。

对于数组 {3, 5, 2, 4, 1}，它具有以下逆序：(3, 2), (3, 1), (5, 2), (5, 4), (5, 1), (2, 1), (4, 1)，插入排序每次只能交换相邻元素，令逆序数量减少 1，因此插入排序需要交换的次数为逆序数量。

插入排序的复杂度取决于数组的初始顺序，如果数组已经部分有序了，逆序较少，那么插入排序会很快。

平均情况下插入排序需要 ~N2/4 比较以及 ~N2/4 次交换；
最坏的情况下需要 ~N2/2 比较以及 ~N2/2 次交换，最坏的情况是数组是倒序的；
最好的情况下需要 N-1 次比较和 0 次交换，最好的情况就是数组已经有序了。
以下演示了在一轮循环中，将元素 2 插入到左侧已经排序的数组中。
插入排序总结：

当前需要排序的元素(array[i])，跟已经排序好的最后一个元素比较(array[i-1])，如果满足条件继续执行后面的程序，否则循环到下一个要排序的元素。
缓存当前要排序的元素的值，以便找到正确的位置进行插入。
排序的元素跟已经排序号的元素比较，比它大的向后移动(升序)。
要排序的元素，插入到正确的位置。
'''
class Solution(object):
    def insert_sort(self, num):
        if not num:
            return []
        len_n = len(num)
        for i in range(1, len_n):
            j = i
            while num[j]<num[j-1] and j >0:
                self.swap(num, j ,j-1)
                j -= 1
        return num

    def swap(self, num , i ,j):
        # num[i], num[j] = num[j], num[i]
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
if __name__ == "__main__":
    # num1 = [1,2,3,4,5]
    num1 = [-3,5, 1,1,3,4,5,6,1,1,2,6]

    S = Solution()
    print(S.insert_sort(num1))