class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 = []
        stack2 = []
        temp_num = 0
        res = ''
        for i in s:
            if i.isdigit():
                temp_num = temp_num*10 + int(i)
            elif i == '[':
                if temp_num != 0:
                    stack1.append(temp_num)
                    temp_num = 0
                stack2.append(res)
                res = ''
            elif i.isalpha():
                res += i
            elif i == ']':
                res = stack2.pop() + stack1.pop()*res
        return res
            
            
if __name__ == "__main__":
    s = "3[a2[bc]]"
    S = Solution()
    print(S.decodeString(s))