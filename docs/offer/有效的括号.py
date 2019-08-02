class Solution:
    def isValid(self, s: str) -> bool:
        dict_k ={'}':'{', ')':'(', ']':'['}
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            if i == '(' or i == '{' or i =='[':
                stack.append(i)
            elif  i == ')' or i == '}' or i ==']':
                try:
                    if stack[-1] == dict_k[i]:
                        stack.pop()
                    else:
                        return False
                except:
                    return False
        if not stack:
            return True
        else:
            return False
if __name__ == "__main__":
    s = "(])"
    S = Solution()
    print(S.isValid(s))