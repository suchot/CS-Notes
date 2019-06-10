# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # if not s or not pattern:
        #     return True
        return self.matchCore(s, pattern)
    def matchCore(self, s, pattern):
        if not s and not pattern:
            return True
        elif s and not pattern:
            return False
        elif not s and pattern:
            # pattern中的第二个字符为*，则pattern后移两位继续比较
            if len(pattern) > 1 and pattern[1] == '*':
                return self.matchCore(s, pattern[2:])
            else:
                return False
        if len(pattern) > 1 and pattern[1] == '*':
            if pattern[0] == s[0] or (pattern[0] == '.' and s):
                return self.matchCore(s[1:], pattern[2:]) or self.matchCore(s[1:],pattern) or self.matchCore(s, pattern[2:])
            else:
                return self.matchCore(s, pattern[2:])
        if s[0] == pattern[0] or (pattern[0]=='.' and s):
            return self.matchCore(s[1:], pattern[1:])
        return False