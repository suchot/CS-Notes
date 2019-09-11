# class Solution():
#     def connect(self,arr):
#         j_num = arr[0]
#         arr =arr[1::]
#         arr.sort()
#         if len(arr)<=3:
#             return min(arr)
#         res  = 0
#         index = 0
#         while arr[-3] != 0:
#             res += arr[index]
#             if index + 3>=j_num:
#                 arr[-3]=0
#             else:
#                 for i in range(3,-1, -1):
#                     temp = arr[index]
#                     arr[index+i]-= temp
#             index+=1
#         return res

# if __name__ == "__main__":
#     S = Solution()
#     c = int(input())
#     con =[]
#     for i in range(c):
#         #l = list(map(int, input().split()))
#         l = [4,2,3,3,99]
#         print(S.connect(l))


import sys
 
 
def get_max_group(t, p):
    if t < 3:
        return 0
    if t == 3:
        return min(p)
    count = 0
    while True:
        p.sort(reverse=True)
        cur = p[2]
        if cur == 0:
            break
        count += cur
        p[:3] = list(map(lambda x: x - cur, p[:3]))
    return count
 
 
if __name__ == "__main__":
    c = int(sys.stdin.readline().strip())
    res = []
    for _ in range(c):
        t_p = list(map(int, sys.stdin.readline().strip().split()))
        # print(t_p)
        res.append(get_max_group(t_p[0], t_p[1:]))
    for i in res:
        print(i)
# 作者：就是suixin
# 链接：https://www.nowcoder.com/discuss/232530?type=post&order=time&pos=&page=3
# 来源：牛客网