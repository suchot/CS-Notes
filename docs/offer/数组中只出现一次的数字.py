# # -*- coding:utf-8 -*-
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         # write code here
#         #先把所有的数求异或,得到结果后某一位为１
#         all, a, b = 0, 0, 0
#         for i in array:
#             all ^= i
#         index = 0
#         #　得到某一位的值为１，按照这一位来将数组划分为两个　分别存在一位不一样的数的数组
#         while not all&1:
#             all = all>>1
#             index += 1
# #        s1, s2 = [], []
# #        for i in array:
# #            if (i>>index)&1==1:
# #                s1.append(i)
# #            else:
# #                s2.append(i)
# #        for i in s1:
# #            a ^= i
# #        for i in s2:
# #            b ^= i
# #        return [a,b]
#     #改进
#         for i in array:
#             if (i>>index)&1==1:
#                 a ^= i
#             else:
#                 b ^= i
#         return [a,b]

# 整理之后的写法
  # -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        #先把所有的数求异或,得到结果后某一位为１
        a,b = 0,0
        index = self.findindex(array)
        for i in array:
            if self.isbit(i, index):
                a ^= i
            else:
                b ^= i
        return [a,b]
    def findindex(self, array):
        all = 0
        for i in array:
            all ^= i
        index = 0
        while all !=1:
            index += 1
            all = all >> 1
        return index
    def isbit(self, num, index):
        return (num>>index)&1   
if __name__ == "__main__":
    s = [1,1,3,6]
    S = Solution()
    S.FindNumsAppearOnce(s)
