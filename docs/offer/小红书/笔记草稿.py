# 题目描述：
# 薯队长写了一篇笔记草稿，请你帮忙输出最后内容。

# 1.输入字符包括英文字符，"(" , ")" 和 "<"。

# 2.英文字符表示笔记内容。

# 3. (  ) 之间表示注释内容，任何字符都无效。 括号保证成对出现。

# 4. "<" 表示退格, 删去前面一个笔记内容字符。 括号不受 "<" 影响 。

# 输入
# 输入一行字符串。长度 <= 10000.

# 输出
# 输出一行字符串，表示最终的笔记内容。


# 样例输入
# a<<b((c)<)
# 样例输出
# b

# 提示
# a退格删除掉了， 括号里面的c不要,  最后一个< 无效

s = input()
def draft(s):
    res = []
    if not s:
        return ''
    s = list(s)
    lens = len(s)
    i=0
    flag = 0
    while i<lens:
        if s[i]=='<':
            try:
                if s[i-1] != ')' or s[i-1] != '(':
                    del res[-1]
                    i += 1
            except:
                i += 1
                pass
        elif s[i]=='(':
            flag=1
            i += 1
            while  flag != 0:
                if  s[i] == ')':
                    flag -= 1
                    
                if s[i]== '(':
                    flag  += 1
                i += 1
        else:
            res.append(s[i])
            i += 1
    return res
                        
print(''.join(draft(s)))
    