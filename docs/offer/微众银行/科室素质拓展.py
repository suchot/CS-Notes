链接：https://www.nowcoder.com/questionTerminal/dd7fe2adc9ec4da5a91da1e224a7ad55?orderByHotValue=1&page=1&onlyReference=false
来源：牛客网

from itertools import combinations
s = [1,2,3,4,5,6,7,8,9]
s_input = input().split()
k = s_input[0]
# print(k)
n = s_input[1]
# print(n)
com_list = list(combinations(s,int(k)))
#print(com_list)
num = 0
for i in com_list:
    total = 0
    for j in i:
        total += j
    if total == int(n):
        num += 1
        for z in i:
            print(z,end=" ")
        print("\t")
if num==0:
    print("None")