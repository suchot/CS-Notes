s = 'zai lai yi bian'
ls = s.split(' ')
res =[]
for strs in ls:
    if len(strs)%2==1:
       res.append(strs[::-1])
    else:
        res.append(strs)
print(res) 
