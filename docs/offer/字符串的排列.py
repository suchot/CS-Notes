class Solution:
    def __init__(self):
        self.res = []
    def Permutation(self, ss):
        if not ss:
            return ss
        self.permutationCore(list(ss), 0, len(ss))
        r = sorted(list(set(self.res)))
        return r
    def permutationCore(self, str,start, end):
        if(start==end):
            s = ''.join(str)
            self.res.append(s)
        for i in range(start, end):
            #第一步交换所有第一个字符和后面所有字符
            str[start], str[i]=str[i],str[start]
            #第二步固定第一个字符，求后面所有字符的排列
            self.permutationCore(str,start+1,end)
            #注意之后要再换回来
            str[start], str[i] = str[i], str[start]
