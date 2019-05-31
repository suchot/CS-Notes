# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = list(s)
        lens = len(new_s)
        space_num = 0
        for i in s:
            if i == ' ':
                space_num += 1
        res = [i for i in range(lens+ 2*space_num)]
        q, p = lens-1, len(res)-1
        while q>=0:
            if new_s[q] == ' ':
                res[p] = '0'
                res[p-1] = '2'
                res[p-2] = '%'
                p = p-3
                q = q-1
            else:
                res[p] =new_s[q]
                p -= 1
                q -= 1
        res = ''.join(res)
        return res