# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s, k):
        # write code here
        if not s:
            return -1
        dict_s = {}
        for i in s:
            dict_s[i]  = dict_s.get(i, 0) + 1
        for index, i in enumerate(s):
            if dict_s[i]==1:
                if k==1:
                    return '['+s[index]+']'
                else:
                    k -= 1
        return  'Myon~'
if __name__ == "__main__":
    S = Solution()
    try:
        while True:
            ins = input().split(' ')
            k = int(ins[0])
            s = ' '.join(ins[1:])
            print(S.FirstNotRepeatingChar(s,k))
    except:
        pass