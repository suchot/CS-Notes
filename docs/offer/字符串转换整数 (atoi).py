class Solution:
    def myAtoi(self, str: str) -> int:
        list_s = list(str.strip())
        if not list_s:
            return 0
        isnegative = False
        if list_s[0]== '-':
            isnegative = True
            list_s.pop(0)
        elif list_s[0] == '+':
            list_s.pop(0)
        res  = 0
        for i in list_s:
            num_i = ord(i)-ord('0')
            if num_i>10 or num_i<0:
                break
            res = res * 10 +num_i
        if res > 0x7FFFFFFF:
            if isnegative:
                res = 0x80000000
            else:
                res = 0x7FFFFFFF
        if isnegative:
            res = -res
        return res

        