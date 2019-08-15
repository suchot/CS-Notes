class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        lent = len(t)
        lens = len(s)
        if lent>lens:
            return ''
        left, right = 0, 0
        min_len = float('inf')
        min_word = ''
        while right<lens:
            words = s[left:right]
            while not self.statify(words, t) and right<lens:
                right += 1
                words = s[left:right]
            while self.statify(words, t) and left<=right:
                if right-left <min_len:
                    min_len = right-left
                    min_word = words
                left += 1
                words = s[left:right]

        return min_word
    def statify(self, words, t):
        if not words:
            return False
        w, t = list(words), list(t)
        words = sorted(w)
        t = sorted(t)
        j = 0
        i, t_end = 0, len(t)
        while i<t_end and j< len(words):
            if t[i]==words[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i==t_end

if __name__ == "__main__":
    S =Solution()
    s, t = "ADOBECODEBANC","ABC"
    print(S.minWindow(s, t))