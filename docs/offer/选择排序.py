'''
选择出数组中的最小元素，将它与数组的第一个元素交换位置。再从剩下的元素中选择出最小的元素，将它与数组的第二个元素交换位置。不断进行这样的操作，直到将整个数组排序。

选择排序需要 ~N2/2 次比较和 ~N 次交换，它的运行时间与输入无关，这个特点使得它对一个已经排序的数组也需要这么多的比较和交换操作。
'''

class Solution:
    def selection_sort(self, num):
        if not num:
            return []
        len_n = len(num)
        for i in range(len_n):
            min_num = i
            for j in range(i+1, len_n):
                if num[j] < num[min_num]:
                    min_num = j
            self.swap(num, i ,min_num)
        return num
    def swap(self, num , i ,j):
        # num[i], num[j] = num[j], num[i]
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
        # 下面这样交换　会导致因为　num[i]　和num[j]指向一个地址，　导致意想不到的错误
        # num[i] = num[j] + num[i]
        # num[j] = num[i] - num[j]
        # num[i] = num[i] - num[j]

if __name__ == "__main__":
    # num1 = [1,2,3,4,5]
    num1 = [-3,5, 1]

    S = Solution()
    print(S.selection_sort(num1))