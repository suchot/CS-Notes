class Solution():
    def removedupletter(self, s):
        if not s1:
            return False
        dict_s = {}
        for char in s:
            dict_s[char] = dict_s.get(char, 0)+1
        
        

if __name__ == "__main__":
    S = Solution()
    s1 = input()
    print(S.removedupletter(s1))