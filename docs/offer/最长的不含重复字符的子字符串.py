class Solution:
    def __init__(self):
        self.str = [-1 for i in range(256)]
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s
        start = 0
        max_len = 0
        for i in range(len_s):
            if self.str[ord(s[i])] != -1 and self.str[ord(s[i])] >= start:
                    max_len = max(max_len, i- start)
                    start = self.str[ord(s[i])] + 1       
            self.str[ord(s[i])] = i
        max_len = max(max_len, len_s - start)
        return max_len

if __name__ == "__main__":
    s = 'ggubk'
    S = Solution()
    print (S.lengthOfLongestSubstring(s))