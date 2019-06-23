class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0': return num2
        if num2 == '0': return num1
        res  = [0] * (max(len(num1), len(num2))+1)
        res_index = 0
        i, j = len(num1)-1, len(num2)-1
        while i>=0 or j>=0:
            if i>=0:
                res[res_index] += ord(num1[i]) - ord('0')
            if j>=0:
                res[res_index] += ord(num2[j]) - ord('0')
            res[res_index+1] += res[res_index]//10
            res[res_index] = res[res_index]%10
            res_index += 1
            i -= 1
            j -= 1
        if res[-1] == 0:
            res = res[:-1]
        res.reverse()
        res = map(str, res)
        return ''.join(res)
        